# The cyclic-overlay obstruction for smallest moving-exterior \(C_6\) routers

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Result and scope

The smallest moving-exterior \(C_6\) router cannot be chained around a
directed cycle of exterior contexts by taking one complete router packet
on every directed context edge.

The obstruction is already in the lower-owner ledger. If the exterior
contexts are \(x_j\), then the outgoing triangle state of the
\((j-1)\)-st packet is literally the internal triangle state of the
\(j\)-th packet. Every such state consequently occurs twice, independently
of which shore of each \(C_6\) trade is selected.

Identifying the two occurrences does not repair the construction. The
identified lower vertex has local degree three. If one deletes the
star--triangle incidence in order to retain the directed exterior
conveyor, two consecutive exterior moves insert \(x_j\) and immediately
delete it. The resulting two-edge segment has Johnson distance one
(distance zero on a two-context cycle), so it is not geodesic.

For a simple context cycle of length at least three, the upper tokens are
all distinct; hence the failure is specifically lower ownership and
geodesicity, not a hidden upper collision. For a two-context cycle, the
second upper collars are duplicated as well.

This rules out the direct cyclic overlay of the minimal routers. It does
not rule out a compound router with fresh triangle coordinates, a
rank-changing seam, or a palette-uniform exterior module whose
intermediate lower states are genuinely different.

## 1. The common ledger of one router

Let \(\ell\ge2\). Take pairwise distinct exterior coordinates

\[
                         x_0,x_1,\ldots,x_{\ell-1},              \tag{1.1}
\]

with indices modulo \(\ell\), and distinct local coordinates

\[
                         k,a_0,a_1,a_2,                          \tag{1.2}
\]

with the \(i\)-index modulo three. Let \(B\) be a fixed background
disjoint from all displayed coordinates.

For the directed context edge \(x_j\to x_{j+1}\), define lower states

\[
\begin{aligned}
 S_j^i&=B\cup\{x_j,k,a_i\},\\
 T_j^i&=B\cup\{x_j,a_i,a_{i+1}\},\\
 T_{j+1}^i&=B\cup\{x_{j+1},a_i,a_{i+1}\},
\end{aligned}                                                   \tag{1.3}
\]

and upper tokens

\[
\begin{aligned}
 U_j^i&=B\cup\{x_j,k,a_i,a_{i+1}\},\\
 V_j^i&=B\cup\{x_j,x_{j+1},a_i,a_{i+1}\}.
\end{aligned}                                                   \tag{1.4}
\]

The old shore consists of the three paths

\[
 S_j^i-U_j^i-T_j^i-V_j^i-T_{j+1}^i,
 \qquad i\in\mathbb Z_3.                                      \tag{1.5}
\]

The alternating \(C_6\) switch replaces their first incidences and gives

\[
 S_j^{i+1}-U_j^i-T_j^i-V_j^i-T_{j+1}^i,
 \qquad i\in\mathbb Z_3.                                      \tag{1.6}
\]

Thus either shore has exactly the same literal ledger

\[
\begin{aligned}
 \mathcal X_j&=
  \{S_j^i,T_j^i,T_{j+1}^i:i\in\mathbb Z_3\},\\
 \mathcal Y_j&=
  \{U_j^i,V_j^i:i\in\mathbb Z_3\}.                             \tag{1.7}
\end{aligned}
\]

This is the smallest-router ledger after absorbing every fixed common
coordinate into \(B\). In the notation of the literal packet,
\(B=C\), \(x_j=u\), \(x_{j+1}=v\), and \(k\) is the common element of
the three star ports.

## 2. Exact lower multiplicities

### Theorem 2.1 (cyclic-overlay duplicate)

Choose either shore (1.5) or (1.6) independently for every
\(j\in\mathbb Z_\ell\), and take the multiset union of the complete
router ledgers. Then, for every \(j\) and \(i\),

\[
 \boxed{
 T_j^i
 =B\cup\{x_j,a_i,a_{i+1}\}
 }
                                                               \tag{2.1}
\]

occurs exactly twice: once as the internal state \(T_j^i\) of packet
\(j\), and once as the terminal state \(T_{(j-1)+1}^i\) of packet
\(j-1\).

All \(3\ell\) states in (2.1) are distinct, and none is an \(S\)-state.
Consequently the lower duplicate excess of the union is exactly

\[
                              3\ell.                            \tag{2.2}
\]

In particular, the complete packet union is not an exact middle-owner
factor.

#### Proof

The displayed equality is immediate from (1.3):

\[
 T_{(j-1)+1}^i
 =B\cup\{x_j,a_i,a_{i+1}\}
 =T_j^i.                                                       \tag{2.3}
\]

It is independent of the switch shore because (1.7) is shore-invariant.

Distinct \(j\)'s are separated by the coordinate \(x_j\). For fixed
\(j\), the three unordered pairs

\[
 \{a_0,a_1\},\quad\{a_1,a_2\},\quad\{a_2,a_0\}
\]

are distinct. Hence the \(T_j^i\)'s are pairwise distinct. Every
\(S_j^i\) contains \(k\), while no \(T_j^i\) contains \(k\), so the two
families are disjoint. Each \(S\)-state occurs in only its own packet,
whereas (2.3) gives exactly the two claimed occurrences of every
\(T\)-state. This proves (2.2). \(\square\)

The theorem applies to a union with any surrounding background: exact
ownership is pointwise, so additional factor rows cannot cancel a
duplicated owner.

## 3. The upper ledger

### Proposition 3.1 (upper multiplicities)

If \(\ell\ge3\) and (1.1) is a simple context cycle, all upper tokens in

\[
                         \bigcup_j\mathcal Y_j                  \tag{3.1}
\]

are pairwise distinct. If \(\ell=2\), then

\[
                         V_0^i=V_1^i
                         \qquad(i\in\mathbb Z_3),               \tag{3.2}
\]

so the three second-collar tokens are duplicated.

#### Proof

Every \(U_j^i\) contains \(k\), and no \(V_j^i\) does. Distinct \(U\)'s
are separated by \(x_j\) or by their adjacent \(a\)-pair.

A \(V_j^i\) records the unordered context edge
\(\{x_j,x_{j+1}\}\) and the adjacent pair
\(\{a_i,a_{i+1}\}\). The unordered edges of a simple cycle of length at
least three are distinct, as are the three adjacent \(a\)-pairs. Hence
all \(V\)'s are distinct in that case. For \(\ell=2\), both directed
edges have the same unordered pair \(\{x_0,x_1\}\), which gives (3.2).
\(\square\)

Thus for \(\ell\ge3\) the upper ledger offers no cancellation mechanism:
one would have to destroy an otherwise exact upper palette to repair the
lower duplication.

## 4. Identification creates degree three

One might try to regard the two copies in (2.3) as one shared physical
state rather than two owner occurrences.

### Theorem 4.1 (shared-state degree and geodesicity obstruction)

After identifying the two copies of \(T_j^i\), the union of the complete
router incidences has the three distinct incident upper tokens

\[
                         V_{j-1}^i,\qquad U_j^i,\qquad V_j^i.   \tag{4.1}
\]

Hence its local degree is three, so it is not a path factor.

If one deletes the incidence through \(U_j^i\) in order to keep the
directed exterior conveyor, the retained two-router segment is

\[
 T_{j-1}^i-V_{j-1}^i-T_j^i-V_j^i-T_{j+1}^i.                   \tag{4.2}
\]

For \(\ell\ge3\), this segment has two Johnson moves but its endpoints
have Johnson distance one. For \(\ell=2\), its endpoints are equal.
Thus (4.2) is never a geodesic.

#### Proof

As the terminal state of packet \(j-1\), \(T_j^i\) is incident with
\(V_{j-1}^i\). As the internal state of packet \(j\), it is incident with
\(U_j^i\) and \(V_j^i\). These tokens are distinct when \(\ell\ge3\) by
Proposition 3.1; for \(\ell=2\), the upper duplication is already fatal.
This proves the degree statement.

The two moves in (4.2) are

\[
                         x_{j-1}\mapsto x_j,\qquad
                         x_j\mapsto x_{j+1}.                    \tag{4.3}
\]

Thus \(x_j\) is inserted and then deleted. When \(\ell\ge3\), the
endpoints differ only by \(x_{j-1}\mapsto x_{j+1}\), so their Johnson
distance is one. When \(\ell=2\), \(x_{j-1}=x_{j+1}\), so the endpoints
coincide. In either case the length-two segment is not geodesic.
\(\square\)

Keeping \(U_j^i\) instead forces one to omit an exterior collar
\(V_{j-1}^i\) or \(V_j^i\), so it no longer uses one complete router on
every directed context edge and leaves an upper token unowned. There is
no repair within the displayed packet union.

## 5. Exact boundary

The result closes the following construction class.

* The contexts form a directed cycle.
* Every directed context edge receives one complete copy of the smallest
  moving-exterior \(C_6\) packet.
* All copies use the same local star coordinate \(k\), the same triangle
  \(\{a_0,a_1,a_2\}\), and the same fixed background.
* Either trade shore may be chosen independently.

Within this class, exact lower ownership fails by \(3\ell\), and
identifying the repeated owners destroys the degree-two path ledger or
geodesicity.

The theorem does **not** rule out:

1. using fresh local triangles on successive context edges;
2. a compound trade which simultaneously removes and replaces the
   duplicated \(T_j^i\)-states and their upper incidences;
3. staggering routers in different local-rank layers;
4. a rank-changing cross-block braid; or
5. a port-fixed palette-uniform exterior seam library not assembled as
   this direct cyclic overlay.

Therefore the natural same-triangle cyclic \(C_6\) realization of a
regular context action is impossible. The global Latin shear remains
algebraically valid, but its router atlas must use a genuinely different
physical composition.
