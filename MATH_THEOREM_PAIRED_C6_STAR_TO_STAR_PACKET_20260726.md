# A literal paired-\(C_6\) star-to-star router and the no-repeat invariant

Date: 2026-07-26

This note completes the star-to-triangle seam left open by
'MATH_THEOREM_SMALLEST_MOVING_EXTERIOR_C6_PACKET_20260726.md'.

One fresh hub and one oppositely switched terminal \(C_6\) convert the
triangle output back into a common-core star.  The resulting two settings
are literal equal-length Johnson geodesic packets, have identical complete
\(X/Y\) ledgers, and induce the absolute twists \(\tau\) and
\(\tau^{-1}\).

The packet is directly installable as one local router.  It is not directly
repeatable along one minimum wreath: the transported output petal was
inserted by the first packet, while every second nontrivial star router
would have to remove it.  This is a statewise geodesicity obstruction, not
a missing incidence count.

## 1. The first half

Use the data from the smallest packet:

\[
 |C|=m-3,\qquad u,v,k,a_0,a_1,a_2,
\]

all disjoint, with indices modulo three.  Put

\[
\begin{aligned}
 S_i&=C\cup\{u,k,a_i\},\\
 U_i&=C\cup\{u,k,a_i,a_{i+1}\},\\
 T_i&=C\cup\{u,a_i,a_{i+1}\},\\
 V_i&=C\cup\{u,v,a_i,a_{i+1}\},\\
 A_i&=C\cup\{v,a_i,a_{i+1}\}.
\end{aligned}                                           \tag{1.1}
\]

Thus

\[
                         S_i-U_i-T_i-V_i-A_i            \tag{1.2}
\]

is the old two-exchange geodesic, and

\[
 S_0-U_0-S_1-U_1-S_2-U_2-S_0                           \tag{1.3}
\]

is its first common-core alternating \(C_6\).

## 2. The terminal seam

Choose one further coordinate \(k'\), disjoint from all data above, and
define

\[
\begin{aligned}
 Z_i&=C\cup\{v,k',a_i,a_{i+1}\},\\
 B_i&=C\cup\{v,k',a_i\}.
\end{aligned}                                           \tag{2.1}
\]

The terminal incidences form the second common-core cycle

\[
                         B_0-Z_0-B_1-Z_1-B_2-Z_2-B_0.   \tag{2.2}
\]

There are two correlated settings.

**Positive setting:** leave (1.3) in its old orientation and use the
shifted terminal matching:

\[
 \boxed{
 \mathcal Q_i^+:
 S_i-U_i-T_i-V_i-A_i-Z_i-B_{i+1}.}                     \tag{2.3}
\]

**Negative setting:** toggle (1.3) and use the unshifted terminal matching:

\[
 \boxed{
 \mathcal Q_{i+1}^-:
 S_{i+1}-U_i-T_i-V_i-A_i-Z_i-B_i.}                     \tag{2.4}
\]

Thus the two \(C_6\)'s are switched oppositely.  Switching only one of
them does not give the geodesic packet proved below.

## 3. Literal geodesicity and monodromy

### Theorem 3.1 (paired-\(C_6\) physical router)

Both (2.3) and (2.4) are three pairwise vertex-disjoint Johnson geodesics
of length three.  The positive setting induces \(\tau:i\mapsto i+1\);
the negative setting induces \(\tau^{-1}:i\mapsto i-1\).

#### Proof

In the positive path rooted at \(S_i\), the exchanges are

\[
                  k\mapsto a_{i+1},\qquad
                  u\mapsto v,\qquad
                  a_i\mapsto k'.                       \tag{3.1}
\]

All three removed coordinates belong to \(S_i\), all three inserted
coordinates are absent from \(S_i\), and every inserted coordinate remains
in \(B_{i+1}\).  Therefore

\[
                         d_J(S_i,B_{i+1})=3,            \tag{3.2}
\]

and (2.3) is geodesic.  Its output label is \(i+1\).

For the negative path rooted at \(S_j\), put \(i=j-1\) in (2.4).  Its
exchanges are

\[
                  k\mapsto a_{j-1},\qquad
                  u\mapsto v,\qquad
                  a_j\mapsto k'.                       \tag{3.3}
\]

Again all exchanges are permanent, so

\[
                         d_J(S_j,B_{j-1})=3.            \tag{3.4}
\]

Its output label is \(j-1\).

Vertex-disjointness is visible layer by layer.  Within a layer, the
singletons \(a_i\) or adjacent pairs \(\{a_i,a_{i+1}\}\) are distinct.
Across lower layers, the membership pattern of \(u,v,k,k'\) is,
respectively,

\[
\begin{array}{c|cccc}
 &u&v&k&k'\\ \hline
S&1&0&1&0\\
T&1&0&0&0\\
A&0&1&0&0\\
B&0&1&0&1,
\end{array}                                             \tag{3.5}
\]

and the three upper layers \(U,V,Z\) have the corresponding distinct
patterns.  Hence no cross-layer collision occurs. \(\square\)

The common boundary geometries are now both stars:

\[
 \bigcap_iS_i=C\cup\{u,k\},\qquad
 \bigcap_iB_i=C\cup\{v,k'\},                            \tag{3.6}
\]

each of size \(m-1\).  Thus the intersection-cardinality obstruction of
the one-\(C_6\) packet has been removed with one additional exchange.

## 4. Exact \(X/Y\) and collar ownership

### Theorem 4.1 (complete ledger)

The positive and negative settings use exactly the same vertices:

\[
\mathcal X_{\rm packet}
 =\{S_i,T_i,A_i,B_i:i\in\mathbb Z_3\},                 \tag{4.1}
\]

\[
\mathcal Y_{\rm packet}
 =\{U_i,V_i,Z_i:i\in\mathbb Z_3\}.                     \tag{4.2}
\]

Every vertex occurs once in either setting.  In particular,

\[
                         \Delta_{\mathcal X}
 =\Delta_{\mathcal Y}=0.                               \tag{4.3}
\]

#### Proof

Equations (2.3) and (2.4) differ only in the incidence matching at the
first \(C_6\) and the opposite incidence matching at the terminal
\(C_6\).  All displayed vertices are unchanged.  The distinctness proof
in Theorem 3.1 shows that the multisets are sets. \(\square\)

The three collars, with no suppressed crossing state, are

\[
\begin{array}{c|c|c}
\text{exchange}&\text{upper state}&\text{following lower state}\\ \hline
k\mapsto a_{i+1}&U_i&T_i\\
u\mapsto v&V_i&A_i\\
a_i\mapsto k'&Z_i&B_{i+1}
\end{array}                                             \tag{4.4}
\]

in the positive setting; the negative setting replaces \(i+1\) by
\(i-1\) in the transported petal while retaining the same literal
\(U_i,V_i,Z_i\).  The mixed exterior collar \(V_i\) contains both \(u\)
and \(v\), and the terminal collar \(Z_i\) contains the fresh hub \(k'\).
Thus (4.1)--(4.4) are the full local \(X/Y\) collar accounting.

As in the one-\(C_6\) packet, each three-exchange list can be completed by
unused coordinates to an omitted-coordinate permutation.  Hence every
displayed path is a literal contiguous minimum-wreath segment, not merely
an abstract \(b\)-factor path.

## 5. Minimality of the seam

The triangle family \(\{A_i\}\) has total intersection \(C\cup\{v\}\),
of size \(m-2\).  Any common-core star family of \(m\)-sets has total
intersection of size \(m-1\).  A coordinate relabelling cannot change
intersection cardinality, so a zero-length seam is impossible.

One Johnson exchange can increase the common intersection by at most one:
each row changes only one coordinate.  The terminal step

\[
                         A_i-Z_i-B_{i+1}
\]

does increase it by one, from \(C\cup\{v\}\) to
\(C\cup\{v,k'\}\).  Therefore the one-exchange seam in Section 2 is
minimal.

The metric correction again matters.  Pairing the first \(C_6\) and
terminal \(C_6\) with the same orientation would make one setting retain
a previously inserted petal and the other remove it, producing unequal
endpoint distances.  The opposite pairing in (2.3)--(2.4) makes all three
exchanges permanent in both settings.

## 6. The direct no-repeat invariant

The star-to-star form makes direct concatenation set-theoretically possible,
but global geodesicity supplies a new obstruction.

### Theorem 6.1 (no direct serial repetition)

Fix either setting of the paired packet.  For the path rooted at \(S_i\),
the unique row-varying output coordinate is

\[
                         a_{\tau^{\pm1}(i)},             \tag{6.1}
\]

and this coordinate was inserted during that packet.  Any immediately
following nonidentity star-to-star router on the same three output strands
must remove this coordinate.  Consequently the concatenated path is not a
Johnson geodesic.

#### Proof

The input family \(\{S_i\}\) and output family \(\{B_i\}\) are stars.
After their common intersections are removed, each row has exactly one
petal.  A nonidentity permutation of the star labels changes that petal,
so the old output petal is absent from the next output and must be removed
somewhere in the next packet.

By (3.1) or (3.3), that old output petal was absent at the beginning of
the first packet and inserted during it.  It is therefore inserted and
later removed in the concatenation.  A Johnson geodesic never changes one
coordinate twice: every removed coordinate belongs to the initial set and
every inserted coordinate belongs to the final set.  Hence the
concatenation is not geodesic. \(\square\)

The choice of the next common hub does not evade the proof.  The hub may be
taken from an untouched common background coordinate, but the only
row-varying coordinate is still the newly inserted petal (6.1), and a
second nontrivial star permutation must remove it.

Thus a serial conveyor needs genuinely new structure, for example:

1. a row-dependent exterior which stores the transported petal in a role
   never removed again;
2. a port family with at least two row-varying coordinates, so successive
   routers can alternate active petals; or
3. a larger packet which realizes the full finite-order norm before
   returning to a star boundary.

## 7. Exact proved boundary

\[
\boxed{
\begin{gathered}
\text{Two oppositely oriented common-core \(C_6\)'s give a smallest
literal star-to-star router;}\\
\text{its two settings are equal-length geodesic, have twists
\(\tau,\tau^{-1}\), and have identical full \(X/Y\) collars;}\\
\text{direct repetition is forbidden by the newly-inserted-petal
geodesicity invariant.}
\end{gathered}}                                         \tag{7.1}
\]

The remaining constant-one gate is therefore not local ownership or local
metric feasibility.  It is a multi-petal or row-dependent-exterior serial
conveyor theorem.
