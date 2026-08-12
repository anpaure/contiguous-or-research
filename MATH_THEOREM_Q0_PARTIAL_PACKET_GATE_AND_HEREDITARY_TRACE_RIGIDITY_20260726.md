# The rank-\(q_0\) partial-packet gate and hereditary trace rigidity

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, web input,
or entropy heuristic is used.

## 0. Corrected outcome

Work in \(B_{2m}\), and put

\[
 W=\binom{2m}{m},\qquad
 0<a<b<\infty,
\tag{0.1}
\]

\[
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,\qquad
 N_q=\binom{2m}{m-q}.
\tag{0.2}
\]

All statements are for sufficiently large \(m\); in particular
\(q_0+1\le H\), since \(a<b\).

The correct integral density for the shared-prefix packet construction is
not \(W/(2m)\).  It is

\[
 \boxed{
 K=\left\lfloor\frac{N_{q_0}}{2m}\right\rfloor.}
\tag{0.3}
\]

In particular, the local central-binomial ratio estimate gives

\[
 \frac{N_{q_0}}W=e^{-a^2}+O_{a}(m^{-1/2}),
\qquad
 K=(e^{-a^2}+o(1))\frac W{2m}.
\tag{0.3a}
\]

Indeed,

\[
 \frac{N_{q_0}}W
 =\prod_{i=1}^{q_0}\frac{m-i+1}{m+i},
\qquad
 \log\frac{N_{q_0}}W
 =-\frac{q_0^2}{m}+O_a(m^{-1}),
\]

by termwise Taylor expansion, while
\(q_0^2/m=a^2+O_a(m^{-1/2})\).  This proves (0.3a).

Thus this is a constant-density partial packet design, not an almost
spanning packet factor of the middle layer.

Let \(\mathcal F\) be \(K\) labelled \(H\)-safe \(2m\)-owner packets.
Define their middle-owner collision excess

\[
 C_0(\mathcal F)
 =2mK-\left|\bigcup_{P\in\mathcal F}V(P)\right|,
\tag{0.4}
\]

and let \(M_q^-(\mathcal F),M_q^+(\mathcal F)\) be their actual lower and
upper target-hole counts at depth \(q\).  Put

\[
 \mathcal H_{[q_0,H]}(\mathcal F)
 =\sum_{q=q_0}^{H}
   \bigl(M_q^-(\mathcal F)+M_q^+(\mathcal F)\bigr).
\tag{0.5}
\]

The exact weak integral gate is

\[
 \boxed{
 C_0(\mathcal F)=o(W),
 \qquad
 \mathcal H_{[q_0,H]}(\mathcal F)=o(W).}
\tag{0.6}
\]

It gives a literal fixed-annulus word of length \(W+o(W)\).  Exact middle
ownership is unnecessary: only the collision excess is charged.  The
rounding error in (0.3) is smaller than \(2m=o(W)\).

The main new audit concerns heredity across depths.  Let

\[
 T_j=L_{j,q_0},\qquad R_j=U_{j,q_0}
\tag{0.7}
\]

be the cyclic lower and upper rank-\(q_0\) traces of one packet.  Then for
every \(d\ge0\) with \(q_0+d\le H\),

\[
 \boxed{
 L_{j,q_0+d}=\bigcap_{k=0}^{d}T_{j+k},\qquad
 U_{j,q_0+d}=\bigcup_{k=0}^{d}R_{j+k}.}
\tag{0.8}
\]

More strongly, the oriented cyclic list \((T_j)\) determines every owner
state and every transition label of the packet.  Hence it determines both
signed traces at every larger depth.  There is no hidden product-cell,
pair-frame, or SCD decoration which can be changed after a rank-\(q_0\)
packet factor has been selected.

Thus the shared-prefix structure correlates all depths **deterministically**.
The rank-\(q_0\) near-factor condition records only the first vertex
ledger; deeper coverage is the following additional hierarchy:

* rank \(q_0\): vertex coverage by the closed trace walks;
* rank \(q_0+1\): coverage by their directed edge-intersection colours;
* rank \(q_0+d\): coverage by intersection colours of directed
  \((d+1)\)-vertex paths;
* upper ranks: the dual union-path colours.

Consequently a two-stage proof—first choose a rank-\(q_0\) near-factor,
then repair deeper ranks by changing internal product frames while keeping
those ordered trace walks—is formally impossible.  All-depth path colours
must be controlled when the rank-\(q_0\) closed-walk packing is selected.
The shared prefix itself is therefore no extra combinatorial object beyond
this ordinary directed cyclic order; its only compiler role is to share
one collar among all product-cell segments.

## 1. The exact partial-packet compiler ledger

Let each packet

\[
 P=(Z_0,\ldots,Z_{2m-1})
\tag{1.1}
\]

be a simple cyclic middle-owner route which is \(H\)-safe.  Its cyclic
delay-\(H\) factor word has length

\[
 2m+2H
\tag{1.2}
\]

and covers all its lower intersections and upper unions through depth
\(H\).

Put

\[
 \rho= N_{q_0}-2mK,\qquad0\le\rho<2m.
\tag{1.3}
\]

The selected packets contain \(2mK=N_{q_0}-\rho\) owner occurrences and
have owner union of size

\[
 N_{q_0}-\rho-C_0(\mathcal F).
\tag{1.4}
\]

### Theorem 1.1 (corrected constant-density packet implication)

For every packet family \(\mathcal F\) of size (0.3), there is a literal
word covering the middle layer and the fixed annulus
\(q_0\le q\le H\) of length at most

\[
 \boxed{
 W+C_0(\mathcal F)+2HK
 +\mathcal H_{[q_0,H]}(\mathcal F).}
\tag{1.5}
\]

Consequently (0.6) implies length \(W+o(W)\).

#### Proof

Concatenate the \(K\) packet factor words.  Their total length is

\[
 K(2m+2H).
\tag{1.6}
\]

Append once every middle owner not in the union of the packet owner sets.
By (1.4), their number is

\[
 W-\bigl(2mK-C_0(\mathcal F)\bigr).
\tag{1.7}
\]

The sum of (1.6) and (1.7) is exactly

\[
 W+C_0(\mathcal F)+2HK.
\]

Finally append every missing signed annular target once.  This adds
(0.5) letters and proves (1.5).  Concatenation does not destroy internal
packet witnesses.

Since

\[
 2HK\le\frac{H}{m}N_{q_0}=O_{a,b}(W/\sqrt m)=o(W),
\tag{1.8}
\]

condition (0.6) proves the last assertion. \(\square\)

At depth \(q_0\), each packet supplies \(2m\) lower and \(2m\) upper
occurrences.  Their total mass is \(N_{q_0}-\rho\).  Therefore
\(M_{q_0}^{\pm}=o(W)\) is equivalent, up to the \(O(m)\) rounding term, to
an \(o(W)\) repeat excess in the corresponding rank-\(q_0\) occurrence
histogram.  This is the precise sense in which the packet family is a
rank-\(q_0\) near-factor.

There is an exact version at every depth.  Define

\[
 B_{q,S}^{\pm}
   =\sum_{P\in\mathcal F}b_{q,S}^{\pm}(P),
\qquad
 E_q^\pm
   =\sum_S(B_{q,S}^{\pm}-1)_+ .
\tag{1.9}
\]

Every packet has exactly \(2m\) cyclic starts, so its signed
depth-\(q\) occurrence mass is \(2m\).  Hence

\[
 \sum_S B_{q,S}^{\pm}=2mK=N_{q_0}-\rho.
\tag{1.10}
\]

If \(D_q^\pm=|\{S:B_{q,S}^{\pm}>0\}|\), then

\[
 E_q^\pm=N_{q_0}-\rho-D_q^\pm,
\qquad
 M_q^\pm=N_q-D_q^\pm.
\]

Subtracting gives the exact conservation law

\[
 \boxed{
 M_q^\pm
 =E_q^\pm-\bigl(N_{q_0}-N_q-\rho\bigr).}
\tag{1.11}
\]

Thus \(N_{q_0}-N_q-\rho\) is the forced repeat surplus at depth \(q\)
(with the harmless sign reversal \(M_{q_0}^\pm=E_{q_0}^\pm+\rho\) at
the first rank).  The aggregate-hole gate is equivalently

\[
 \sum_{q=q_0}^{H}\sum_{\sigma\in\{-,+\}}
 \left[
 E_q^\sigma-\bigl(N_{q_0}-N_q-\rho\bigr)
 \right]
 =o(W).
\tag{1.12}
\]

This is much sharper than asking for few repetitions.  For depths a
constant multiple of \(\sqrt m\) beyond \(q_0\), the forced repeat term
itself is \(\Theta_{a,b}(W)\); the allowed repeat excess must track it
with aggregate additive error \(o(W)\).

## 2. Exact heredity of cyclic traces

Write the packet transitions as

\[
 Z_{j+1}=Z_j-\{a_j\}+\{b_j\},
\tag{2.1}
\]

with cyclic indices.  Because the packet is \(H\)-safe, all coordinates
appearing in any \(H\)-edge window are distinct.

For \(0\le q\le H\), write

\[
 L_{j,q}=\bigcap_{t=0}^{q}Z_{j+t},
 \qquad
 U_{j,q}=\bigcup_{t=0}^{q}Z_{j+t}.
\tag{2.2}
\]

### Lemma 2.1 (rank-\(q_0\) trace transitions)

The lower trace states \(T_j=L_{j,q_0}\) satisfy

\[
 \boxed{
 T_{j+1}=T_j-\{a_{j+q_0}\}+\{b_j\}.}
\tag{2.3}
\]

In particular they form a closed directed Johnson walk at rank \(m-q_0\).
It is a Johnson cycle when its trace vertices are pairwise distinct.

#### Proof

Safety gives

\[
 T_j
 =Z_j\setminus\{a_j,a_{j+1},\ldots,a_{j+q_0-1}\}.
\tag{2.4}
\]

Indeed those are exactly the coordinates present at time \(j\) which are
removed during the window; inserted coordinates were absent at time \(j\)
and hence never belong to its intersection.  Similarly,

\[
 T_{j+1}
 =Z_{j+1}\setminus
   \{a_{j+1},\ldots,a_{j+q_0}\}.
\]

Substitute (2.1).  The common removed coordinates cancel, leaving (2.3).
\(\square\)

### Theorem 2.2 (oriented trace reconstruction)

The oriented cyclic list

\[
 (T_0,T_1,\ldots,T_{2m-1})
\tag{2.5}
\]

uniquely determines every transition label \(a_j,b_j\) and every owner
\(Z_j\).  Explicitly,

\[
 \{b_j\}=T_{j+1}\setminus T_j,
 \qquad
 \{a_{j+q_0}\}=T_j\setminus T_{j+1},
\tag{2.6}
\]

and

\[
 \boxed{
 Z_j=T_j\cup\{a_j,a_{j+1},\ldots,a_{j+q_0-1}\}.}
\tag{2.7}
\]

#### Proof

Equation (2.6) is immediate from (2.3).  It recovers all \(b_j\)'s and,
after the cyclic index shift by \(q_0\), all \(a_j\)'s.  Formula (2.4)
then gives (2.7). \(\square\)

Thus two packets with the same oriented lower rank-\(q_0\) trace are the
same directed owner packet.  In particular they have identical upper
traces.  They may be given different formal product-cell decompositions
or SCD names, but those decorations describe the same physical owner
route and cannot alter its target ledger.

### Theorem 2.3 (hereditary sliding-intersection identity)

For every \(d\ge0\) with \(q_0+d\le H\), equation (0.8) holds.

#### Proof

By definition,

\[
 T_{j+k}=\bigcap_{t=k}^{k+q_0}Z_{j+t}.
\]

As \(k\) runs from \(0\) to \(d\), the index intervals
\([k,k+q_0]\) have union \([0,q_0+d]\).  Intersecting the \(T_{j+k}\)'s
therefore gives

\[
 \bigcap_{k=0}^{d}T_{j+k}
 =\bigcap_{t=0}^{q_0+d}Z_{j+t}
 =L_{j,q_0+d}.
\]

The union identity is identical with intersections replaced by unions.
\(\square\)

### Corollary 2.4 (nested home flags)

Every rank-\(q_0\) start \(j\) carries the two nested flags

\[
 \boxed{
 L_{j,q_0+d}
 =T_j\setminus
   \{a_{j+q_0},a_{j+q_0+1},\ldots,a_{j+q_0+d-1}\},}
\tag{2.8}
\]

\[
 \boxed{
 U_{j,q_0+d}
 =R_j\cup
   \{b_{j+q_0},b_{j+q_0+1},\ldots,b_{j+q_0+d-1}\}.}
\tag{2.9}
\]

All displayed coordinates are distinct over the relevant window.

#### Proof

Relative to the window defining \(T_j\), extending its right endpoint by
\(d\) transitions removes exactly the next \(d\) coordinates present at
time \(j\).  Safety says none was changed earlier in that window, giving
(2.8).  Dually, extending the union window inserts exactly the next
\(d\) new coordinates, giving (2.9). \(\square\)

Thus an exact rank-\(q_0\) occurrence factor would assign one complete
ordered deletion/addition flag to every rank-\(q_0\) target, not merely
one depth-\(q_0\) vertex.  If the rank-\(q_0\) hole count is \(o(W)\),
then (1.11) shows that all but \(o(W)\) rank-\(q_0\) targets have exactly
one home occurrence.  Their higher-depth images are nevertheless fixed
by their home flags and need not be distinct.

There is also a quantitative warning.  Quarantining \(r\) exceptional
rank-\(q_0\) starts by discarding their complete flags can affect as many
as

\[
 2r(H-q_0+1)
\tag{2.10}
\]

signed annular occurrences.  Hence a proof which first builds a
rank-\(q_0\) near-factor and then simply quarantines its exceptional
starts needs \(r=o(W/H)\), not merely \(r=o(W)\).  This is a limitation
of that two-stage proof strategy, not a lower bound on the optimum of the
joint program (4.3).

### Corollary 2.5 (no hidden-decoration repair)

Fix the oriented rank-\(q_0\) trace walks of a selected packet family.
Changing product-cell decompositions, coordinate-pair labels, local SCD
names, or compiler frames without changing those trace walks cannot
change a single target occurrence at any depth \(q_0\le q\le H\), on
either sign.

This is a literal statewise obstruction to post-selection depth repair.
It is important that the trace is oriented.  An unordered rank-\(q_0\)
vertex near-factor may still admit several legal cyclic orderings, and
choosing among those orderings is genuine remaining freedom.  Once those
orders—and hence the packet columns—are fixed, no further frame freedom
remains.

### Proposition 2.6 (interval normal form for the shared-prefix packet)

For the explicit shared-prefix packet, write its coordinate pairs as
\(e_i=\{u_i,v_i\}\), cyclically ordered by \(i\in\mathbb Z/m\mathbb Z\).
The transition supports occur in the order

\[
 e_0,e_1,\ldots,e_{m-1},e_0,e_1,\ldots,e_{m-1}.
\tag{2.11}
\]

Let \(I_{j,q}\) be the \(q\) consecutive pair supports beginning at the
transition out of \(Z_j\).  Then

\[
 L_{j,q}\cap e_i=
 \begin{cases}
  \varnothing,&e_i\in I_{j,q},\\
  Z_j\cap e_i,&e_i\notin I_{j,q},
 \end{cases}
\tag{2.12}
\]

and

\[
 U_{j,q}\cap e_i=
 \begin{cases}
  e_i,&e_i\in I_{j,q},\\
  Z_j\cap e_i,&e_i\notin I_{j,q}.
 \end{cases}
\tag{2.13}
\]

In particular, increasing depth from \(q_0\) to \(q_0+d\) extends one
cyclic interval by \(d\) pair supports.  A product-cell decomposition
only marks cuts in (2.11); it neither changes the interval nor creates a
new continuation choice at a cut.

#### Proof

During the \(q\)-edge window, each pair in \(I_{j,q}\) is flipped once.
Its old coordinate is absent after the flip and its new coordinate was
absent before the flip, so the intersection contains neither and the
union contains both.  Every other pair is unchanged and contributes its
unique owner coordinate to both.  This proves (2.12)--(2.13). \(\square\)

## 3. The exact path-colour hierarchy

Let \(\mathcal T_{q_0}\) be the rank-\((m-q_0)\) target layer.  For a
rank-\((m-q_0-d)\) target \(S\), define its up-set in the trace layer by

\[
 \mathcal U_S
 =\{T\in\mathcal T_{q_0}:S\subseteq T\}.
\tag{3.1}
\]

### Theorem 3.1 (lower path-hitting formulation)

A selected packet covers \(S\) at depth \(q_0+d\) if and only if its
rank-\(q_0\) trace contains a directed consecutive path

\[
 T_j,T_{j+1},\ldots,T_{j+d}
\tag{3.2}
\]

inside \(\mathcal U_S\) whose intersection is \(S\).

For an \(H\)-safe packet the intersection automatically has rank
\(m-q_0-d\); hence containment in \(\mathcal U_S\) already forces that
intersection to equal \(S\).

#### Proof

Theorem 2.3 identifies the depth-\((q_0+d)\) occurrence with the
intersection of (3.2).  This proves both directions.  The rank assertion
follows from \(H\)-safety. \(\square\)

The induced graph on \(\mathcal U_S\) is a Johnson graph on

\[
 n'=2m-|S|=m+q_0+d
\]

available coordinates, with vertex rank \(d\).  Every legal path in
(3.2) is a length-\(d\) geodesic: it deletes \(d\) distinct coordinates
of \(T_j\setminus S\) and inserts \(d\) distinct coordinates outside
\(T_j\).  Conversely every such geodesic has total intersection \(S\).
Consequently the exact number of oriented local trace paths with colour
\(S\), before imposing extension to a complete packet, is

\[
 \boxed{
 (m+q_0+d)_{2d}.}
\tag{3.3}
\]

Indeed, choose the ordered deletion list and then the disjoint ordered
insertion list.  This large local census is only a candidate reservoir:
the \(2m\) cyclic windows of one packet are tied together by Theorem 2.2.

The upper version is dual.  Put

\[
 \mathcal R_{q_0}=\binom{[2m]}{m+q_0},
 \qquad
 \mathcal D_U=\{R\in\mathcal R_{q_0}:R\subseteq U\}.
\tag{3.4}
\]

A rank-\((m+q_0+d)\) set \(U\) is covered if and only if one selected
upper trace contains \(d+1\) consecutive vertices in \(\mathcal D_U\)
whose union is \(U\).

For the complement-antipodal shared-prefix packets of the explicit
catalogue,

\[
 L_{j+m,q}=U_{j,q}^{\,c}.
\tag{3.5}
\]

Consequently their complete lower and upper occurrence histograms are
complementary, packet by packet, and

\[
 \boxed{M_q^+(\mathcal F)=M_q^-(\mathcal F)}
\tag{3.6}
\]

for every selected family from that catalogue.  The two signs therefore
do not create two independent rounding problems.

At \(d=0\), this is vertex coverage.  At \(d=1\), the lower target colours
are

\[
 T_j\cap T_{j+1},
\tag{3.7}
\]

so the new condition is edge-colour coverage.  At general \(d\), the
colours belong to directed length-\(d\) paths.  A rank-\(q_0\) near-factor
controls only the vertex ledger.  It supplies no separate variable with
which to alter the edge and path colours after the oriented walks have
been fixed.

## 4. Exact integral partial-design program

Let \(\mathscr P_m\) be the labelled catalogue of complement-antipodal
shared-prefix packets.  The weak integral gate is exactly the following
finite \(0\)-\(1\) covering program.  Introduce \(x_P\in\{0,1\}\), owner
coverage variables \(0\le y_X\le1\), and target coverage variables
\(0\le z_{q,S}^{\pm}\le1\), subject to

\[
 \sum_{P\in\mathscr P_m}x_P=K,
\tag{4.1}
\]

\[
 y_X\le\sum_P a_X(P)x_P,
\qquad
 z_{q,S}^{\pm}\le\sum_P b_{q,S}^{\pm}(P)x_P.
\tag{4.2}
\]

Minimize

\[
 \Phi_m(x,y,z)
 =
 2mK-\sum_Xy_X
 +\sum_{q=q_0}^{H}\sum_{\sigma\in\{-,+\}}\sum_S
   (1-z_{q,S}^{\sigma}).
\tag{4.3}
\]

For fixed integral \(x\), an optimum makes each \(y\) and \(z\) the
indicator that its object is covered.  Therefore

\[
 \boxed{
 \min\Phi_m
 =\min_{\substack{\mathcal F\subseteq\mathscr P_m\\|\mathcal F|=K}}
   \left[
    C_0(\mathcal F)+
    \mathcal H_{[q_0,H]}(\mathcal F)
   \right].}
\tag{4.4}
\]

For the antipodal catalogue, (3.6) permits replacing the signed target
sum by twice the lower-target sum.  Theorem 2.2 projects (4.1)--(4.3)
without loss onto admissible oriented rank-\(q_0\) trace walks:
owner incidences are reconstructed by (2.6)--(2.7), while every deeper
coefficient is the path colour in (0.8).

Thus the exact constant-density question is

\[
 \boxed{\min\Phi_m=o(W).}
\tag{4.5}
\]

This formulation isolates the genuine joint variable: the cyclic ordering
of the rank-\(q_0\) trace vertices.  It contains no later product-cell or
depthwise choice.

## 5. Corrected fractional normalization

For completeness, the complete coordinate orbit of one packet has the
constant fractional weight

\[
 \vartheta_m
 =\frac{N_{q_0}}{(2m)!\,2m},
\tag{5.1}
\]

not the owner-saturating weight \(W/((2m)!\,2m)\).

The orbit double count gives:

\[
 \sum_P\vartheta_m b_{q_0,T}^{\pm}(P)=1
\quad\text{for every signed rank-\(q_0\) target},
\tag{5.2}
\]

\[
 \sum_P\vartheta_m b_{q,S}^{\pm}(P)
 =\frac{N_{q_0}}{N_q}\ge1
\quad(q_0\le q\le H),
\tag{5.3}
\]

and

\[
 \sum_P\vartheta_m a_X(P)=\frac{N_{q_0}}W<1
\quad\text{for every middle owner}.
\tag{5.4}
\]

The total fractional packet count is \(N_{q_0}/(2m)\).  After adding the
unused fractional middle-owner mass, its cost is

\[
 W+\frac HmN_{q_0}=W+O_{a,b}(W/\sqrt m).
\tag{5.5}
\]

These identities explain the corrected density but do not solve the
integral design; they are only the old symmetric fractional point and
carry no rounding claim.

## 6. Exact remaining partial-design problem

The integral object is now unambiguous:

> Select \(K=\lfloor N_{q_0}/(2m)\rfloor\) labelled
> complement-antipodal shared-prefix packets so
> that:
> 1. their middle collision excess \(C_0\) is \(o(W)\);
> 2. their lower and upper rank-\(q_0\) traces are near-factors; and
> 3. the sliding intersection/union path colours in (0.8) have aggregate
>    holes \(o(W)\) through \(H\).

Condition 2 is already included in condition 3 at \(q=q_0\), but is
displayed because it is the natural first matching problem.

Theorems 2.2--2.3 show the exact sequencing constraint: after the oriented
rank-\(q_0\) trace walks are chosen, every deeper column is frozen.  Therefore
the problem is not:

\[
 \text{rank-\(q_0\) matching}
 \quad+\quad
 \text{independent deeper-depth rounding}.
\]

It is one coloured closed-walk packing problem whose colours are all directed
path intersections and unions of lengths \(1,\ldots,H-q_0+1\).

## 7. Status

Proved here:

1. the corrected constant-density compiler ledger with
   \(K=N_{q_0}/(2m)+O(1)\);
2. the exact owner-collision rather than exact-owner gate;
3. the exact hole/forced-repeat conservation identity at every depth;
4. reconstruction of the entire packet from its oriented rank-\(q_0\)
   lower trace;
5. deterministic sliding intersection/union heredity and nested home
   flags at every larger
   depth;
6. the explicit interval normal form across product-cell cuts;
7. the exact up-set/down-set path-hitting formulation and local geodesic
   census;
8. the \(o(W/H)\) rate required by any blind exceptional-flag
   quarantine; and
9. the exact integral \(0\)-\(1\) partial-design program.

Not proved here:

1. an integral rank-\(q_0\) packet near-factor;
2. aggregate all-depth holes \(o(W)\) after such a near-factor;
3. a deterministic switch or absorber preserving all path colours; or
4. coefficient one.

The audit gives a sharp answer to the correlation question.  Shared
prefixes correlate all depths completely, not weakly: deeper traces are
functions of the ordered rank-\(q_0\) trace walk.  This removes hidden
continuation freedom and rules out a two-stage repair by changing
product-cell decorations after the packet walks have been fixed.  It does
not prove that every rank-\(q_0\) near-factor has bad deeper colours.
The remaining positive task is to choose the constant-density
rank-\(q_0\) packet walks with their entire path-colour profile already
balanced.
