# Exact q1 arrival normalization and the remaining residence-sewing gate

Date: 2026-07-25  
Line: N — packetization from Proposition 18A

## 0. Verdict

Let

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn,
\qquad N_1=\binom n{m-1}.
\]

Proposition 18A of
`TRANSLATION_PACKET_MULTIDEPTH_RAINBOW_LEMMA_20260725.md` gives a Hamilton
Johnson cycle whose rank-\((m-1)\) intersection multiplicities are exactly
one or two.  This note proves the following quantitative strengthening and
separates it from the unresolved packetization step.

1. For **every** such balanced Hamilton cycle, the total discrepancy of its
   coordinate arrival counts from the wreath value \(B\) is at most

   \[
   \boxed{
   \frac{2W}{m+2}
   \sqrt{2(m-1)\log(m/2)}
   =O\!\left(W\sqrt{\frac{\log m}{m}}\right)=o(W).}
   \]

   This is automatic; it does not depend on how the facet SDR in
   Proposition 18A is chosen.

2. At the level of the duplicated-color family, exact point regularity can
   be reached by at most half this many elementary set exchanges.  This is
   only a label-level normalization: the exchanges need not preserve the
   SDR, the Hamilton cycle, reciprocal endpoint incidence, or FIFO
   residence.

3. The particular SDR insertion used in Proposition 18A creates exactly

   \[
   d=W-N_1=\frac{2W}{m+2}
   \]

   singleton positive coordinate runs.  Their incident edge pairs are
   disjoint.  Consequently every genuine wreath factor must delete at least
   \(d\) edges of that Hamilton cycle.  This cost is still \(o(W)\), but it
   rules out a one-seam-per-packet cutting of the displayed Hamilton order.

4. More strongly, the half-\(\ell^1\) residence-length defect of the inserted
   Hamilton cycle is at least

   \[
   \boxed{
   d(m-1)=\frac{2(m-1)}{m+2}W=(2-o(1))W.}
   \]

   Thus near-perfect arrival multiplicities and exact q1 histogram balance
   coexist with a linear residence defect.

5. An exact FIFO block criterion and a restricted conversion theorem are
   proved below.  If a Hamilton cycle can be divided into \(B\) consecutive
   \(n\)-vertex FIFO blocks, replacing exactly the \(B\) boundary edges gives
   an exact wreath factor with q1 overload at most \(B=o(W)\).  Proposition
   18A by itself does not supply those FIFO blocks; in fact its \(d>B\)
   singleton insertions prevent this direct one-boundary-per-block route.

No theorem here constructs an exact factor with q1 overload \(o(W)\).  The
proved advance is that the arrival-count margin is automatically sublinear,
while the unresolved obstruction is genuinely ordered reciprocal residence.

Throughout, logarithms are natural.

## 1. Balanced q1 colors and coordinate runs

Let \(C\) be any spanning two-factor of the Johnson graph on
\(\binom{[n]}m\).  A Hamilton cycle is the special case relevant to
Proposition 18A.  For a Johnson edge \(XY\), its lower color is

\[
\chi(XY)=X\cap Y\in\binom{[n]}{m-1}.
\]

Assume every lower color has multiplicity one or two.  Put

\[
\mathcal H=\{S:\text{the color }S\text{ has multiplicity }2\},
\qquad h_x=|\{S\in\mathcal H:x\in S\}|.
\tag{1.1}
\]

Counting colors gives

\[
|\mathcal H|=W-N_1=:d=\frac{2W}{m+2},
\qquad
\frac d{N_1}=\frac2m.
\tag{1.2}
\]

Orient every component of \(C\).  Let \(r_x(C)\) be the number of
\(0\)-to-\(1\) transitions of the indicator \(\mathbf1_{x\in X}\) along all
oriented components, equivalently half the number of factor edges crossing
the point cut for \(x\).  On every component on which the indicator is
nonconstant this is the number of cyclic positive runs; a constant component
contributes zero.  The total is independent of the chosen component
orientations.

Define

\[
h_*:=\frac{(m-1)d}{n}
=\frac{2(m-1)B}{m+2}.
\tag{1.3}
\]

The quantity \(h_*\) is integral.  Indeed,

\[
h_*=(m-1)B-\binom{2m}{m-2}.
\tag{1.4}
\]

### Theorem 1.1 (exact q1 color-run identity)

For every coordinate \(x\),

\[
\boxed{r_x(C)=B+h_*-h_x.}
\tag{1.5}
\]

In particular,

\[
\sum_{x=1}^n|r_x(C)-B|
=\sum_{x=1}^n|h_x-h_*|.
\tag{1.6}
\]

#### Proof

Exactly

\[
M_x=\binom{n-1}{m-1}=mB
\tag{1.7}
\]

middle vertices contain \(x\).  On each cyclic binary word, the number of
adjacent \(11\) pairs is its number of ones minus its number of
\(0\)-to-\(1\) transitions; this remains true for constant words.  Summing
over components gives \(M_x-r_x\).

A Johnson edge has both endpoints containing \(x\) precisely when its lower
color contains \(x\).  Since every lower color occurs once and the colors in
\(\mathcal H\) occur once more, the number of such edges is

\[
\binom{n-1}{m-2}+h_x
=\binom{2m}{m-2}+h_x.
\tag{1.8}
\]

Therefore

\[
r_x=mB-\binom{2m}{m-2}-h_x.
\tag{1.9}
\]

Using

\[
\binom{2m}{m-2}
=\frac{m(m-1)}{m+2}B
\tag{1.10}
\]

turns (1.9) into (1.5).  Equation (1.6) follows.  \(\square\)

Every exact wreath factor has exactly \(B\) positive runs of each
coordinate: every one of its \(B\) rows has one coordinate interval of
length \(m\).  Hence (1.5) shows that exact point regularity

\[
h_x=h_*\qquad(x\in[n])
\tag{1.11}
\]

is a necessary condition on any balanced q1 color family arising from a
wreath factor.

## 2. A universal entropy bound for the high-color degrees

The sparse density \(d/N_1=2/m\) alone forces the point degrees of
\(\mathcal H\) to be close to regular in aggregate.

### Lemma 2.1 (slice marginal entropy bound)

Let \(1\le r<n\), let \(\mathcal A\subseteq\binom{[n]}r\) have density
\(\alpha\), and put

\[
p=\frac rn,
\qquad
p_x=\Pr_{S\text{ uniform in }\mathcal A}(x\in S).
\]

Then

\[
\boxed{
\sum_{x=1}^n|p_x-p|
\le \sqrt{2r\log(1/\alpha)}.}
\tag{2.1}
\]

#### Proof

Choose

\[
\varepsilon_x=\operatorname{sgn}(p_x-p),
\]

with value zero when \(p_x=p\), and define on the full \(r\)-slice

\[
Z(S)=\sum_x\varepsilon_x(\mathbf1_{x\in S}-p).
\tag{2.2}
\]

Then

\[
\mathbb E_{\mathcal A}Z
=\sum_x|p_x-p|.
\tag{2.3}
\]

Let \(U\) denote the uniform distribution on the full slice.  Maclaurin's
inequality for elementary symmetric means gives, for \(\lambda>0\),

\[
\begin{aligned}
\mathbb E_U\exp\!\left(\lambda\sum_{x\in S}\varepsilon_x\right)
&=\frac{e_r(e^{\lambda\varepsilon_1},\ldots,
             e^{\lambda\varepsilon_n})}{\binom nr}\\
&\le
\left(\frac1n\sum_{x=1}^n e^{\lambda\varepsilon_x}\right)^r.
\end{aligned}
\tag{2.4}
\]

If \(Y\) is uniformly chosen from the numbers
\(\varepsilon_1,\ldots,\varepsilon_n\), then \(Y\in[-1,1]\).  Hoeffding's
elementary bounded-variable lemma gives

\[
\mathbb E e^{\lambda(Y-\mathbb EY)}\le e^{\lambda^2/2}.
\tag{2.5}
\]

Since \(p=r/n\), multiplying (2.4) by the centering factor in (2.2) and
using (2.5) yields

\[
\mathbb E_Ue^{\lambda Z}\le e^{r\lambda^2/2}.
\tag{2.6}
\]

The event \(S\in\mathcal A\) has \(U\)-probability \(\alpha\).  Jensen and
(2.6) therefore imply

\[
\lambda\mathbb E_{\mathcal A}Z
\le \log\mathbb E_{\mathcal A}e^{\lambda Z}
\le \log(1/\alpha)+\frac{r\lambda^2}{2}.
\tag{2.7}
\]

Choose

\[
\lambda=\sqrt{\frac{2\log(1/\alpha)}r}.
\]

Equations (2.3) and (2.7) give (2.1).  \(\square\)

### Theorem 2.2 (automatic sublinear arrival discrepancy)

For the high-color family in (1.1),

\[
\boxed{
D_1(\mathcal H):=\sum_x|h_x-h_*|
\le
d\sqrt{2(m-1)\log(m/2)}.}
\tag{2.8}
\]

Consequently

\[
\boxed{
\frac{D_1(\mathcal H)}W
\le
\frac{2}{m+2}\sqrt{2(m-1)\log(m/2)}
=O\!\left(\sqrt{\frac{\log m}{m}}\right).}
\tag{2.9}
\]

The same bounds hold for
\(\sum_x|r_x(C)-B|\).

#### Proof

Apply Lemma 2.1 with

\[
r=m-1,\qquad \mathcal A=\mathcal H,
\qquad \alpha=d/N_1=2/m.
\]

Here \(p_x=h_x/d\) and \(dp=h_*\).  Multiply (2.1) by \(d\), then use
Theorem 1.1.  \(\square\)

This bound includes highly concentrated families.  For example, if
\(\mathcal H\) is contained in a fixed \(c\)-star, then

\[
\frac2m=\frac d{N_1}
\le\frac{(m-1)_c}{(2m+1)_c}<2^{-c},
\tag{2.10}
\]

so necessarily \(c\le\log_2(m/2)\).  Concentrating all high colors on a
large fixed core cannot produce a linear degree discrepancy.

## 3. Exact point regularization by few abstract color swaps

The preceding approximate regularity can be rounded exactly inside the
simple-set fibre.

### Theorem 3.1 (degree-balancing exchange)

Let \(\mathcal H\subseteq\binom{[n]}r\) be simple, \(|\mathcal H|=d\), and
assume \(h_*=rd/n\) is an integer.  There is a simple family
\(\mathcal H^{\rm reg}\subseteq\binom{[n]}r\), also of size \(d\), such
that

\[
\deg_{\mathcal H^{\rm reg}}(x)=h_*
\qquad(x\in[n]),
\tag{3.1}
\]

and \(\mathcal H^{\rm reg}\) is obtained from \(\mathcal H\) by at most

\[
\boxed{
\frac12\sum_x|h_x-h_*|}
\tag{3.2}
\]

exchanges of the form

\[
S\longmapsto S-x+y.
\tag{3.3}
\]

#### Proof

Unless all degrees equal \(h_*\), choose \(x,y\) with

\[
h_x>h_*>h_y.
\]

Let \(\mathcal A_{x\bar y}\) be the members of \(\mathcal H\) containing
\(x\) but not \(y\), and define \(\mathcal A_{\bar x y}\) analogously.
Then

\[
|\mathcal A_{x\bar y}|-|\mathcal A_{\bar x y}|=h_x-h_y>0.
\tag{3.4}
\]

The map \(S\mapsto S-x+y\) is a bijection between all \(r\)-sets of the
first type and all \(r\)-sets of the second type.  If every image of a
member of \(\mathcal A_{x\bar y}\) already belonged to \(\mathcal H\),
then (3.4) would be impossible.  Hence some \(S\in\mathcal H\) has

\[
S-x+y\notin\mathcal H.
\]

Perform (3.3).  Simplicity and size are preserved, \(h_x\) drops by one,
\(h_y\) rises by one, and the \(\ell^1\) distance from the constant degree
vector drops by exactly two.  Iteration proves (3.1)--(3.2).  \(\square\)

For Proposition 18A, Theorem 2.2 and (3.2) give an abstract exactly regular
high-color family after

\[
O\!\left(W\sqrt{\frac{\log m}{m}}\right)=o(W)
\tag{3.5}
\]

color exchanges.

This is **not** an actual Hamilton-cycle switch theorem.  In Proposition
18A, each high color is the chosen facet of a particular omitted owner.
The exchange (3.3) need not remain a facet of that owner, and even if it
does, it need not preserve distinct representatives.  It also supplies no
reciprocal endpoint pairing or packet residence.

For reference, if \(\mathcal E\) is the omitted family, put

\[
e_x=|\{Z\in\mathcal E:x\in Z\}|,
\qquad
a_x=|\{Z\in\mathcal E:Z\setminus S_Z=\{x\}\}|.
\tag{3.6}
\]

The SDR high family satisfies the exact identity

\[
h_x=e_x-a_x.
\tag{3.7}
\]

Thus exact arrival balance inside the fixed omitted family would require

\[
a_x=e_x-h_*
\qquad(x\in[n]).
\tag{3.8}
\]

In particular, \(e_x\ge h_*\) for every \(x\) is a necessary condition for
an exactly point-regular facet SDR.  Lovasz--Kruskal--Katona Hall proves an
unconstrained facet SDR, not the simultaneous quota system (3.8).

## 4. An exact recourse lower bound for arrival multiplicity

Let \(F\) be any exact wreath factor on the same middle vertices.  Let

\[
k=|E(C)\setminus E(F)|=|E(F)\setminus E(C)|.
\tag{4.1}
\]

The equality holds because both graphs are spanning two-factors and have
\(W\) edges.

### Proposition 4.1 (crossing-count recourse bound)

For every balanced q1 two-factor \(C\),

\[
\boxed{k\ge\frac12D_1(\mathcal H).}
\tag{4.2}
\]

#### Proof

For a two-factor \(G\), let \(b_G(x)\) be the number of its edges crossing
the point cut

\[
\{X:x\in X\}\mid\{X:x\notin X\}.
\]

Then \(b_C(x)=2r_x(C)\), while \(b_F(x)=2B\).  Every Johnson edge crosses
exactly two point cuts, namely those of its exchanged coordinates.
Therefore

\[
\begin{aligned}
2D_1(\mathcal H)
&=\sum_x|b_C(x)-b_F(x)|\\
&\le \sum_{e\in E(C)\triangle E(F)}2
=4k.
\end{aligned}
\]

Use Theorem 1.1 and divide by two.  \(\square\)

Theorem 2.2 says that this particular necessary recourse is always
sublinear.  Proposition 4.1 supplies no converse: prescribed changes of
point-cut counts need not be realizable by reciprocal Johnson seams.

## 5. The SDR insertion has linear residence defect

Return to the exact construction of Proposition 18A.  Begin with the
\(N_1\)-vertex saturating Johnson cycle.  For every omitted middle set
\(Z\in\mathcal E\), its chosen facet \(S_Z\) colors a unique old edge

\[
A_ZB_Z,
\qquad
A_Z\cap B_Z=S_Z.
\]

Subdivide this edge as

\[
A_Z-Z-B_Z.
\tag{5.1}
\]

Write

\[
Z=S_Z\cup\{z\},\qquad
A_Z=S_Z\cup\{a\},\qquad
B_Z=S_Z\cup\{b\}.
\]

The three added coordinates \(a,b,z\) are pairwise distinct, so the
membership pattern of \(z\) on (5.1) is

\[
0,1,0.
\tag{5.2}
\]

### Lemma 5.1 (exact singleton-run count)

The inserted Hamilton cycle has exactly \(d\) singleton positive runs, one
at each inserted vertex.  No edge of the Hamilton cycle is incident with
two inserted vertices.

#### Proof

At a vertex \(X\) of a simple Johnson cycle, let the two incident lower
colors be \(S,T\).  The coordinate entering \(X\) leaves immediately if
and only if

\[
S=T=X-\{x\},
\]

so singleton positive runs are exactly the vertices whose two incident
lower colors agree.

Before insertion, every lower color occurs exactly once, so the two incident
colors at every old vertex are distinct.  Subdivision (5.1) leaves the old
incident colors distinct at old vertices and gives the repeated color
\(S_Z,S_Z\) at \(Z\).  Hence there are exactly \(d\) singleton runs.

Distinct omitted vertices are inserted into distinct old edges because the
facet representatives are distinct.  Even when two selected old edges share
an endpoint, their inserted vertices are separated by that old endpoint.
Thus inserted vertices are pairwise nonadjacent, and every new Hamilton edge
is incident with at most one of them.  \(\square\)

### Proposition 5.2 (actual edge-recourse floor)

Every exact wreath factor \(F\) on the middle layer satisfies

\[
\boxed{|E(C)\setminus E(F)|\ge d=\frac{2W}{m+2}.}
\tag{5.3}
\]

#### Proof

If both Hamilton edges incident with an inserted vertex \(Z\) were retained
in \(F\), the degree-two condition would force the local triple
\(A_Z-Z-B_Z\) to occur consecutively in one factor component.  By (5.2),
coordinate \(z\) would then have a positive run of length one.  In a wreath
row every coordinate has one positive run of length \(m\), a contradiction.

Thus at least one of the two incident Hamilton edges must be removed for
every inserted vertex.  Lemma 5.1 says these incident edge pairs are
edge-disjoint, proving (5.3).  \(\square\)

This is a genuine lower bound for arbitrary repacketization, but it is only
\(O(W/m)=o(W)\); it does not obstruct coefficient one.

For a sharper diagnosis of residence, let \(\mathscr R(C)\) be the set of
all maximal cyclic positive coordinate runs, counted with their coordinate
and occurrence, and define

\[
\Delta_{\rm run}(C)
=\frac12\sum_{R\in\mathscr R(C)}\bigl||R|-m\bigr|.
\tag{5.4}
\]

### Proposition 5.3 (linear run-length defect)

For the Proposition 18A Hamilton cycle,

\[
\boxed{
\Delta_{\rm run}(C)
\ge d(m-1)
=\frac{2(m-1)}{m+2}W.}
\tag{5.5}
\]

#### Proof

Every oriented Hamilton edge has one entering coordinate and hence starts
one positive run.  Thus

\[
|\mathscr R(C)|=W.
\]

The total length of all positive runs is the number of point--middle-owner
incidences,

\[
\sum_{R\in\mathscr R(C)}|R|=mW.
\]

Consequently

\[
\sum_R(|R|-m)=0,
\]

and (5.4) equals both the total shortfall of the runs shorter than \(m\)
and the total excess of the runs longer than \(m\).  Each of the \(d\)
singleton runs from Lemma 5.1 contributes \(m-1\) to the shortfall.
This proves (5.5).  \(\square\)

If one is allowed to cut only \(B\) old Hamilton edges and then sew the
resulting whole paths without changing their internal order, at most \(B\)
inserted vertices are incident with a cut.  Hence at least \(d-B\)
singleton triples survive internally.  Their retained run shortfall is at
least

\[
\boxed{
(d-B)(m-1)
=\frac{3m(m-1)}{(m+2)(2m+1)}W
=\left(\frac32-o(1)\right)W.}
\tag{5.6}
\]

Thus no choice of a block offset can repair the inserted Hamilton order by
one seam per desired packet.  Internal rewiring, contraction/release of the
insertions, or a larger number of path pieces is compulsory.

The contrast between (2.9) and (5.5) is decisive:

\[
\text{arrival-count discrepancy}=o(W),
\qquad
\text{residence-length defect}=\Omega(W).
\tag{5.6a}
\]

Therefore no argument using only the high-color point degrees can prove
packetization.

### Lemma 5.3A (short residence forces a chronological color collision)

Let a coordinate \(a\) have a maximal positive run

\[
X_s,X_{s+1},\ldots,X_{s+r-1}
\tag{5.6b}
\]

in any Johnson cycle.  Then

\[
\boxed{
\bigcap_{j=s-1}^{s+r-1}X_j
=
\bigcap_{j=s}^{s+r}X_j
=
\left(\bigcap_{j=s}^{s+r-1}X_j\right)\setminus\{a\}.}
\tag{5.6c}
\]

#### Proof

The predecessor \(X_{s-1}\) omits \(a\) and differs from \(X_s\) in only
the exchange which introduces \(a\).  Hence it contains every member of
\(X_s\setminus\{a\}\), and intersecting it with the run intersection removes
exactly \(a\).  The successor \(X_{s+r}\) gives the same argument at the
other end.  \(\square\)

For \(r=1\), (5.6c) is exactly the repeated-lower-color diagnosis used in
Lemma 5.1.  For every \(2\le r\le K\), avoiding residence \(r\) requires a
separate noncollision condition on consecutive depth-\(r\) intersection
colors.  The q1 histogram contains none of this chronological information.

### Proposition 5.4 (exact reciprocal-sewing forest)

Choose, independently at every inserted vertex \(Z\), exactly one of the
two Hamilton edges incident with \(Z\), and delete the chosen edges.  The
remaining graph is a spanning linear forest with exactly

\[
d=\frac{2W}{m+2}
\tag{5.7}
\]

components and exactly one edge of every lower color.

Consequently, a two-factor with the **same q1 histogram as the Hamilton
cycle** which preserves all remaining forest edges is equivalent to a
pairing of the \(2d\) endpoint slots by \(d\) new Johnson edges whose lower
colors are precisely the members of \(\mathcal H\), each used once.  Such a
completion is a wreath factor if
and only if the component-sewing produces exactly \(B\) cycles, each has
\(n\) owners, and every resulting cycle satisfies the residence/FIFO
criterion.

The exact mean number of forest components which must be sewn into one
wreath is

\[
\boxed{
\frac dB=\frac{2(2m+1)}{m+2}=4-\frac6{m+2}.}
\tag{5.8}
\]

#### Proof

Lemma 5.1 says the two incident-edge pairs at different inserted vertices
are edge-disjoint, so the \(d\) deleted edges are distinct.  Deleting \(d\)
edges from one cycle produces a spanning linear forest with \(d\)
components, with the usual interpretation that a vertex between two deleted
edges is an isolated path.

At an inserted vertex, both incident edges have the same high color
\(S_Z\).  Deleting exactly one leaves one occurrence of \(S_Z\).  No edge
of an unchosen lower color is deleted.  Thus every one of the \(N_1\) lower
colors occurs exactly once in the forest.

Its total degree deficit from two-regularity is \(2d\), represented by two
endpoint slots per path component, including two slots at an isolated
vertex.  Any degree-two completion preserving all forest edges therefore
pairs these slots with exactly \(d\) new edges.  Since the forest already
uses every lower color once, the final histogram is one or two with the
same high family \(\mathcal H\) exactly when the new edge colors are a
bijection onto \(\mathcal H\).  This proves the reciprocal-sewing
equivalence.

Finally, a degree-two completion is an exact wreath factor precisely when
its components are \(B\) genuine length-\(n\) wreath cycles.  Formula (5.8)
is immediate from \(W=nB\) and (5.7).  \(\square\)

Proposition 5.4 is the cleanest exact use of the strengthened q1 base.  It
reduces packetization to a constant-average-arity reciprocal sewing problem:
roughly four rainbow forest pieces per desired row.  It does **not** prove
that the required endpoint-color matching exists.  Even a matching would
only give a balanced two-factor; cycle length and residence remain separate
conditions.

### Proposition 5.5 (oriented reciprocal graph and the diagonal trap)

Index the insertions by \(i\in[d]\), writing their subdivided old edges as

\[
A_i-Z_i-B_i,
\qquad A_i\cap B_i=S_i,
\qquad Z_i=S_i\cup\{z_i\}.
\tag{5.9}
\]

Choose an adjacent-deletion orientation

\[
p_i\in\{A_i,B_i\},
\tag{5.10}
\]

meaning that the deleted edge is \(Z_ip_i\).  The endpoint slots of the
resulting forest are then

\[
Z_1,\ldots,Z_d
\quad\text{and}\quad
p_1,\ldots,p_d,
\tag{5.11}
\]

with slots counted separately when the same old owner occurs twice.

Define the reciprocal bipartite graph \(R_p\) on two copies of \([d]\) by

\[
i\sim j
\quad\Longleftrightarrow\quad
S_i\subset p_j.
\tag{5.12}
\]

Every perfect matching \(\varphi\) of \(R_p\) gives a q1-histogram-
preserving two-factor by adding the seams

\[
Z_i p_{\varphi(i)}
\qquad(i\in[d]).
\tag{5.13}
\]

Conversely, every completion which pairs each inserted endpoint slot with
an old endpoint slot **and assigns its own color \(S_i\) to the seam at
\(Z_i\)** has this form.

The diagonal \(i\sim i\) is always present.  Its perfect matching merely
restores every deleted edge and recovers the original Hamilton cycle.
Therefore ordinary Hall feasibility of \(R_p\) proves nothing productive.
Any sewing theorem must control an off-diagonal matching together with the
cycle lengths and FIFO histories induced after the forest paths are
contracted.

The own-color, inserted-to-old restriction is a sufficient sewing
architecture, not a lossless description of every completion.  A general
completion may assign another high color to a seam at \(Z_i\), or may pair
two inserted slots and two old slots.  That general problem is a colored
endpoint-pairing hypergraph rather than the bipartite graph \(R_p\).

#### Proof

The inclusion \(S_i\subset p_i\) gives every diagonal edge.  If
\(i\sim j\), then both \(Z_i\) and \(p_j\) contain \(S_i\).  They are
distinct because every \(Z_i\) was omitted from the saturating cycle whereas
every \(p_j\) is an old used vertex.  Thus they are Johnson adjacent and

\[
Z_i\cap p_j=S_i.
\]

A perfect matching uses every inserted endpoint slot and every old endpoint
slot once, so (5.13) restores degree two everywhere.  Its new lower colors
are \(S_1,\ldots,S_d\), each once; Proposition 5.4 shows that the original
histogram is restored.  Under the stated own-color restriction, the converse
follows by reading the old endpoint paired with each \(Z_i\).  Finally, the
diagonal seam \(Z_ip_i\) is exactly the edge deleted in (5.10), proving the
trap statement.  \(\square\)

There is an exact contracted description of the remaining order condition.
Contract every path component of the forest to an edge joining its two
endpoint slots.  These \(d\) path edges form a perfect matching \(P_p\) on
the \(2d\) slots.  The seams (5.13) form a second perfect matching
\(M_\varphi\).  Hence

\[
P_p\cup M_\varphi
\tag{5.14}
\]

is a disjoint union of even cycles.  Those cycles are exactly the components
of the completed owner two-factor before contraction.  A successful wreath
completion requires exactly \(B\) such cycles, total owner length \(n\) on
each, and the FIFO identities of Lemma 6.1 along every expanded cycle.

Thus the live q1 theorem is not ordinary Hall.  It is an adaptive choice of
\(p_i\in\{A_i,B_i\}\), followed by a productive reciprocal matching in
\(R_p\), satisfying simultaneous weighted-cycle and FIFO constraints.

### Proposition 5.6 (exact adjacent-deletion length transport)

Index the \(N_1\) edges of the unexpanded saturating cycle cyclically.  Let

\[
s_1,s_2,\ldots,s_d
\]

be the cyclic positions of the edges selected by the facet SDR, and put

\[
g_i=s_{i+1}-s_i\pmod {N_1},
\qquad g_i\ge1,
\qquad \sum_i g_i=N_1.
\tag{5.15}
\]

Encode the adjacent-deletion choice by \(\varepsilon_i=0\) when the first
half of the subdivided edge is cut and \(\varepsilon_i=1\) when the second
half is cut.  In cyclic order, the \(d\) path components of the resulting
forest have vertex lengths

\[
\boxed{
\ell_i=g_i+1+\varepsilon_{i+1}-\varepsilon_i.}
\tag{5.16}
\]

In particular,

\[
\sum_i\ell_i=W,
\qquad
g_i\le\ell_i\le g_i+2.
\tag{5.17}
\]

If the forest is completed to a wreath factor without changing an internal
forest edge, then necessarily:

1. every path is itself a segment of a wreath and hence \(\ell_i\le n\);
2. the multiset \(\{\ell_i\}\) can be partitioned into \(B\) groups, each
   with total length exactly \(n\); and
3. within each group, the endpoint seams obey the reciprocal color
   constraints and the expanded owner order obeys FIFO.

Thus a gap \(g_i\ge n+1\) is an orientation-independent obstruction to
whole-path sewing.

#### Proof

Replacing a selected old edge by two edges adds one unit of cyclic length.
Between the first half of selected edge \(i\) and the first half of selected
edge \(i+1\), the expanded cyclic distance is therefore \(g_i+1\).
Moving the first cut to the second half subtracts one from that distance,
whereas moving the second cut to its second half adds one.  This is exactly
(5.16).  Summing telescopes and uses (5.15), giving (5.17).

Every retained path lies wholly inside one component of any completion,
because its internal vertices already have degree two.  In a genuine wreath
component it is therefore a consecutive wreath segment; it cannot have more
than \(n\) distinct owners.  The paths in each completed component partition
its \(n\) owners, proving the group-sum condition.  Reciprocal colors and
FIFO are necessary by the definitions of the seams and wreaths.  Finally,
the smallest possible value in (5.16) is \(g_i\), so \(g_i\ge n+1\) forces
\(\ell_i>n\).  \(\square\)

Formula (5.16) shows exactly how little freedom adjacent deletion provides:
it transports one unit of path length from one neighboring gap to another.
Lovasz--Kruskal--Katona Hall gives distinct facet representatives but gives
no spacing theorem for the selected edge positions \(s_i\).  Consequently
it gives neither the bound \(g_i\le n\) nor the exact \(n\)-bin composition
required above.

This spacing obstruction alone is not a coefficient-one obstruction.  Any
path of length \(\ell_i>n\) can be cut into
\(\lceil\ell_i/n\rceil\) shorter paths, and

\[
\sum_i\left(\left\lceil\frac{\ell_i}{n}\right\rceil-1\right)
\le B
\tag{5.18}
\]

because \(\sum_i\ell_i=nB\).  Thus arbitrary long gaps cost at most another
\(B=o(W)\) cuts.  What remains uncontrolled is whether the resulting pieces
are FIFO-compatible and whether their endpoint/color graph admits the
required reciprocal grouping.

## 6. Exact FIFO test for an n-vertex Johnson block

The remaining ordered condition has a compact deterministic form.

Let

\[
X_0,X_1,\ldots,X_{n-1}
\tag{6.1}
\]

be a simple directed Johnson path.  For \(0\le i\le n-2=2m-1\), write

\[
X_{i+1}=X_i-\{a_i\}+\{b_i\}.
\tag{6.2}
\]

### Lemma 6.1 (exact open-block FIFO criterion)

The path (6.1) is the ordered list of all \(m\)-windows of one cyclic
coordinate order if and only if:

1. the \(n\) coordinates

   \[
   a_0,a_1,\ldots,a_{2m-1},b_m
   \tag{6.3}
   \]

   are pairwise distinct;

2. the forward FIFO identities hold:

   \[
   b_i=a_{i+m}
   \qquad(0\le i\le m-1);
   \tag{6.4}
   \]

3. the wrapped FIFO identities hold:

   \[
   b_i=a_{i-m-1}
   \qquad(m+1\le i\le2m-1).
   \tag{6.5}
   \]

When these conditions hold, the missing closing edge is

\[
X_{n-1}\longrightarrow X_0
=X_{n-1}-\{b_m\}+\{a_{m-1}\}.
\tag{6.6}
\]

#### Proof

For a cyclic order \(z_0,\ldots,z_{n-1}\), its windows

\[
X_i=\{z_i,z_{i+1},\ldots,z_{i+m-1}\}
\]

obey

\[
a_i=z_i,\qquad b_i=z_{i+m}\quad\text{modulo }n.
\]

This immediately gives (6.3)--(6.6).

Conversely, define

\[
z_i=a_i\quad(0\le i\le2m-1),
\qquad z_{2m}=b_m.
\tag{6.7}
\]

Condition (6.3) makes this a permutation of \([n]\).  For
\(0\le j<m\), the earlier arrivals in (6.2) are, by (6.4), among
\(a_m,\ldots,a_{2m-2}\), and are distinct from \(a_j\).  Since
\(a_j\in X_j\), induction backwards through the first \(j\) transitions
shows that \(a_j\in X_0\).  Hence

\[
X_0=\{a_0,\ldots,a_{m-1}\}
=\{z_0,\ldots,z_{m-1}\}.
\]

Equations (6.4), the exceptional identity \(b_m=z_{2m}\), and (6.5) now
say exactly that every transition removes \(z_i\) and inserts
\(z_{i+m}\) modulo \(n\).  Induction gives all the required windows, and
the final unused transition is (6.6).  \(\square\)

For a Hamilton Johnson cycle \(C\), define its **wreath path-cut number**

\[
\tau_{\rm wr}(C)
=\min\{|K|:\text{every path component of }C-K
\text{ is a consecutive segment of a wreath row}\}.
\tag{6.8}
\]

Segments may be taken in either orientation.

### Proposition 6.2 (sharp common-edge packetization obstruction)

The following hold.

1. For every Hamilton cycle,

   \[
   \tau_{\rm wr}(C)\ge B.
   \tag{6.9}
   \]

2. If an exact wreath factor \(F\) retains \(W-k\) edges of \(C\), then

   \[
   \boxed{k\ge\tau_{\rm wr}(C).}
   \tag{6.10}
   \]

3. Equality \(\tau_{\rm wr}(C)=B\) holds if and only if deleting \(B\)
   edges partitions \(C\) into \(B\) FIFO blocks of \(n\) vertices; closing
   those blocks converts \(C\) into an exact wreath factor with exactly
   \(B\) old-edge deletions.

4. For the inserted Hamilton cycle of Proposition 18A,

   \[
   \tau_{\rm wr}(C)\ge d=\frac{2W}{m+2}.
   \tag{6.11}
   \]

#### Proof

A simple segment of one wreath row contains at most its \(n\) owners.  A cut
of a Hamilton cycle into wreath-embeddable paths therefore needs at least
\(W/n=B\) components, proving (6.9).

If \(F\) omits \(k\) old Hamilton edges, the graph consisting of the common
edges \(E(C)\cap E(F)\) is obtained from \(C\) by those \(k\) cuts.  Every
one of its path components lies consecutively inside one wreath component of
\(F\), so it is wreath-embeddable.  This proves (6.10).

If exactly \(B\) cuts suffice, their \(B\) path components have total size
\(W=nB\) and each has at most \(n\) vertices.  Hence every component has
exactly \(n\) vertices.  An \(n\)-vertex segment of a wreath row is the full
row with one edge removed, so adding its closing edge gives a factor.  The
converse is immediate.

Finally, every wreath-embeddable path can contain at most one of the two
Hamilton edges incident with an inserted singleton vertex.  The \(d\)
incident edge pairs are disjoint by Lemma 5.1, so every admissible cut set
has size at least \(d\).  \(\square\)

The entropy theorem controls the weaker point-cut statistic
\(D_1(\mathcal H)\); it gives no upper bound on
\(\tau_{\rm wr}(C)\).  Proposition 5.3 exhibits the separation: the first is
\(o(W)\), while the raw residence defect can be linear.

## 7. A restricted exact block-sewing theorem

The FIFO criterion yields a literal positive conversion statement.

### Theorem 7.1 (FIFO block conversion)

Let \(C=(X_0,X_1,\ldots,X_{W-1})\) be a Hamilton Johnson cycle, and suppose
that for some cyclic offset its vertex order splits into \(B=W/n\)
consecutive blocks of \(n\) vertices, each satisfying Lemma 6.1 in its
inherited orientation.  Replace, for every block, the old Hamilton edge
from its last vertex to the first vertex of the next block by the closing
edge (6.6) inside that block.

Then the result is an exact middle wreath factor.  It differs from \(C\) in
exactly \(B\) old edges and \(B\) new edges.  If the q1 histogram of \(C\)
is balanced, the q1 overload of the resulting factor is at most

\[
\boxed{B=\frac W{2m+1}=o(W).}
\tag{7.1}
\]

#### Proof

Lemma 6.1 says that each block closes to one genuine wreath row.  The blocks
partition all middle owners, so their closures form an exact factor.

Only the \(B\) inter-block Hamilton edges are removed, and only the \(B\)
within-block closing edges are added.  Each Johnson edge contributes one
q1 color occurrence.  Therefore the half-\(\ell^1\) distance between the
old and new q1 histograms is at most \(B\).  The old histogram is itself a
balanced floor/ceiling vector, so the distance of the new histogram from the
balanced set is at most \(B\).  \(\square\)

The direct Proposition 18A Hamilton order cannot satisfy the hypothesis of
Theorem 7.1.  Indeed, a block partition removes only \(B\) old edges, whereas
Proposition 5.2 requires at least

\[
d=\frac{2W}{m+2}>\frac W{2m+1}=B
\qquad(m\ge2).
\tag{7.2}
\]

Thus its SDR insertions must first be contracted, released, or internally
rewired.  Merely choosing a better cyclic offset and closing one seam per
packet cannot work.

## 8. Exact proved boundary

The following statements are unconditional.

* Proposition 18A gives exact q1 floor/ceiling balance on one Hamilton
  Johnson cycle.
* Its coordinate arrival-count discrepancy from the wreath value is
  automatically

  \[
  O\!\left(W\sqrt{\frac{\log m}{m}}\right)=o(W).
  \]

* The duplicated-color family can be made exactly point regular by that many
  abstract simple-family exchanges.
* The displayed SDR insertion creates exactly \(2W/(m+2)\) isolated local
  residence violations, forces at least that many old-edge deletions in any
  exact wreath factor, and has linear total residence-length defect.
* Once a partition into FIFO \(n\)-blocks is available, exact packetization
  and q1 overload \(O(W/m)\) follow deterministically.

The following are unproved and are not consequences of the entropy bound.

1. realizing the regularizing color exchanges inside the facet SDR;
2. preserving a spanning degree-two Johnson structure during those
   exchanges;
3. reciprocal pairing of all cut endpoints with the required old color
   tokens;
4. producing \(B\) point-regular length-\(n\) components rather than a
   general two-factor;
5. controlling FIFO residence after contracting the \(d\) inserted
   vertices;
6. completing an almost-packetized owner set to one exact factor; and
7. simultaneous fixed-window shadow balance beyond q1.

The strengthened q1 base therefore removes the marginal arrival-count gate,
but it does not remove the long-residence/reciprocal-sewing gate.

## 9. Audit of the two-facet 2-opt insertion

There is a second proposed way to insert one omitted owner which avoids the
forced singleton run of Section 5.  It is locally valid, but only after a
chord-availability test and an orientation-sign test.

Fix an omitted middle set \(Z\), and choose distinct \(a,b\in Z\).  Put

\[
S_a=Z\setminus\{a\},
\qquad
S_b=Z\setminus\{b\}.
\tag{9.1}
\]

The unexpanded saturating cycle has a unique edge of each lower color.  Write
the edges of colors \(S_a,S_b\) as

\[
A B,qquad C D.
\tag{9.2}
\]

For a facet \(S_a\), let \(p_a\) be the two extra coordinates of the two
endpoints of its core edge.  Since \(Z=S_a\cup\{a\}\) is omitted, neither
endpoint is \(Z\), so

\[
p_a\subseteq[n]\setminus Z.
\tag{9.3}
\]

Suppose

\[
p_a=\{x,y\},
\qquad
p_b=\{x,z\}
\tag{9.4}
\]

share the outside coordinate \(x\).  Name the endpoints so that

\[
\begin{aligned}
A&=S_a\cup\{y\},& B&=S_a\cup\{x\},\\
C&=S_b\cup\{z\},& D&=S_b\cup\{x\}.
\end{aligned}
\tag{9.5}
\]

The proposal deletes \(AB,CD\) and adds

\[
A Z,\qquad Z C,\qquad B D.
\tag{9.6}
\]

### Proposition 9.1 (local degree and color audit)

The four core owners \(A,B,C,D\) are distinct.  The three proposed edges in
(9.6) are Johnson edges with lower colors

\[
S_a,qquad S_b,qquad
T_{a,b,x}:=(Z\setminus\{a,b\})\cup\{x\},
\tag{9.7}
\]

respectively.  If \(BD\) is not already an edge of the retained core cycle,
then the replacement is a simple spanning two-factor on the old core owners
together with \(Z\).  Its q1 histogram keeps the colors \(S_a,S_b\) at load
one and raises \(T_{a,b,x}\) from load one to load two.

However, \(BD\) can equal the unique core edge of color
\(T_{a,b,x}\).  In that case the proposed addition is not a new simple edge,
and the local move fails: after deleting \(AB,CD\), the vertices \(B,D\)
have degree one.  Counting a second copy of \(BD\) would create a forbidden
parallel-edge component rather than a wreath factor.

#### Proof

All elements of \(p_a,p_b\) lie outside \(Z\).  Sets based on \(S_a\) omit
\(a\) and contain \(b\), while sets based on \(S_b\) contain \(a\) and omit
\(b\).  This makes every cross-pair among \(A,B\) and \(C,D\) distinct;
the two endpoints within each old edge are distinct by definition.

Direct intersections give

\[
A\cap Z=S_a,
\qquad
Z\cap C=S_b,
\qquad
B\cap D=(Z\setminus\{a,b\})\cup\{x\}.
\]

Thus all three additions are Johnson edges with the displayed colors.  When
\(BD\) is absent, every one of \(A,B,C,D\) loses one incident edge and gains
one, while \(Z\) gains degree two.  The edge count changes by \(-2+3=1\),
as required when one new owner is inserted.  The color ledger follows from
(9.7).

If \(BD\) is already the core edge of color \(T_{a,b,x}\), it is retained
because this color differs from \(S_a,S_b\).  A simple graph cannot add it a
second time.  Hence \(B,D\) do not recover the degree lost with \(AB,CD\).
\(\square\)

The bad chord configuration is locally possible.  The core cycle may
contain the three-edge segment

\[
A-B-D-C
\tag{9.8}
\]

with successive colors \(S_a,T_{a,b,x},S_b\).  Thus absence of \(BD\) is a
genuine additional hypothesis, not a consequence of distinct facets.
This is a local compatibility countercase; no claim is made here that a
particular published saturating-cycle construction must realize it.

### Proposition 9.2 (exact topology sign)

Orient the core Hamilton cycle.  For the edge \(AB\), record whether the
shared-\(x\) endpoint \(B\) is the head or the tail; record the analogous
sign for \(D\) on \(CD\).  Assuming the chord \(BD\) is available, the move
(9.6) gives:

* one Hamilton cycle if the two signs agree;
* two disjoint cycles if the two signs disagree.

#### Proof

Delete the two directed core edges.  If the shared-\(x\) endpoints have the
same sign, the two remaining core paths have their two heads in
\(\{B,D\}\) and their two tails in \(\{A,C\}\).  Pairing heads by \(BD\)
and tails by the subdivided connection \(A-Z-C\) joins the two paths into
one cycle.

If the signs are opposite, one remaining path has endpoints \(B,D\), while
the other has endpoints \(A,C\).  The two additions close these paths
separately.  \(\square\)

Thus degree balance and correct q1 colors do not by themselves preserve the
Hamilton base.  In a simultaneous family of moves, even the same-sign test
for every individual pair is not sufficient: interlacing 2-opt cuts can
alter the global number of components, which must be checked on the final
endpoint permutation.

### Proposition 9.3 (exact local safe-chord obstruction)

For fixed \(Z\), form the labeled multigraph \(L_Z\) on

\[
Y=[n]\setminus Z,
\qquad |Y|=m+1,
\]

whose edge labeled by \(a\in Z\) is the two-set \(p_a\).  Then \(L_Z\) has
\(m\) edges.  Some two edges of \(L_Z\) intersect.

Call an intersection witness \((a,b,x)\) **blocked** when the vertical chord

\[
(S_a\cup\{x\})(S_b\cup\{x\})
\tag{9.9}
\]

is already a core edge.  If every intersection witness is blocked, then:

1. \(L_Z\) is a simple spanning path on its \(m+1\) vertices; and
2. the core Hamilton cycle contains the alternating path formed by the
   \(m\) horizontal facet edges and the \(m-1\) vertical edges joining
   consecutive horizontal edges.

Conversely, this alternating-path configuration blocks every shared-extra
choice.  Therefore the pigeonhole proof of a shared coordinate does not
prove a usable absorber.

#### Proof

The \(m\) two-sets \(p_a\) cannot be pairwise disjoint on only \(m+1\)
points, proving the first assertion.

At the core vertex \(S_a\cup\{x\}\), the horizontal edge of color \(S_a\)
already consumes one of the two cycle degrees.  Hence this incidence can
belong to at most one blocking vertical edge.  If three labels
\(a,b,c\) had \(x\in p_a\cap p_b\cap p_c\), not all three pair witnesses
could be blocked.  Thus, under the all-blocked assumption,

\[
\deg_{L_Z}(x)\le2
\qquad(x\in Y).
\tag{9.10}
\]

Two parallel labeled edges would share both endpoints.  Blocking both
witnesses would make their two horizontal edges and two vertical edges a
closed four-cycle all of whose core vertices already have degree two.  This
would be a proper component of the core Hamilton cycle, impossible.  Hence
\(L_Z\) is simple.

Likewise, a cycle component of \(L_Z\), together with all its required
vertical blockers, would lift to a proper closed alternating component of
the core cycle.  Hence \(L_Z\) is a forest of paths.  If it has \(c\)
nonempty components and \(v\) used vertices, then

\[
m=v-c.
\]

Since \(v\le m+1\), one has \(c\le1\).  Thus \(c=1\), \(v=m+1\), and
\(L_Z\) is a spanning path.  Every adjacency of its consecutive labeled
edges must be blocked, producing the alternating core path.  The converse
is immediate.  \(\square\)

Concretely, label the spanning path by

\[
p_{a_i}=\{x_{i-1},x_i\}
\qquad(1\le i\le m).
\tag{9.15}
\]

The corresponding core segment may alternate as

\[
(S_{a_1}+x_0)-(S_{a_1}+x_1)
-(S_{a_2}+x_1)-(S_{a_2}+x_2)-\cdots
-(S_{a_m}+x_m).
\tag{9.16}
\]

Every underlying wedge shares \(x_i\), but its vertical chord is already
the intervening core edge.  Along the displayed orientation, that shared
endpoint is the head of one horizontal edge and the tail of the next, so it
also fails the equal-sign test.  This is the exact local recourse trap.

Even outside this exact obstruction, Proposition 9.2 supplies a further
sign condition.  A safe shared-extra pair need not have equal signs.
The classification is local to the displayed core/omitted-owner incidence;
it does not assert that the obstruction occurs for every choice of a global
saturating cycle.

### Proposition 9.4 (the exact 2-SDR projection and the KK ceiling)

Ignoring for the moment the shared-extra, chord, sign, and topology
conditions, one can choose two distinct facet colors for every omitted
owner, with no facet color reused, if and only if

\[
\boxed{
|\partial\mathcal A|\ge2|\mathcal A|
\quad\text{for every }\mathcal A\subseteq\mathcal E.}
\tag{9.11}
\]

This is the integral max-flow/Hall condition for a bipartite graph with
demand two on every omitted owner and capacity one on every facet color.

Lovasz--Kruskal--Katona does not prove (9.11) from the cardinality
\(|\mathcal E|=d\).  If

\[
|\mathcal A|=\binom xm
\]

in generalized-binomial notation, its bound is only

\[
|\partial\mathcal A|
\ge\binom x{m-1}
=|\mathcal A|\frac{m}{x-m+1}.
\tag{9.12}
\]

The one-SDR proof uses \(x\le2m-1\), which makes the factor in (9.12) at
least one.  To force factor two one would need

\[
x\le\frac{3m-2}{2},
\tag{9.13}
\]

which does not follow.  This is a real limitation of the inequality, not
merely a weak calculation.  For

\[
t=\left\lfloor\frac{3m}{2}\right\rfloor,
\qquad
\mathcal A=\binom{[t]}m,
\]

one has

\[
\frac{|\partial\mathcal A|}{|\mathcal A|}
=\frac{m}{t-m+1}<2,
\tag{9.14}
\]

while \(|\mathcal A|\le d\) for all sufficiently large \(m\) by Stirling's
formula: the left side grows like \(\exp(c_0m)\) for
\(c_0<\log4\), whereas \(d=\exp((\log4)m-O(\log m))\).

The example in (9.14) need not occur as a subfamily of the particular
omitted set of a saturating cycle.  It proves the precise scope statement:
KK and the size bound alone yield factor one, not factor two.  A structural
theorem about that omitted family would be needed for (9.11).

Finally, (9.11) is still only a projection of the actual absorber problem.
For every \(Z\), define admissible pairs of facets by the shared-extra,
available-chord, and equal-sign tests.  Simultaneously inserting all omitted
owners requires a matching which chooses one admissible pair per \(Z\),
uses every deleted facet color at most once, and uses every chord color
\(T_{a,b,x}\) at most once.  It is naturally a colored hypergraph matching,
not ordinary bipartite Hall.

For a collection of absorbers, the exact resource audit is:

1. the \(2d\) deleted core edges/facet colors are distinct;
2. all proposed added edges are distinct, and a chord which is already a
   core edge is either excluded or explicitly coupled to deletion of that
   same edge;
3. the \(d\) chord colors are distinct, so the final q1 loads remain one or
   two;
4. the final degree ledger is checked at shared core endpoints;
5. the final two-factor has the intended number and lengths of components;
   and
6. every final component satisfies FIFO residence.

Conditions 1--3 give the correct q1 multiplicities and local degree count.
They do not imply conditions 5--6.
