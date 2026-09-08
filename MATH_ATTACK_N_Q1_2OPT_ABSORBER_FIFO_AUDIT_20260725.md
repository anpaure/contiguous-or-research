# Lane N: exact audit of the shared-extra two-facet absorber

Date: 2026-07-25  
Status: proved local Hamilton absorber, proved quantitative simple-seam supply, proved exact global resource and residence gates; no critical-scale FIFO construction

## 1. Setup and exact constants

Assume \(m\ge 6\), and put

\[
n=2m+1,
\qquad
W=\binom{n}{m},
\qquad
B=\frac Wn.
\]

Let \(\Gamma_0\) be the Proposition 18A core cycle.  It has

\[
L=N_1=\binom{n}{m-1}=\frac{m}{m+2}W
\tag{1.1}
\]

middle owners and uses every rank-\((m-1)\) lower color exactly once.  Its
omitted middle family \(\mathcal E\) has

\[
d=W-L=\frac{2W}{m+2}
\tag{1.2}
\]

members.

Fix \(Z\in\mathcal E\).  For \(a\in Z\), set

\[
S_a=Z\setminus\{a\}.
\tag{1.3}
\]

The unique core edge \(e_a\) of color \(S_a\) has endpoints

\[
S_a\cup\{u_a\},\qquad S_a\cup\{v_a\}.
\]

Neither extra coordinate can be \(a\), because that endpoint would be the
omitted owner \(Z\).  Hence

\[
p_a:=\{u_a,v_a\}\subseteq Y:=Z^c,
\qquad |Y|=m+1.
\tag{1.4}
\]

For distinct \(a,b\in Z\), the core edges \(e_a,e_b\) are vertex-disjoint.
Indeed, a common endpoint would contain
\(S_a\cup S_b=Z\), and hence would equal the omitted \(m\)-set \(Z\).

The \(m\) pairs \(p_a\) form a labeled loopless multigraph on \(m+1\)
outside coordinates.  If \(d_x\) is its degree at \(x\), the number of
shared-coordinate witnesses, counted with their shared coordinate, is

\[
w_Z=\sum_{x\in Y}\binom{d_x}{2}\ge m-1.
\tag{1.5}
\]

To prove (1.5), minimize the convex sum subject to
\(\sum_xd_x=2m\).  Its minimum degree sequence is
\(2^{m-1},1^2\), giving \(m-1\).  This is the exact content of the raw
pigeonhole argument.  Orientation and residence require more.

## 2. The exact local move

Choose distinct \(a,b\in Z\) and a shared outside coordinate
\(x\in p_a\cap p_b\).  Write

\[
p_a=\{x,y\},\qquad p_b=\{x,z\},
\tag{2.1}
\]

and name the four endpoints

\[
\begin{aligned}
A&=S_a\cup\{y\},&B&=S_a\cup\{x\},\\
C&=S_b\cup\{z\},&D&=S_b\cup\{x\}.
\end{aligned}
\tag{2.2}
\]

Put

\[
T=T_{a,b,x}:=(Z\setminus\{a,b\})\cup\{x\}.
\tag{2.3}
\]

The proposed exchange is

\[
AB,CD\quad\longmapsto\quad AZ,ZC,BD.
\tag{2.4}
\]

### Theorem 2.1 (degree and color ledger)

The three new pairs in (2.4) are Johnson edges, with lower colors

\[
\operatorname{col}(AZ)=S_a,
\qquad
\operatorname{col}(ZC)=S_b,
\qquad
\operatorname{col}(BD)=T.
\tag{2.5}
\]

If \(BD\notin E(\Gamma_0)\), (2.4) is a simple spanning two-factor on
\(V(\Gamma_0)\cup\{Z\}\).  It preserves the occurrences of \(S_a,S_b\)
and adds exactly one occurrence of \(T\).

#### Proof

Direct intersection gives

\[
A\cap Z=S_a,
\qquad
Z\cap C=S_b,
\qquad
B\cap D=T.
\]

Every old endpoint loses one incident edge and gains one; \(Z\) gains two.
The edge count changes by \(-2+3=1\), exactly matching the new owner.
Simplicity fails only if the proposed chord \(BD\) is already present or
if simultaneous moves duplicate a new edge.  The color statement is the
displayed intersection calculation. \(\square\)

If \(BD\) is already the unique core edge of color \(T\), merely counting
a second copy creates a forbidden parallel edge; in the simple Johnson
graph, \(B,D\) remain degree deficient after \(AB,CD\) are deleted.  Thus
the raw unoriented move needs a genuine chord-availability check.

## 3. Orientation is not a free choice

Orient the core cycle once.  Direct \(p_a\) from \(u\) to \(v\) precisely
when \(e_a\) is traversed from \(S_a+u\) to \(S_a+v\).  Let
\(d_x^+\) and \(d_x^-\) be the numbers of arcs entering and leaving \(x\),
respectively.

### Theorem 3.1 (Hamilton sign and automatic simplicity)

A shared-\(x\) witness preserves one Hamilton cycle under (2.4) if and
only if \(x\) is the head of both marked arcs or the tail of both marked
arcs.  The exact number of Hamilton-preserving witnesses is

\[
H_Z=\sum_{x\in Y}
\left[
\binom{d_x^+}{2}+\binom{d_x^-}{2}
\right].
\tag{3.1}
\]

The number of opposite-sign witnesses is

\[
S_Z=\sum_{x\in Y}d_x^+d_x^-;
\qquad H_Z+S_Z=w_Z.
\tag{3.2}
\]

For a same-sign witness, the chord \(BD\) is automatically absent from
the core, so the move is a simple Hamilton insertion.  For an opposite-sign
witness, an available chord produces two cycles rather than one.

#### Proof

After reversing the global orientation if needed, a same-head witness has

\[
A\longrightarrow B,
\qquad
C\longrightarrow D.
\tag{3.3}
\]

The cyclic order is \(A,B,\ldots,C,D,\ldots,A\).  After (2.4), one obtains

\[
A,Z,C,\ldots,B,D,\ldots,A,
\tag{3.4}
\]

where the old \(B\)-to-\(C\) arc is traversed in reverse.  This is one
Hamilton cycle.

Moreover \(BD\) cannot be an oriented core edge.  If \(B\to D\), then
\(D\) has the two predecessors \(B,C\); if \(D\to B\), then \(B\) has the
two predecessors \(A,D\).  Both contradict the directed-cycle degrees.

If one \(x\)-endpoint is a head and the other a tail, deleting the two
marked edges leaves one old path with endpoints \(B,D\) and the other with
endpoints \(A,C\).  The links \(BD\) and \(A-Z-C\) close them separately.
The counting formulas are the two possible sign pairings at every \(x\).
\(\square\)

Thus the instruction to “orient the two edges so that \(B,D\) contain
\(x\)” is not a discretionary local orientation.  \(B,D\) are forced by
\(x\), and their head/tail signs are inherited from the single core
orientation.

### Proposition 3.2 (sharp local zero-witness classification)

For the oriented extra-pair data of any fixed core, one has

\[
H_Z=0
\quad\Longleftrightarrow\quad
d_x^+\le1\text{ and }d_x^-\le1
\quad(x\in Y).
\tag{3.5}
\]

In this case the oriented multigraph on \(Y\) is the disjoint union of
exactly one directed path component, possibly an isolated vertex, and any
number of directed cycle components.

#### Proof

Equation (3.1) proves (3.5).  A loopless directed multigraph with both
in- and out-degree at most one has path and directed-cycle components.
The number of path components, counting isolated vertices, is

\[
|Y|-|E|=(m+1)-m=1.
\]

This proves the classification. \(\square\)

Thus the pair count (1.5) alone gives no positive lower bound for
\(H_Z\).  The directed spanning path

\[
x_0\to x_1\to\cdots\to x_m
\tag{3.6}
\]

is the sharp abstract obstruction: it has \(w_Z=m-1\) but \(H_Z=0\).

There is also a literal local Johnson obstruction packet.  Enumerate
\(Z=\{a_1,\ldots,a_m\}\), \(Y=\{y_0,\ldots,y_m\}\), and place the following
owners consecutively in the core:

\[
\begin{split}
&Z-a_1+y_0, Z-a_1+y_1, Z-a_2+y_1, Z-a_2+y_2,\ldots,\\
&\hspace{35mm} Z-a_m+y_{m-1}, Z-a_m+y_m.
\end{split}
\tag{3.7}
\]

The horizontal edges have the distinct facet colors \(Z-a_i\), the
connectors have the distinct colors

\[
(Z\setminus\{a_i,a_{i+1}\})\cup\{y_i\},
\]

and the induced arcs are (3.6).  Every shared-extra pair has opposite
sign, and every proposed cross chord is the intervening retained core
edge.  This packet is internally Johnson and lower-rainbow.  Extending it
to a complete saturating core is an unproved global extension problem; it
is used here only to close the local pigeonhole argument.

## 4. A quantitative positive theorem for simple seams

Although a Hamilton-preserving witness is not forced, a genuine noncore
chord is forced for many omitted owners.

Call a shared-coordinate witness **bad** if its cross chord is already a
core edge, and **productive** otherwise.  Let \(G_2\) be the step-two graph
on the \(L\) core edges: two core edges are adjacent in \(G_2\) when one
core edge lies between them on the core cycle.  Thus \(G_2\) is one cycle
of length \(L\) if \(L\) is odd and two cycles of length \(L/2\) if \(L\)
is even.  Its components have length greater than \(2m\), since

\[
\frac L2
\ge \frac12\binom{2m+1}{2}>2m
\qquad(m\ge6).
\tag{4.1}
\]

For \(Z\), put \(M_Z=\{e_a:a\in Z\}\).

### Theorem 4.1 (at least asymptotically half have a productive wedge)

Let \(P\) be the number of \(Z\in\mathcal E\) admitting a productive
witness.  Then

\[
\boxed{
P\ge
d-\frac{L}{m-1}
=\frac{(m-2)W}{(m+2)(m-1)}
=\frac{m-2}{2(m-1)}\,d.}
\tag{4.2}
\]

#### Proof

A bad witness between \(e_a,e_b\) makes those marked edges adjacent in
\(G_2\).  If \(p_a=p_b\), the two possible shared coordinates cannot both
be bad: the two horizontal and two cross edges would form a proper
four-cycle component of the core.  Therefore, if every witness for \(Z\)
is bad, the bad witnesses inject into \(E(G_2[M_Z])\).

A set of \(m\) vertices in cycles whose lengths exceed \(m\) induces at
most \(m-1\) edges.  Together with (1.5), an all-bad \(Z\) forces equality:

\[
w_Z=m-1=|E(G_2[M_Z])|.
\]

Hence \(G_2[M_Z]\) is one path, so \(M_Z\) is a cyclic interval of \(m\)
vertices in one component of \(G_2\).

For \(Z\ne Z'\), one has

\[
|M_Z\cap M_{Z'}|\le1,
\tag{4.3}
\]

because two distinct \(m\)-sets share at most one rank-\((m-1)\) facet.
Within either long component of \(G_2\), the starting points of two
length-\(m\) cyclic intervals satisfying (4.3) are separated by at least
\(m-1\).  Thus the number \(e_0\) of all-bad omitted owners obeys

\[
e_0(m-1)\le L.
\]

Subtracting from \(d\) gives (4.2). \(\square\)

This theorem supplies a simple two-factor absorber, not necessarily a
same-sign Hamilton absorber, a proper wedge, or a residence-clean wedge.

### Corollary 4.2 (an unconditional simultaneous family below critical scale)

There is a family of pairwise facet-edge-disjoint, pairwise seam-distinct
productive absorbers of size

\[
\boxed{
r\ge
\left\lceil\frac{P}{3m-3}\right\rceil
\ge
\frac{(m-2)W}{3(m+2)(m-1)^2}.}
\tag{4.4}
\]

It gives a simultaneous simple two-factor exchange on \(L+r\) owners.

#### Proof

Choose one productive option for each of the \(P\) owners.  A fixed facet
color belongs to at most \(m\) omitted owners: among its \(m+2\) middle
extensions, two are the endpoints of its core edge.  Either selected facet
therefore creates at most \(m-1\) conflicts.

A fixed proposed seam \(BD\), with lower color \(T=B\cap D\), can arise
from at most \(m-1\) omitted owners, since necessarily

\[
Z=(T\setminus\{x\})\cup(B\setminus D)\cup(D\setminus B)
\qquad(x\in T).
\tag{4.5}
\]

Thus the conflict graph has maximum degree at most

\[
2(m-1)+(m-2)=3m-4.
\]

A greedy independent set proves (4.4).  Distinct deleted edges and distinct
new seams make the degree ledger additive even when two deleted edges share
a core endpoint. \(\square\)

If literal vertex-disjoint core support is desired, a further factor-five
extraction suffices: along the core, the two selected edges of one absorber
have at most four neighboring selected edges belonging to other absorbers.

The bound (4.4) is only \(\Omega(W/m^2)\).  It does not reach the required
\(\Theta(W/m)\) scale.  It also does not enforce distinct new colors \(T\)
or either orientation/residence condition.

## 5. Exact two-sided singleton audit

For an owner \(X\) with cyclic neighbors \(L_X,R_X\), define

\[
\operatorname{Pos}(X)=X\setminus(L_X\cup R_X),
\qquad
\operatorname{Neg}(X)=(L_X\cap R_X)\setminus X.
\tag{5.1}
\]

These are exactly the coordinates with local membership patterns \(010\)
and \(101\), respectively.  Equivalently, a positive singleton is equality
of the two incident lower colors, while a negative singleton is equality
of the two incident upper unions.

Assume now the same-head Hamilton case (3.3), and write

\[
K=Z\setminus\{a,b\}.
\]

Thus

\[
A=K+b+y,\quad B=K+b+x,\quad
C=K+a+z,\quad D=K+a+x.
\]

Let

\[
P_A=\operatorname{pred}_{\Gamma_0}(A),\quad
Q_B=\operatorname{succ}_{\Gamma_0}(B),\quad
P_C=\operatorname{pred}_{\Gamma_0}(C),\quad
Q_D=\operatorname{succ}_{\Gamma_0}(D).
\tag{5.2}
\]

These are the four retained exterior neighbors after the splice.

### Theorem 5.1 (complete local singleton table)

At the five affected owners of the new Hamilton cycle,

\[
\begin{array}{c|c|c}
X&\operatorname{Pos}(X)&\operatorname{Neg}(X)\\ \hline
A&\{y:y\notin P_A\}&\{a:a\in P_A\}\\
B&\{b:b\notin Q_B\}&\{a:a\in Q_B\}\\
C&\{z:z\notin P_C\}&\{b:b\in P_C\}\\
D&\{a:a\notin Q_D\}&\{b:b\in Q_D\}\\
Z&\varnothing&\{y:y=z\}.
\end{array}
\tag{5.3}
\]

Core lower-rainbowness forces

\[
y\in P_A,qquad x\in Q_B,qquad
z\in P_C,qquad x\in Q_D.
\tag{5.4}
\]

Consequently the splice introduces no positive or negative singleton at
any of the five affected owners if and only if

\[
\boxed{
y\ne z,\quad
a\notin P_A\cup Q_B,\quad
b\notin P_C\cup Q_D,\quad
b\in Q_B,\quad
a\in Q_D.}
\tag{5.5}
\]

#### Proof

The new neighbor pairs are

\[
A:\{P_A,Z\},\quad
B:\{Q_B,D\},\quad
C:\{P_C,Z\},\quad
D:\{Q_D,B\},\quad
Z:\{A,C\}.
\]

Substitution into (5.1) gives (5.3).  For example,
\(B\cap D=T=B-b\), so \(b\) is a positive singleton at \(B\) precisely
when \(Q_B\) also omits \(b\); and \(B\cup D=B+a\), so \(a\) is a
negative singleton there precisely when \(Q_B\) contains \(a\).

If \(y\notin P_A\), the retained edge \(P_AA\) would have lower color
\(A-y=S_a\), duplicating the color of \(AB\) in the rainbow core.  This
proves the first clause of (5.4); the other three are identical.  Combining
(5.3) and (5.4) gives (5.5). \(\square\)

The condition \(y\ne z\) is exactly \(p_a\ne p_b\).  If the two extra
pairs are parallel, whichever common coordinate is used for \(x\), the
other outside coordinate has pattern \(1,0,1\) through \(A,Z,C\).  Thus
distinct lower colors at \(Z\) remove the old positive singleton but can
replace it by a negative singleton.

The two positive clauses \(b\in Q_B\) and \(a\in Q_D\) are equivalent to
saying that the old \(T\)-colored edge is incident with neither \(B\) nor
\(D\).  If, for example, \(BQ_B\) has color \(T=B-b\), the avoided apex
singleton is simply relocated to \(B\).

The four negative clauses say more.  The \(a\)-zero run containing the
marked edge \(AB\) must extend beyond both endpoints, and the \(b\)-zero
run containing \(CD\) must do the same.  Lower q1 rainbowness supplies no
such upper-color residence information.

No supply of proper wedges follows from the pair count alone: the \(m\)
pairs can be distributed with multiplicity over mutually disjoint outside
pairs, so every intersection may be between parallel pairs.  Nor does the
local core-edge ledger force marked edges to lie in the required zero-run
interiors.  The packet (3.7) makes every marked facet edge adjacent, through
a connector, to another marked facet edge; none is zero-interior.  These
are exact local method obstructions.  Excluding them for every complete
saturating core would require a new global structure theorem.

### Proposition 5.2 (exact run-count transport and length-two trap)

Let \(\rho_t\) be the number of cyclic \(0\to1\) arrivals for coordinate
\(t\).  On the present core cycles this is also the number of positive
\(t\)-runs, because no coordinate-membership word is identically one.
One splice changes it by

\[
\boxed{
\Delta\rho_t=
\mathbf1_{\{t\in Z\}}-
\mathbf1_{\{t\in T\}}.}
\tag{5.6}
\]

Thus

\[
\Delta\rho_a=\Delta\rho_b=1,
\qquad
\Delta\rho_x=-1,
\tag{5.7}
\]

and every other coordinate is unchanged.

Even under all singleton-clean conditions (5.5), one may have
\(a\notin P_C\), producing the exact new length-two run

\[
A(0),Z(1),C(1),P_C(0),
\tag{5.8}
\]

or \(b\notin P_A\), producing

\[
P_A(0),A(1),Z(1),C(0).
\tag{5.9}
\]

Hence singleton absorption can raise the shortest new residence only from
one to two; it does not imply FIFO or residence \(m\).

#### Proof

For a cyclic binary word, the number of positive runs is half its number
of boundary edges.  The old edges \(AB,CD\) have boundary coordinates

\[
\{x,y\},\qquad\{x,z\},
\]

while the new edges \(AZ,ZC,BD\) have boundary coordinates

\[
\{a,y\},\qquad\{b,z\},\qquad\{a,b\}.
\]

Taking half the difference proves (5.6)-(5.7).  The displayed membership
patterns prove (5.8)-(5.9). \(\square\)

## 6. Global q1 color and point-margin conditions

Suppose all \(d\) omitted owners are inserted by such absorbers, and let
\(c_T\) be the number of selected chords of lower color \(T\).  Starting
from the core load one on every lower color, the final load is

\[
\mu_1(T)=1+c_T.
\tag{6.1}
\]

Since \(W/L=(m+2)/m\), exact q1 floor/ceiling balance is equivalent to

\[
c_T\in\{0,1\}\quad\text{for every }T;
\tag{6.2}
\]

that is, the \(d\) chord colors must be distinct.  Without this condition,
the total excess above ceiling two is

\[
\sum_T(\mu_1(T)-2)_+
=\sum_T(c_T-1)_+
\le d
=\frac{2W}{m+2}=o(W).
\tag{6.3}
\]

Thus collisions are harmless for an \(o(W)\) scalar overload target but
not for the exact balanced base.

There is a second, independent exact condition.  Let

\[
h_t=\sum_Tc_T\mathbf1_{\{t\in T\}}
\tag{6.4}
\]

be the chord-color degree at coordinate \(t\).  On the full middle layer,
the number of \(11\)-edges for \(t\) is

\[
\binom{2m}{m-2}+h_t.
\]

Since \(t\) belongs to exactly \(mB\) owners, its total \(0\to1\) arrival
count over the final two-factor is

\[
\rho_t
=mB-\binom{2m}{m-2}-h_t
=\frac{3m}{m+2}B-h_t.
\tag{6.5}
\]

Every exact wreath factor has \(\rho_t=B\).  Therefore the chosen chord
multifamily must be point-regular:

\[
\boxed{
h_t=h_*:=\frac{2(m-1)}{m+2}B
\qquad(t\in[n]).}
\tag{6.6}
\]

The average degree is indeed \(h_*\), because
\((m-1)d=nh_*\), but distinct chord colors do not imply point regularity.
Equation (6.6) is the aggregate form of the local transport (5.6).

## 7. Exact simultaneous resource gate

Even before orientation and residence, choosing two distinct facet colors
for every omitted owner, with no core edge reused, is possible if and only
if

\[
\boxed{
|\partial\mathcal A|\ge2|\mathcal A|
\quad\text{for every }\mathcal A\subseteq\mathcal E.}
\tag{7.1}
\]

This is Hall's theorem applied to two clones of every omitted owner.
More generally, if \(K\subseteq\mathcal E\) is absorbed by two-facet moves
and every owner outside \(K\) receives one subdivision facet, the exact
projected condition is

\[
|\partial\mathcal A|
\ge |\mathcal A|+|\mathcal A\cap K|
\quad(\mathcal A\subseteq\mathcal E).
\tag{7.2}
\]

The Lovasz--Kruskal--Katona argument in Proposition 18A proves only the
factor-one part.  This is a genuine method ceiling.  Let

\[
u=\left\lceil\frac{3m}{2}\right\rceil,
\qquad
\mathcal A=\binom{[u]}m.
\]

Then

\[
\frac{|\partial\mathcal A|}{|\mathcal A|}
=\frac{m}{u-m+1}<2.
\tag{7.3}
\]

Moreover, for every \(m\ge6\),

\[
\frac{|\mathcal A|}{W}
=\prod_{j=0}^{m-1}\frac{u-j}{2m+1-j}
\le\left(\frac{u}{2m+1}\right)^m
<\left(\frac34\right)^m
<\frac{2}{m+2}.
\tag{7.4}
\]

The last inequality holds at \(m=6\), and induction works because
\(3/4<(m+2)/(m+3)\).  Thus this violating family can be contained in an
abstract \(m\)-uniform family of size \(d\).  This does not construct it as
the omitted family of an actual saturating core; it proves exactly that
KK plus the cardinality \(d\) cannot yield (7.1).

The true absorber object is stricter than (7.1).  An option

\[
(Z;a,b,x)
\tag{7.5}
\]

simultaneously consumes the two facet edges \(e_a,e_b\), a seam edge
\(BD\), a chord color \(T\), an orientation sign, and local residence
conditions.  A full construction is therefore a correlated colored
hypergraph matching with capacities on all these resources.  Separate
Hall theorems for the projections are not sufficient.

## 8. Exact topology and the critical numerical scale

For \(r\) simultaneous productive absorbers with distinct deleted core
edges, deleting those \(2r\) edges leaves \(2r\) retained core paths and
\(4r\) boundary slots.  Slots are kept distinct even when adjacent deleted
edges leave an isolated core owner.

Let \(\alpha\) pair the two boundary slots belonging to the same retained
core path.  Let \(\beta\) pair, for every absorber,

\[
A\longleftrightarrow C
\quad\text{through the inserted owner }Z,
\qquad
B\longleftrightarrow D
\quad\text{through the direct chord}.
\tag{8.1}
\]

Then the final two-factor components are exactly the alternating cycles of
\(\alpha\cup\beta\), and

\[
\#\{\text{components}\}
=\frac12\#\{\text{cycles of }\alpha\beta\}.
\tag{8.2}
\]

Give every \(\alpha\)-link the number of old owners on its retained path,
every \(A\)-\(C\) link weight one, and every \(B\)-\(D\) link weight zero.
The owner count of a final component is its alternating-cycle weight.

This is the exact simultaneous topology formula.  Pairwise local sign
tests do not replace it.  Sequentially, an exchange on two edges in one
current cycle can preserve or split it; an exchange across two cycles
merges them.  A same-sign move also reverses a whole old arc, so it can flip
the later sign of exactly those candidate edges lying on one side of the
reversal.  Static initial orientations are not adaptive-safe.

One two-facet exchange changes the number of components by at most one.
Ordinary facet subdivision changes it by zero.  Hence reaching \(B\) cycles
from one core cycle requires at least

\[
r\ge B-1.
\tag{8.3}
\]

This is already critical scale, since

\[
\frac Bd=\frac{m+2}{2(2m+1)}=\frac14+o(1).
\tag{8.4}
\]

If all \(d\) owners are absorbed, the exact averages are

\[
\frac{2d}{L}=\frac4m
\tag{8.5}
\]

for the fraction of core edges cut,

\[
\frac{L}{2d}=\frac m4
\tag{8.6}
\]

old owners per retained core path,

\[
\frac dB=4-\frac6{m+2}
\tag{8.7}
\]

inserted owners per target wreath, and

\[
\frac{2d}{B}=8-\frac{12}{m+2}
\tag{8.8}
\]

retained core paths per target wreath.  The proposed mechanism therefore
has exactly the right cardinal scale: about four absorbers and eight old
paths per row.  The unconditional family (4.4) is a factor \(m\) too small
even for the topological lower bound (8.3).

## 9. Why the scale does not imply FIFO

The simultaneous exchanges never alter an internal edge of a component of
\(\Gamma_0-D\), where \(D\) is the selected set of deleted core edges.
Every such path occurs contiguously in the final two-factor, in one of its
two orientations.  Consequently:

1. every retained path must itself embed as a consecutive segment of a
   wreath row;
2. every forbidden coordinate substring wholly internal to a retained path
   survives, up to reversal; and
3. the endpoint permutation (8.2), component weight \(n\), and FIFO history
   are separate constraints.

For example, if a core coordinate has a positive run

\[
0,\underbrace{1,\ldots,1}_{s},0
\]

with \(s\ne m\), at least one of the \(s+1\) boundary/internal core edges of
that displayed substring must be selected; otherwise the forbidden run
persists inside one final component.  The same statement holds for a
negative run of length different from \(m+1\).

In particular, let \(M_-\) be the core owners at which some coordinate has
the pattern \(1,0,1\) through its two core neighbors.  Every vertex in
\(M_-\) must be incident with a deleted core edge.  Since \(r\) absorbers
delete \(2r\) edges and touch at most \(4r\) old endpoints,

\[
|M_-|\le4r
\tag{9.1}
\]

is necessary.  For a full \(d\)-absorber construction this becomes

\[
|M_-|\le4d=\frac{8W}{m+2}.
\tag{9.2}
\]

Lower q1 rainbowness rules out positive singletons in the core but gives no
bound on \(M_-\), nor on positive or negative runs of lengths \(2,3,\ldots\).

There is also an exact short-path test.  A directed Johnson path

\[
X_0,X_1,\ldots,X_\ell,
\qquad \ell\le m,
\]

embeds consecutively in a wreath row if and only if it is geodesic:

\[
d_J(X_0,X_\ell)=\ell.
\tag{9.3}
\]

Necessity follows because the first \(\ell\) exits and entries in a wreath
are all distinct.  Conversely, a Johnson geodesic deletes distinct elements
of \(X_0\) and inserts distinct elements of \(X_0^c\); place these deletions
first in the order of \(X_0\), place their insertions \(m\) positions later,
and complete the coordinate order arbitrarily.  This embeds the path.
Core lower-color rainbowness does not imply (9.3).

For a full \(n\)-owner component, the exact FIFO test is stronger.  If

\[
X_{i+1}=X_i-\{\alpha_i\}+\{\beta_i\}
\qquad(i\bmod n),
\]

then the component is a literal wreath row if and only if the
\(\alpha_i\) form a permutation of \([n]\) and

\[
\beta_i=\alpha_{i+m}
\qquad(i\bmod n).
\tag{9.4}
\]

Neither q1 histogram balance, the point margin (6.6), nor the component
weight equation forces (9.4).

### Theorem 9.1 (exact conditional packetization certificate)

Within the independently productive template--every proposed direct chord
is absent from the initial core--a full collection of \(d\) absorbers
produces an exact balanced-q1 wreath factor if the following, and only the
following, checks hold:

1. every local replacement is a simple Johnson replacement and the global
   degree ledger has no duplicated new edge;
2. the selected facet edges are distinct and the chord colors satisfy
   (6.2) and (6.6);
3. the alternating endpoint graph \(\alpha\cup\beta\) has exactly \(B\)
   components, each of total weight \(n\); and
4. the expanded cyclic owner order on every component satisfies (9.4).

#### Proof

Conditions 1-2 give a simple two-factor on all \(W\) owners with the exact
q1 color and point ledgers.  Condition 3 makes its components have the only
possible wreath order \(n\).  Condition 4 identifies each component
literally as the \(n\) cyclic \(m\)-windows of a coordinate order.  The
converse follows by reading the same ledgers and endpoint paths from any
factor produced by these prescribed replacements. \(\square\)

The theorem is a certificate, not an existence proof: conditions 3-4 are
precisely the weighted composition and FIFO gates left uncontrolled by the
local absorber.  If one permits a proposed chord which is itself a core edge
scheduled for deletion by another absorber, the coupled global exchange may
still be legal; that broader template requires replacing item 1 by a global
edge-cancellation and degree ledger, and is outside the stated
"independently productive" equivalence.

## 10. Proved boundary

The proposed shared-extra construction contains a genuine positive lemma:

* a same-head or same-tail witness gives a simple Hamilton two-facet
  insertion automatically, preserves its two facet colors, and adds exactly
  one lower color \(T\);
* even without the sign condition, at least
  \((m-2)d/[2(m-1)]\) omitted owners have some productive noncore seam;
* one can select \(\Omega(W/m^2)\) simultaneous simple absorbers
  unconditionally.

The following statements are false without further hypotheses:

* the \(m\)-pairs-on-\(m+1\)-points pigeonhole forces a Hamilton-preserving
  wedge;
* distinct incident lower colors at \(Z\) force two-sided singleton
  cleanliness;
* Lovasz--Kruskal--Katona supplies two distinct facet resources per omitted
  owner;
* \(O(W/m)\) local splices, merely by having the right count, force \(B\)
  length-\(n\) FIFO components.

The exact unresolved critical gate is a spatially distributed correlated
option matching of size at least \(B-1\), and ultimately size \(d\), which
simultaneously enforces facet capacity, chord availability and color
regularity, adaptive endpoint topology, two-sided residence, component
weight \(n\), and the lag-\(m\) identities (9.4).

Thus the two-facet absorber improves Proposition 18A's local insertion, but
it does not presently reshape the core into FIFO blocks or prove the
constant-one theorem.
