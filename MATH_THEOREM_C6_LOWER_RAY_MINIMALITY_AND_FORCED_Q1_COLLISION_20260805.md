# Exact lower-ray cost of the coatom \(C_6\): three rails are necessary, and the canonical cubic forces three \(q1\) collisions

**Date:** 2026-08-05

**Method:** literal suffix-chain counters and the canonical mixed-screen flag identity; no computation

**Status:** unconditional obstruction for the bare common-prefix coatom
\(C_6\), and an exact classification of the active-triangle cancellation in
the canonical mixed-screen packet class. This does not rule out a
noncanonical cubic packet with different state geometry.

## 0. Outcome

There are two different meanings of “decorate the coatom triangle”.

1. Adding auxiliary chains to the bare functional \(C_6\) cannot make it
   one-copy. At every proper depth the rotated phase contains three copies
   of one common suffix target. Any additive counter-balancing decoration
   leaves that target with multiplicity at least three in both phases. At
   least three auxiliary chain substitutions are needed even to balance the
   unlabelled counter. Thus one shared chain, or two, is impossible.

2. Replacing the bare geometry by canonical mixed-screen birails does give
   an all-depth phase-transparent cubic. Three owner-disjoint packet slots
   are necessary and sufficient for counter cancellation. However, for the
   natural active-label triangle

   \[
                         x\to y\to z\to x,
   \]

   cancellation at depth two already forces the three packets to have the
   same complete internal flag base. Consequently the three exceptional
   \(q1\) socket colours each occur twice.

Hence the shortest canonical exact-\(B\) candidate has a precise residual
obstruction:

\[
 \boxed{
   \text{all depths }q\ge2\text{ cancel exactly, but the zero-spare }q1
   \text{ row has three forced collisions.}
 }
\]

On a host whose remaining resources are exact, appending the three missing
\(q1\) masks gives a conditional \(B+3\) repair. Exact \(B\) requires a
noncanonical cubic (or higher) packet, a pivot/noncoatom interface, or a
different global use of the three collided sockets.

## 1. The bare common-prefix triangle

Let \(P_1,\ldots,P_{d-1}\) be an ordered list of nonempty literal blocks
and put

\[
                         R=P_1\cup\cdots\cup P_{d-1}.
\]

No disjointness among the \(P_i\)'s is required. Let \(D\) be disjoint from
\(R\), and let \(a,b,c\) be three fresh coordinates. Put

\[
                         C=R\mathbin{\dot\cup}D.
\]

For \(0\le q\le d-1\), define the terminal suffix flag

\[
 F_0=\varnothing,
 \qquad
 F_q=P_{d-q}\cup P_{d-q+1}\cup\cdots\cup P_{d-1}.   \tag{1.1}
\]

For \(u\in\{a,b,c\}\), the common-prefix head state and its rotated tail
state are

\[
 H_u=(P_1,\ldots,P_{d-1},D+u),
 \qquad
 T_u=(D+u,P_1,\ldots,P_{d-1}).                     \tag{1.2}
\]

The top payload of both states is the same named coatom

\[
                         U_u=C+u.                    \tag{1.3}
\]

For an ordered state \(A=(A_1,\ldots,A_d)\), write

\[
 \sigma_q(A)=A_{d-q+1}\cup\cdots\cup A_d
 \qquad(1\le q\le d)                               \tag{1.4}
\]

for its depth-\(q\) suffix target.

### Lemma 1.1 (exact bare-\(C_6\) lower current)

For \(1\le q<d\),

\[
 \sigma_q(H_u)=D+u+F_{q-1},
 \qquad
 \sigma_q(T_u)=F_q,                                \tag{1.5}
\]

while

\[
                         \sigma_d(H_u)=\sigma_d(T_u)=C+u.
                                                               \tag{1.6}
\]

Consequently, with tail-minus-head orientation, the three-role lower
counter current is

\[
 \boxed{
 \Delta_q^{\rm bare}
   =3{\bf e}_{F_q}
      -\sum_{u\in\{a,b,c\}}{\bf e}_{D+u+F_{q-1}}
 }
 \qquad(1\le q<d),                                  \tag{1.7}
\]

and

\[
                         \Delta_d^{\rm bare}=0.       \tag{1.8}
\]

The positive and negative masses in (1.7) are both exactly three.

#### Proof

Equations (1.5)--(1.6) follow by reading the last \(q\) blocks of
(1.2). The three sets \(D+u+F_{q-1}\) are distinct because their
intersections with \(\{a,b,c\}\) are different. None equals \(F_q\),
because it contains one of \(a,b,c\), while \(F_q\) contains none. Summing
the three state currents proves (1.7) and the mass assertion. \(\square\)

## 2. No additive one-chain repair

An **auxiliary chain substitution** is a pair of nested chains

\[
 (A_1\subseteq\cdots\subseteq A_d)
   \longrightarrow
 (B_1\subseteq\cdots\subseteq B_d),                \tag{2.1}
\]

which contributes

\[
                         {\bf e}_{B_q}-{\bf e}_{A_q} \tag{2.2}
\]

to the depth-\(q\) counter. This abstracts any added role which supplies
one old and one new target at every depth. No owner, residence, or topology
assumption is needed for the obstruction below.

### Theorem 2.1 (three-chain lower bound and persistent collision)

Suppose \(t\) auxiliary chain substitutions are added to the two bare
phases and make their lower multiplicity counters equal at every depth.
Then:

1. \(t\ge3\);
2. at every \(1\le q<d\), the old auxiliary phase contains at least three
   occurrences of \(F_q\), after orienting the bare move as in (1.7); and
3. the complete decorated phase counter contains \(F_q\) with multiplicity
   at least three in both phases.

If \(t=3\), then, at every proper depth,

\[
 \{\!\{A_q^{(1)},A_q^{(2)},A_q^{(3)}\}\!\}
       =\{\!\{F_q,F_q,F_q\}\!\},                   \tag{2.3}
\]

and

\[
 \{\!\{B_q^{(1)},B_q^{(2)},B_q^{(3)}\}\!\}
       =
 \{\!\{D+a+F_{q-1},D+b+F_{q-1},D+c+F_{q-1}\}\!\}. \tag{2.4}
\]

Thus one shared chain and two shared chains are impossible, while the
minimum counter repair still has a triple target collision.

#### Proof

Counter equality requires

\[
 \sum_{j=1}^t({\bf e}_{B_q^{(j)}}-{\bf e}_{A_q^{(j)}})
                         =-\Delta_q^{\rm bare}.       \tag{2.5}
\]

The coefficient of \(F_q\) on the right is \(-3\). Each summand on the
left contributes at least \(-1\) to that coefficient, so \(t\ge3\), and
at least three of the old auxiliary targets \(A_q^{(j)}\) equal \(F_q\).

The new bare phase already contains three occurrences of \(F_q\). The old
decorated phase contains at least the three auxiliary occurrences just
identified. Since the two decorated counters are equal, both phases have
multiplicity at least three at \(F_q\).

When \(t=3\), every summand must contribute \(-1\) at \(F_q\). No
old--new cancellation remains available. The three positive coefficients
on the right side of (2.5) are the three distinct head targets in (2.4),
so the new auxiliary multiset is forced as well. \(\square\)

### Corollary 2.2 (additive decoration cannot produce an exact one-copy face)

No collection of merely added chain roles can turn the bare common-prefix
\(C_6\) into a one-copy lower factor. A successful exact-\(B\) packet must
change the literal state geometry of the three roles, or must exploit
external slack at every collided depth.

#### Proof

A one-copy lower factor has multiplicity at most one at every named target.
Theorem 2.1 forces multiplicity at least three at \(F_q\) for every proper
depth. \(\square\)

This is stronger than saying that the two phases have different supports:
even a counter-perfect additive repair preserves the collision.

## 3. The canonical birail replacement

The mixed-screen packet changes the geometry rather than adding inverse
copies of the bare chains. For packet \(i\), let its two depth-\(q\) bases
be

\[
                         B^P_{i,q},\qquad B^S_{i,q}, \tag{3.1}
\]

and let its ordered active pair be \(x_i\to x_{i+1}\), with indices modulo
three. All active labels are assumed absent from every base. The exact
canonical lower current is

\[
\begin{aligned}
 \Delta_{i,q}={}&
   {\bf e}_{B^P_{i,q}+x_i}
  -{\bf e}_{B^P_{i,q}+x_{i+1}}\\
 &+{\bf e}_{B^S_{i,q}+x_{i+1}}
  -{\bf e}_{B^S_{i,q}+x_i},
                         &&2\le q\le d,             \tag{3.2}\\
 \Delta_{i,1}={}&0.                                  \tag{3.3}
\end{aligned}
\]

This is a pair of opposite nested-rail currents. If all three packets use
common bases at every depth, then

\[
                         \Delta_{0,q}+\Delta_{1,q}
                                  +\Delta_{2,q}=0     \tag{3.4}
\]

coefficientwise for every \(q\le d\).

The standard private-extreme realization makes the three complete owner
banks disjoint. The sharp two-packet obstruction for canonical packets
says that an inverse pair has the same central upper-screen owner; hence it
cannot occupy two slots of a simple carrier. Therefore three packet slots
are both necessary and sufficient for a nontrivial owner-disjoint
canonical counter absorber.

The next theorem shows that the common bases in this familiar construction
are not a dispensable convenience.

## 4. Cancellation forces the common flag and the \(q1\) collision

Let the internal filler list of packet \(i\) be

\[
                         G_i=(g_{i,1},\ldots,g_{i,d}),
\]

and write

\[
                         J_i=K_i\cup\{\mathord\infty,c\}.
\]

At depth two the canonical bases are

\[
\begin{aligned}
 B^P_{i,2}&=J_i\cup(G_i-\{g_{i,d}\}),\\
 B^S_{i,2}&=J_i\cup(G_i-\{g_{i,1}\}).              \tag{4.1}
\end{aligned}
\]

Assume the four signed targets of each packet are distinct, equivalently

\[
                         B^P_{i,2}\ne B^S_{i,2}.     \tag{4.2}
\]

The two exceptional \(q1\) socket colours of packet \(i\) are

\[
 Q_i+x_i,\qquad Q_i+x_{i+1},
 \qquad
 Q_i:=J_i\cup G_i.                                  \tag{4.3}
\]

### Theorem 4.1 (active-triangle flag rigidity)

Suppose the three active-triangle packets satisfy

\[
                         \Delta_{0,2}+\Delta_{1,2}
                                  +\Delta_{2,2}=0.    \tag{4.4}
\]

Then

\[
 B^P_{0,2}=B^P_{1,2}=B^P_{2,2},
 \qquad
 B^S_{0,2}=B^S_{1,2}=B^S_{2,2},                    \tag{4.5}
\]

and consequently

\[
                         Q_0=Q_1=Q_2=:Q.             \tag{4.6}
\]

Thus the combined \(q1\) bank contains the three distinct colours

\[
                         Q+x_0,\quad Q+x_1,\quad Q+x_2
                                                               \tag{4.7}
\]

with multiplicity exactly two each among the six exceptional sockets.

#### Proof

Every target in (3.2) meets the active-label set
\(\{x_0,x_1,x_2\}\) in exactly its displayed active label. Hence (4.4)
may be separated by active label.

For \(x_i\), the two positive and two negative terms give the multiset
identity

\[
 \{\!\{B^P_{i,2},B^S_{i-1,2}\}\!\}
   =
 \{\!\{B^S_{i,2},B^P_{i-1,2}\}\!\}.                \tag{4.8}
\]

There are only two matchings between the two members. The matching

\[
 B^P_{i,2}=B^S_{i,2},
 \qquad
 B^S_{i-1,2}=B^P_{i-1,2}
\]

is excluded by (4.2). Therefore

\[
 B^P_{i,2}=B^P_{i-1,2},
 \qquad
 B^S_{i,2}=B^S_{i-1,2}.                             \tag{4.9}
\]

Cycling \(i\) proves (4.5).

Since \(d\ge2\), the first and last filler labels are distinct, and (4.1)
gives

\[
                         Q_i=B^P_{i,2}\cup B^S_{i,2}.
\]

This proves (4.6). Finally, active label \(x_i\) is one endpoint of packet
\(i\) and the other endpoint of packet \(i-1\). Formula (4.3) therefore
places \(Q+x_i\) in exactly those two exceptional socket positions. The
three colours are distinct because the \(x_i\)'s are. \(\square\)

### Corollary 4.2 (all-depth transparency cannot remove the collision)

Any canonical active-triangle packet family which is transparent at every
depth \(q\le d\) satisfies the conclusion of Theorem 4.1. In particular,
varying the three cores or filler orders cannot make this cubic both
counter-transparent and \(q1\)-injective.

#### Proof

All-depth transparency includes (4.4). \(\square\)

This corollary is deliberately scoped to the active-label triangle
\((x_0,x_1),(x_1,x_2),(x_2,x_0)\) with one canonical birail current per
slot. It does not classify filler-axis triangles, arbitrary noncanonical
coatom packets, or higher-degree compounds.

## 5. Exact sidecar consequence on the zero-spare \(q1\) face

Suppose the global \(q1\) row has \(N\) physical occurrences for \(N\)
required named colours, and all occurrences outside the three packet banks
are distinct and avoid (4.7). The three doubled colours consume six
occurrences but represent only three values. Therefore the complete row
has at most

\[
                         N-3                            \tag{5.1}
\]

distinct values, and at least three required \(q1\) colours are missing.

If there are no other defects, the deficiency is exactly three. Appending
the three missing masks as literal source letters is always a valid
terminal repair, so the packet contributes a constant lower-side charge
of at most three positions.

This is a conditional \(B+3\) interface, not an unconditional universal
word theorem: one still needs a host containing the three prepared slots,
the upper/residence guards, and a background compiler which is exact away
from these sockets.

## 6. Why the \(d=2,3\) filler-axis escape does not extend with fixed channels

There is a second cubic pattern in the small depths. Keep one active pair
fixed and vary three filler words. At each depth, cancel the prefix flag of
one word against the suffix flag of the preceding word. The examples

\[
 (x,y),\ (y,z),\ (z,x)
\]

at \(d=2\), and

\[
 (x,m,y),\ (y,m,z),\ (z,m,x)
\]

at \(d=3\), have distinct complete filler sets and therefore avoid the
active-triangle socket collision.

The following elementary result explains exactly why the same fixed-channel
pattern stops there.

### Theorem 6.1 (fixed-channel filler triangle has depth at most three)

For \(i\in\mathbb Z_3\), let

\[
                         w_i=(g_{i,1},\ldots,g_{i,d})
                                                               \tag{6.1}
\]

be a word with pairwise distinct entries. Suppose that for every
\(1\le t<d\),

\[
 \{g_{i,1},\ldots,g_{i,t}\}
   =
 \{g_{i-1,d-t+1},\ldots,g_{i-1,d}\}.                \tag{6.2}
\]

Then \(d\le3\).

#### Proof

Taking the difference of (6.2) at lengths \(t\) and \(t-1\) gives

\[
                         g_{i,t}=g_{i-1,d-t+1}
 \qquad(1\le t<d).                                  \tag{6.3}
\]

For \(2\le t\le d-1\), the reflected position \(d-t+1\) also lies between
2 and \(d-1\). Applying (6.3) once more gives

\[
                         g_{i,t}=g_{i-2,t}.          \tag{6.4}
\]

Cycling \(i\) shows that all three words have a common entry \(m_t\) at
each internal position \(t\). Equation (6.3) then says

\[
                         m_t=m_{d-t+1}
 \qquad(2\le t\le d-1).                             \tag{6.5}
\]

If \(d\ge4\), positions \(2\) and \(d-1\) are distinct, yet (6.5) assigns
them the same entry. This contradicts the distinctness of the entries of
each word. Hence \(d\le3\). \(\square\)

### Corollary 6.2 (a uniform filler-axis cubic must braid with depth)

For \(d\ge4\), three distinct-label canonical filler flags cannot cancel by
one fixed cyclic prefix-to-suffix pairing at all depths. Any filler-axis
cubic escaping Theorem 4.1 must change its cancellation matching with
depth, change cores in a way that creates genuine cross-flag containments,
or leave the canonical packet class.

This theorem does not rule out such a depth-braided or arbitrary-core
cubic. It isolates the additional structure that one would have to build.

## 7. Sharp remaining alternatives

The results above eliminate the shortest naive exact-\(B\) routes.

* A bare \(C_6\) plus one shared lower chain cannot work.
* A bare \(C_6\) plus any number of merely added inverse chains remains
  non-one-copy.
* One or two owner-disjoint canonical birail packets cannot close the
  counter.
* Three active-triangle canonical packets close every lower counter, but
  force three \(q1\) collisions.

Therefore a zero-sidecar cubic fusion must leave this face in at least one
way:

1. use a noncanonical state replacement whose proper suffix chains do not
   contain the common-ray triple;
2. use a filler-axis or other structurally different \(C_6\) in which the
   cancellation graph does not reuse the same \(q1\) flag vertices;
3. use a higher-degree compound packet; or
4. use a pivot/noncoatom interface which pays and reabsorbs the socket
   collisions elsewhere.

The exact local target is consequently narrower than “find a cubic”:

\[
 \boxed{
  \text{find a literal owner-preserving cubic whose lower-current cycle is
  vertex-simple at }q1.
 }
\]

The canonical active triangle fails this condition by Theorem 4.1.
