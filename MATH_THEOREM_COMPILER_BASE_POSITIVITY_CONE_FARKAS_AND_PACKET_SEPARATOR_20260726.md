# Positivity at the diverse-compiler base: exact Farkas alternative, feasible reversal directions, and the packet separator

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Fix the explicit diverse-order compiler factor \(z\) on its retained
owner set.  It has

\[
 G=W-o(W/H),\qquad c(z)=M={G\over2R}=o(W/H),                  \tag{0.1}
\]

and every packet has a literal injective trace map through depth \(H\).

The one-sided set

\[
 \mathcal C_z=\{\delta\in K_H:\delta^-\le z\}                \tag{0.2}
\]

is not literally a cone: the coefficient-one bound truncates its negative
coordinates.  Its tangent cone has an exact Gordan--Farkas description.
After eliminating the root equations, every direction is a nonnegative
combination of rootwise column replacements, and a nonzero fractional
direction exists if and only if the origin lies in the convex hull of
their memory/trace difference vectors.  Dually, it fails to exist exactly
when one state-and-target potential makes the selected compiler column
strictly cheaper than every alternative in every root fibre.

The tangent cone is certainly nonzero.  Reversing any collection of
compiler cycles gives a genuine integral member of \(\mathcal C_z\), and
reversing all cycles changes \(\Theta(W)\) directed successor edges while
preserving every literal trace.  These directions are inert: their
undirected edge set and their component count are unchanged.

There is an exact packet-level separator explaining this inertness.  In
one physical split-pair packet, the lower depth-one target determines the
undirected Johnson edge.  Hence on packet-supported directions the
undirected edge projection factors through \(S_1^-\).  Therefore

\[
 \boxed{\delta\in K_H\text{ and packet-supported}
        \quad\Longrightarrow\quad QP\delta=0,}                \tag{0.3}
\]

where \(P\) is the directed first-edge projection and \(Q\) forgets
orientation.  The same holds for any union of sibling fibres in one
parent product cell.  Thus no packet-local or sibling-local feasible
kernel move can be productive; every productive move must exchange
literal flags between different parent product cells.

Globally, the depth-one image of every productive feasible move is an
alternating circulation in the bipartite graph

\[
 \binom{[2m]}{m-1}\longleftrightarrow\binom{[2m]}{m+1},        \tag{0.4}
\]

whose edge \((L,U)\) is the Johnson edge with meet \(L\) and join \(U\).
The negative alternating edges must belong to \(z\).  The higher-depth
equations are precisely the additional requirement that this alternating
circulation lift through the full \(H\)-memory replacement matrix.

There is a stronger global row-space separator.  Root and memory balance
together with the two signed depth-one ledgers determine the complete
coordinate-direction-pair histogram.  Since the compiler uses only
internal macroblock axes, a feasible positive move cannot create a
cross-macroblock direction.  Thus the apparent Eulerian macroblock-cycle
escape is excluded at every length; only reassignment of occurrences of
the same old internal axes remains possible.

Finally, if ``favorable monodromy'' means positive joining rank on this
base, there is a complete obstruction independent of Farkas duality:

\[
 r_{\rm join}(z,\delta)\le c(z)-1=o(W/H)=o(W/\sqrt m).       \tag{0.5}
\]

The compiler already has too few cycles to support the
\(\Theta(W/\sqrt m)\) joining rank sought in the product-SCD fusion lane.
It can instead serve as a base on which an extensive move must preserve,
not create, the few-cycle property.

Accordingly, the signed kernel **does** become actual factor moves at
linear scale, but the currently certified ones are cycle reversals.  The
remaining positive non-gauge question is a cross-parent integer
alternating-cycle lift which merely reassigns the old internal physical
axes and has controlled final cycle count.  No separator for that
internal-axis reassignment and no such positive lift is proved here.

## 1. Eliminate the root equations

Let \(\Gamma_H(X)\) be the safe columns rooted at owner \(X\).  The base
factor selects one column \(\gamma_X\in\Gamma_H(X)\).  Write

\[
 T_0=M\oplus\bigoplus_{q\le H}(S_q^-\oplus S_q^+).             \tag{1.1}
\]

The deletion rows can be omitted because

\[
                         D=B_mA-B_{m-1}S_1^-.                  \tag{1.2}
\]

For every alternative \(\gamma\in\Gamma_H(X)\setminus\{\gamma_X\}\),
define the root-balanced replacement vector

\[
                         r_\gamma=e_\gamma-e_{\gamma_X}.       \tag{1.3}
\]

Let \(R_z\) be the matrix with columns \(r_\gamma\), and put

\[
                         K_z=T_0R_z.                            \tag{1.4}
\]

### Theorem 1.1 (exact tangent-cone normal form)

An integer or real vector \(\delta\) satisfies

\[
 A\delta=0,qquad
 \delta_\gamma\ge0\quad(\gamma\notin\operatorname{supp}z)     \tag{1.5}
\]

if and only if there is a unique vector \(u\ge0\), indexed by the
alternative columns, such that

\[
                         \delta=R_zu.                           \tag{1.6}
\]

Moreover,

\[
 \delta\in K_H\quad\Longleftrightarrow\quad K_zu=0.           \tag{1.7}
\]

The coefficient-one bound \(\delta^-\le z\) is exactly

\[
 \sum_{\gamma\in\Gamma_H(X)\setminus\{\gamma_X\}}u_\gamma
                              \le1\qquad\text{for every }X.    \tag{1.8}
\]

If \(u\) is integral, every sum in (1.8) is zero or one, so it replaces
the old column at each changed root by exactly one new column.

#### Proof

Outside the selected support set \(u_\gamma=\delta_\gamma\ge0\) is
forced.  The root equation in fibre \(X\) then forces

\[
 \delta_{\gamma_X}=-
 \sum_{\gamma\in\Gamma_H(X)\setminus\{\gamma_X\}}u_\gamma,
\]

which proves existence and uniqueness in (1.6).  Applying \(T_0\) gives
(1.7), because root balance is already built into \(R_z\).  The displayed
formula for \(\delta_{\gamma_X}\) also proves (1.8). \(\square\)

Thus the fractional tangent cone and the actual coefficient-one fibre are

\[
 \widehat{\mathcal C}_z
   =\{R_zu:u\ge0, K_zu=0\},                                    \tag{1.9}
\]

\[
 \mathcal C_z
   =\{R_zu:u\in\mathbb Z_{\ge0}, K_zu=0,
              \text{and (1.8) holds}\}.                       \tag{1.10}
\]

The distinction matters.  A nonzero rational vector in (1.9) can be
scaled down to obey (1.8), but clearing denominators scales the negative
root coefficients above one.  Fractional feasibility therefore does not
imply an integral factor move.

## 2. Exact Farkas dual

### Theorem 2.1 (strict-separation alternative)

Exactly one of the following holds.

1. There is a nonzero \(u\ge0\) with \(K_zu=0\).
2. There is a row vector \(y\) such that
   \[
                              K_z^Ty>0                           \tag{2.1}
   \]
   coordinatewise on every alternative column.

#### Proof

This is Gordan's theorem of the alternative applied to \(K_z\). \(\square\)

Write \(y\) as a potential \(f\) on memory states and potentials
\(h_{q,T}^\pm\) on literal targets.  Define the column score

\[
 \Phi_y(\gamma)=
 f(\operatorname{suf}\gamma)-f(\operatorname{pre}\gamma)
 +\sum_{q\le H}\big(h_{q,L_q(\gamma)}^-
                       +h_{q,U_q(\gamma)}^+\big).               \tag{2.2}
\]

Then (2.1) says exactly

\[
 \boxed{
 \Phi_y(\gamma)>\Phi_y(\gamma_X)
 \quad\text{for every }X
 \text{ and every }\gamma\ne\gamma_X\text{ rooted at }X.}    \tag{2.3}
\]

So a separating dual certificate is a single state-and-target cost for
which the compiler's selected history is the strict unique minimizer in
every root fibre.  Root potentials need not be included because they
cancel in (1.3).

There is an equally useful optimization form.  For any linear score
\(c\) on replacement columns,

\[
 \max\{c^Tu:K_zu=0, u\ge0, \mathbf1^Tu=1\}
 =\min_y\max_\gamma\big(c_\gamma-(K_z^Ty)_\gamma\big).         \tag{2.4}
\]

This can test any **linear** immediate-edge objective.  Component count
and favorable monodromy are not linear scores, so they require the
additional topology retained in Section 5.

Because the reversal directions of Section 3 exist, the global strict
separator (2.3) cannot exist for the full cone.  To separate productive
directions one must quotient by orientation, or equivalently test the
undirected projection \(QPR_z\).

### Corollary 2.2 (exact conic dual for productive edge movement)

Let \(q_e^T\) be one coordinate row of \(QPR_z\), indexed by an
undirected Johnson edge \(e\).  Then

\[
 q_e^Tu=0\quad\text{for every }u\ge0\text{ with }K_zu=0        \tag{2.5}
\]

if and only if there are dual vectors \(y_e^+,y_e^-\) such that

\[
 K_z^Ty_e^+\ge q_e,
 \qquad
 K_z^Ty_e^-\ge-q_e.                                            \tag{2.6}
\]

Consequently the entire fractional positive cone has zero undirected
edge image if and only if (2.6) holds for every \(e\).

#### Proof

The implication from (2.6) follows by pairing either inequality with
\(u\ge0\) and using \(K_zu=0\).  Conversely, the conic Farkas lemma says
that \(q_e^Tu\le0\) on \(\{u\ge0:K_zu=0\}\) exactly when some
\(K_z^Ty\ge q_e\); apply it also to \(-q_e\). \(\square\)

The packet identity (4.3) below supplies (2.6) with equality on every
packet-local catalogue.  Globally, cross-parent columns are exactly the
columns on which this dual certificate is currently missing.

## 3. Extensive feasible directions exist, but reversal is inert

Let \(C=(X_0,X_1,\ldots,X_{\ell-1})\) be one oriented compiler cycle.
Reverse it to

\[
                         \bar C=(X_0,X_{\ell-1},\ldots,X_1).    \tag{3.1}
\]

### Theorem 3.1 (cycle-reversal cube)

For every subfamily \(\mathcal S\) of compiler cycles, independently
reverse precisely the cycles in \(\mathcal S\).  The resulting circulation
\(z_{\mathcal S}\) is a coefficient-one \(H\)-safe factor and

\[
                         z_{\mathcal S}-z\in\mathcal C_z.       \tag{3.2}
\]

All these factors have the same undirected edge set and the same number of
components.  Reversing every cycle changes \(2G\) directed edge
coordinates, for all sufficiently large compiler cycles.

#### Proof

Reversal preserves every owner and every undirected edge.  A reversed
q-window visits the same \(q+1\) owners in reverse order, so its meet and
join are unchanged.  Cyclic reversal bijects all windows and hence
preserves every literal trace multiset.  Safety is also invariant under
reversal.  On one cycle, the number of deletions of a coordinate equals
the number of insertions of that coordinate, so the run vector is
unchanged.  This proves (3.2).  Reversal neither joins nor splits the
underlying cycle.  Finally, a simple cycle of length greater than two has
disjoint forward and reverse oriented arc sets, giving two changed
directed coordinates per owner. \(\square\)

Thus the positive cone has at least a \(2^{M}\)-point integral cube and an
extensive immediate **directed** edge image.  This is not the non-gauge
direction needed for topology: after forgetting orientation its image is
zero.

## 4. Packet-local Farkas certificate

Let \(E(P)\) be the undirected Johnson edges inside one physical
split-pair packet \(P\cong Q_R\).  Put

\[
 \ell:E(P)\longrightarrow\binom{[2m]}{m-1},qquad
                         \ell(XY)=X\cap Y.                     \tag{4.1}
\]

The packet lower-shadow injectivity theorem says that \(\ell\) is
injective.  Let \(J_P\) be the inverse linear map from its image targets
to edge coordinates.

### Theorem 4.1 (packet-supported productive directions are separated)

Suppose \(\delta\in K_H\) and every immediate old and new edge in
\(P\delta\) lies in one packet \(P\).  Then

\[
                         QP\delta=0,                             \tag{4.2}
\]

where \(Q\) forgets edge orientation.  More precisely, on this restricted
column catalogue,

\[
                         QP=J_PS_1^-.                           \tag{4.3}
\]

The same conclusion holds for a union of parallel sibling fibres in one
parent product cell, provided every new edge remains in its own sibling
fibre.

#### Proof

For a first transition \(X\to Y\), \(S_1^-\) records exactly
\(X\cap Y=\ell(XY)\).  Injectivity of \(\ell\) gives (4.3).  Since
\(S_1^-\delta=0\), equation (4.2) follows.

Distinct sibling fibres have disjoint literal lower-target images because
some frozen spectator pair records opposite endpoints.  Therefore the
same inverse can be applied blockwise to their disjoint images. \(\square\)

Equation (4.3) is an explicit row-space dual certificate, stronger than a
mere dimension count: every packet-local undirected edge coordinate is a
linear combination of lower-target rows.  Hence it vanishes on the exact
kernel.  A productive move must use cross-packet edges, and sibling
separation pushes it further to different parent product cells.

## 5. The global productive image is an alternating flag circulation

Form the bipartite graph \(\mathcal B_1\) with left vertices the
\((m-1)\)-sets and right vertices the \((m+1)\)-sets.  Each undirected
Johnson edge \(XY\) gives the edge

\[
               (L,U)=(X\cap Y,X\cup Y),qquad L\subset U.      \tag{5.1}
\]

This is a bijection: if \(U\setminus L=\{a,b\}\), the corresponding
Johnson edge is \(L+a\)--\(L+b\).

### Theorem 5.1 (depth-one alternating-cycle normal form)

For every \(\delta\in K_H\), the undirected immediate-edge derivative

\[
                         \eta=QP\delta                          \tag{5.2}
\]

has zero degree at every vertex of \(\mathcal B_1\).  Hence \(\eta\)
decomposes over \(\mathbb Z\) into signed alternating even cycles of
\(\mathcal B_1\).  If \(\delta\in\mathcal C_z\), every negative edge in
this decomposition belongs to the compiler base.

Conversely, the depth-one equations on an undirected edge derivative are
exactly this zero-degree condition.  Such a circulation comes from an
element of \(\mathcal C_z\) only if it also admits a root-compatible,
sign-compatible lift through

\[
                         K_zu=0                                  \tag{5.3}
\]

and the bounds (1.8).

#### Proof

The left degree vector of \(\eta\) is \(S_1^-\delta\), and its right
degree vector is \(S_1^+\delta\).  Both vanish.  The integer cycle lattice
of a bipartite graph is generated by its alternating even cycles.  The
sign statement follows from \(\delta^-\le z\).  The converse at depth one
is the same incidence calculation; the final warning is precisely the
higher-memory system of Theorem 1.1. \(\square\)

There is no nontrivial two-old-edge factor switch preserving both signed
depth-one traces; the first useful circuit is the six-edge octahedral
cycle.  Thus every productive compiler move must locate cross-parent
alternating flag cycles and then solve their simultaneous \(H\)-memory
lift.

### Theorem 5.2 (the minimal octahedral lift is absent from the rank-twisted base)

In the rank-twisted macroblock packet factor, no three old edges form the
negative matching of an octahedral depth-one trade.  Consequently the
certified two-rail \(H\)-lift of the octahedral atom is not sign-compatible
with this base.

#### Proof

Write the six ports of an octahedral trade as \(C+xy\), with central
coordinates \(a,b,c,d\).  Its three old directions are

\[
                         \{d,a\},\quad\{d,b\},\quad\{d,c\}.    \tag{5.4}
\]

Every compiler edge is one selected split-pair axis of a rank-twisted
product cell.  Such an axis lies inside one macroblock \(B_j\) and belongs
to the perfect matching \(M_{j,k}\), where \(k\) is the local owner rank
in that block.

If all three edges in (5.4) existed, each of \(a,b,c\) would lie in the
same macroblock as \(d\).  The three owners on the \(d\)-shore are

\[
                         C+ad,quad C+bd,quad C+cd.             \tag{5.5}
\]

They have the same local rank

\[
                         k=|C\cap B_j|+2                        \tag{5.6}
\]

in that macroblock.  Therefore all three directions in (5.4) would have
to be edges of the one perfect matching \(M_{j,k}\).  This is impossible,
because they are three distinct edges incident with \(d\). \(\square\)

Equivalently, every directed link graph \(D_{C,d}\) of this base is
triangle-free.  For fixed \((C,d)\), the possible mate of \(d\) is a
function only of whether the retained coordinate \(x\) lies in the
macroblock of \(d\); on a directed link triangle all three retained
coordinates must lie in that block, where the mate is unique.

Theorem 5.2 by itself closes only the minimal six-edge circuit.  The
direction-pair row-space identity in Theorem 5.4 below excludes the
proposed longer cross-macroblock escape as well.

### Proposition 5.3 (cross-macroblock directions are Eulerian)

Let \(\eta=\eta^+-\eta^-\) be the undirected edge derivative of a
feasible kernel move, and suppose every negative edge is a compiler edge.
Make a multigraph \(\mathcal G_B^+\) on the macroblocks by sending a
positive Johnson direction \(\{a,b\}\) to the block pair
\(\{B(a),B(b)\}\), with an internal direction represented by a loop.
Then the submultigraph of cross-macroblock edges has even degree at every
macroblock.  Hence it is a union of macroblock cycles.

#### Proof

For a set \(S\), let \(r(S)=(|S\cap B_j|)_j\).  If an edge of the flag
graph is \((L,U)\), with \(U\setminus L=\{a,b\}\), put

\[
 \rho(L,U)=r(U)-r(L)=e_{B(a)}+e_{B(b)}.                         \tag{5.7}
\]

Because \(\eta\) has zero degree at every lower and every upper flag,

\[
                         \sum_e\eta_e\rho(e)=0.                \tag{5.8}
\]

Every negative compiler direction is internal to one macroblock, so its
\(\rho\)-vector is \(2e_{B_j}\).  Therefore the positive direction
multigraph has even total degree at every block.  Positive internal loops
also contribute degree two.  Removing them leaves even cross degree at
every block, proving the claim. \(\square\)

This does not itself give the memory lift, but it identifies the next
possible geometry after Theorem 5.2: a productive move must route an
Eulerian cycle through several parent macroblocks, rather than export a
single isolated axis.

### Theorem 5.4 (complete direction-pair row-space separator)

In fact the Eulerian alternative of Proposition 5.3 never occurs.  For
every unordered coordinate pair \(\{a,b\}\), the number of immediate
Johnson edges having direction pair \(\{a,b\}\) is an exact linear
consequence of the root, memory, lower-depth-one, and upper-depth-one
ledgers.  Consequently

\[
 \boxed{\delta\in K_H\quad\Longrightarrow\quad
   \text{the complete coordinate-direction-pair histogram of }P\delta
   \text{ is zero}.}                                          \tag{5.9}
\]

In particular, let \(z\) be the rank-twisted compiler base.  Every edge
of \(z\) has both direction coordinates in one macroblock.  If
\(\delta\in\mathcal C_z\), then every positive immediate edge of
\(\delta\) also has both direction coordinates in one macroblock.  More
sharply, for each physical compiler axis \(\{a,b\}\), its positive and
negative multiplicities in \(P\delta\) are equal.  Thus no alternating
flag circuit of any length can create a cross-macroblock direction.

#### Proof

For a set \(S\), put

\[
                         f_{ab}(S)={\bf1}_{\{a,b\}\subseteq S}.
                                                               \tag{5.10}
\]

Let the first Johnson edge of a safe history be \(X\)--\(Y\), and put
\(L=X\cap Y\), \(U=X\cup Y\).  Then the following columnwise identity
is exact:

\[
 {\bf1}_{U\setminus L=\{a,b\}}
   =f_{ab}(L)+f_{ab}(U)-f_{ab}(X)-f_{ab}(Y).                  \tag{5.11}
\]

Indeed, if \(a,b\) are the two direction coordinates, only \(U\)
contains both.  If both already lie in \(L\), all four terms contain
them and cancel.  If exactly one is a direction coordinate and the other
lies in \(L\), then \(U\) and exactly one of \(X,Y\) contain both and
cancel.  In every remaining case all terms are zero.

The \(X\)-ledger is the root row \(A\).  The \(Y\)-ledger is also in the
row span of \(A\oplus M\): project a prefix memory state to its first
owner.  Applied to the de Bruijn boundary of
\((X_0,\ldots,X_H)\), this gives \(e_{X_1}-e_{X_0}\).  Hence the head
incidence row equals the root incidence row plus a row combination of
\(M\).  Finally, the \(L\)- and \(U\)-ledgers are exactly
\(S_1^-\) and \(S_1^+\).  Equation (5.11) therefore places every
direction-pair row in

\[
          \operatorname{row}(A\oplus M\oplus S_1^-\oplus S_1^+).
                                                               \tag{5.12}
\]

It vanishes on \(K_H\), proving (5.9).

For the positivity statement, a cross-macroblock pair occurs zero times
in \(z\).  The inequality \(\delta^-\le z\) therefore gives it no
negative occurrence in \(P\delta\).  Its signed count is zero by (5.9),
so it has no positive occurrence either.  The same argument pair by pair
gives equality of positive and negative multiplicities on every internal
axis. \(\square\)

There is a useful quadratic shorthand for (5.11).  If
\(r(S)=(|S\cap B_j|)_j\), then

\[
 \|r(L)\|_2^2+\|r(U)\|_2^2-\|r(X)\|_2^2-\|r(Y)\|_2^2
 =2\,{\bf1}_{\text{the direction pair lies in one macroblock}}.
                                                               \tag{5.13}
\]

This already preserves the total number of internal directions.  The
coordinatewise polarization (5.11) is stronger: it preserves the exact
physical axis histogram.  Proposition 5.3 is therefore a necessary
first-moment consequence whose putative nontrivial Eulerian part is
annihilated by the quadratic/coordinate-pair rows.

## 6. Few-cycle topology is already a separator for positive joining

### Theorem 6.1 (joining ceiling at the compiler base)

For every feasible \(\delta\in\mathcal C_z\) such that \(z+\delta\) is a
factor,

\[
 r_{\rm join}(z,\delta)
 :=c(z)-c(z+\delta)
 \le c(z)-1
 ={G\over2R}-1=o(W/H).                            \tag{6.1}
\]

In particular, when \(H/\sqrt m\to\infty\),

\[
                         r_{\rm join}(z,\delta)=o(W/\sqrt m).   \tag{6.2}
\]

#### Proof

Every nonempty factor has at least one component.  Use (0.1). \(\square\)

Thus this base cannot be used to realize the extensive positive joining
rank demanded when starting from the product-SCD path cover.  That is not
a defect of the compiler: its component gate is already solved.  A useful
extensive non-gauge move on this base should instead satisfy

\[
                         c(z+\delta)=o(W/H),                    \tag{6.3}
\]

while changing cross-parent target pairing or another later structure.
Condition (6.3) is nonlinear and is invisible to the Farkas system.

## 7. Exact remaining positivity theorem

The large signed kernel does intersect the coefficient-one fibre at
linear directed-edge scale, but presently only through the reversal cube.
The packet-local row-space certificate eliminates every non-gauge move
that stays inside one packet or its sibling fibres.  Therefore the exact
remaining question is:

> **Cross-parent positive kernel theorem (open).**  Find an integral
> \(u\ge0\) satisfying (1.8) and \(K_zu=0\), such that the alternating
> flag circulation \(QPR_zu\) is nonzero on \(\Theta(W)\) edges, uses
> edges from different parent product cells, preserves the occurrence
> count of every old internal physical direction pair as forced by
> Theorem 5.4, and the resulting factor has \(o(W/H)\) components.

Equivalently, exhibit a cross-parent collection of alternating flag cycles
whose negative edges lie in \(z\), whose positive edges reuse exactly the
same multiset of internal physical axes, whose rootwise replacements lift
to a zero-voltage \(H\)-memory circulation, and whose exterior
monodromies do not create a large cycle count.

A global strict separator of the form (2.3) would refute even fractional
movement.  No such separator is known.  Conversely, failure of strict
separation supplies only a fractional tangent direction; it does not
clear the coefficient-one integrality gate.  This is the precise boundary
between the enormous formal kernel and an actual productive factor move.
