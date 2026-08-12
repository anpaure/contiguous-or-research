# The top MSW component: exact owner-star lift, global dependency collapse, and the lag-\(H\) braid gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

> **Audited correction to the chronology claim.**  The exact owner-star
> lift, the \(5/16\) top-component bound, the global dependency
> collapse, the cut-only \(5/8\) collar toll, and the lag-\(H\) gate in
> this file are valid.  The one-row staircase \((L-d)_+\) is also valid.
> Outcome item 5 and Section 8's aggregate \(1/64\) Hall cut are only
> conditional on simplicity for *all cyclic \(m\)-windows*.  An
> infinity-cut MSW/\(C_8\) factor is merely primary-owner-simple; every
> nonport target also occurs cyclically in the row primarily owning its
> complement.  The unconditional cyclic multiplicity is two, adding a
> factor two to (0.12)/(8.10) and making the shallow cut vacuous.  Hence
> the actual complement-paired common-row lift remains open.  See
> MATH_THEOREM_K_CATALAN_PROMOTION_CROSS_INTERFACE_AND_CHRONOLOGY_CUT_20260726.md
> for the corrected statement and exact scope.

## 0. Outcome

Put

\[
 V=[2m],\qquad
 W=\binom{2m}{m},\qquad
 B=C_m=\frac{W}{m+1},
\tag{0.1}
\]

and take the critically calibrated promotion height

\[
 H^2/m=\log m+o(1),\qquad
 M=m+H,\qquad
 N_H=\binom{2m}{m-H},
\tag{0.2}
\]

so that

\[
 \frac{MN_H}{W}=1+o(1),\qquad N_H=(1+o(1))B.
\tag{0.3}
\]

Let \(F_m\) be the canonical anchored MSW/PBBS factor, cut at infinity,
and compare it with \(\tau F_m\), \(\tau=(2\ 3)\).  Its ownership
components are the exact Catalan hierarchy.  The unique top component has
shore size

\[
 b_{\rm top}=C_{m-2}+C_{m-1}
             =\left(\frac5{16}+o(1)\right)B.
\tag{0.4}
\]

This report proves one positive interface theorem, four exact
obstructions, and one sharp conditional chronology test.

1. **Exact owner-star lift.**  Every incidence

   \[
   A\subset D,\qquad |A|=m-H,\quad |D|=m,
   \tag{0.5}
   \]

   has a literal promotion-frame witness obtained by restricting the
   unique MSW row which owns \(D\).  If \(D\)'s owner lies in component
   \(K\), then the two shores of \(K\) give two such witnesses,
   coherently for every \(A\in\binom D{m-H}\).  Thus every complete
   provider star is exactly monochromatic at the component-resource
   level, not merely almost monochromatic.

2. **The unique top component is insufficient by itself.**  Its primary
   target block has exact size

   \[
   |\Omega_{\rm top}|=(m+1)b_{\rm top}
      =\left(\frac5{16}+o(1)\right)W.
   \tag{0.6}
   \]

   Hence the canonical lift from this component supplies precisely those
   target stars, only \(5/16+o(1)\) of all stars.  More generally, any
   injective assignment of its rows to promotion roots can be
   \((1-\varepsilon)\)-dominant in at most

   \[
   \left(\frac{5}{16(1-\varepsilon)}+o(1)\right)W
   \tag{0.7}
   \]

   root stars.  Therefore the unique top component cannot be the sole
   correlation block required by the block-factor theorem.

3. **Exact component-locality collapses globally.**  Colour every middle
   target by its MSW ownership component.  Join a promotion root \(A\)
   to component \(K\) whenever some target \(D\supset A\) has colour
   \(K\).  This bipartite graph is connected.  Consequently, if every
   star is controlled by its owner component as in the exact lift, the
   transitive dependency block contains every promotion root and every
   MSW component.  Independent Catalan component bits cannot implement
   the lift; they must be merged into one global coupling.

4. **Cut-only physical inheritance has a linear toll.**  The top
   component carries \((m+1)b_{\rm top}\) consecutive owner positions.
   A consecutive piece assigned without rethreading to one fixed
   \((m+H)\)-top has length at most \(H+1\).  Thus it creates at least

   \[
   p_{\rm top}\ge
   \frac{(m+1)b_{\rm top}}{H+1}
   =\left(\frac5{16}+o(1)\right)\frac WH
   \tag{0.8}
   \]

   pieces and pays collar toll

   \[
   2Hp_{\rm top}\ge\left(\frac58-o(1)\right)W.
   \tag{0.9}
   \]

   Hence a successful use of the top component must perform
   \(\Theta(W/H)\) cross-row rethreading splices.  The exact splice
   equations are the lag-\(H\) identities from the mechanical
   clone--Hall atlas.

5. **The common-chronology staircase cut is conditional, and the
   natural owner lift fails nested provenance much earlier.**  For a
   cyclic-\(m\)-window-simple ambient row family, the exact staircase law
   gives

   \[
      C_d\le MN_H\left(1-\frac d{H+1}\right)
   \]

   and, under \((M-1)N_H\le W\), the former \(1/64\) aggregate
   deficiency.  An infinity-cut MSW factor does **not** satisfy that
   premise: ports have cyclic multiplicity one and nonports multiplicity
   two.  The unconditional replacement has a factor two and is vacuous
   in the shallow band.

   There is nevertheless an exact obstruction for the canonical
   owner-row lift itself.  For one primary target \(D\), exactly

   \[
                 \binom{m-d}{H-d}
   \]

   of its \(\binom mH\) compatible roots inherit the full oriented
   radius-\(d\) flag from that same owner row.  The fraction is
   \((H)_d/(m)_d\); even granting both component shores gives at most
   twice this.  At \(d=1\) this is at most \(2H/m=o(1)\).

The positive owner-star lift resolves targetwise component alignment at
the level of individual middle clones.  Its same-owner nested extension
has density \(o(1)\) already at depth one.  The factor-wide staircase
argument does not close the remaining escape because of exact cyclic
multiplicity two.  The sole remaining object is a global noncellular
multirow braid which groups the lifted clones into common cyclic orders
while satisfying the lag-\(H\) equations and retaining \(o(W)\)
aggregate holes at all protected depths.

## 1. Primary owner partition after the infinity cut

Rotate an anchored odd row to put infinity first and delete it.  Write the
resulting cyclic order as

\[
                         \pi_x=(a_{x,1},\ldots,a_{x,2m}).
\tag{1.1}
\]

Its \(m+1\) nonwrapping middle windows are

\[
 P_{x,j}=\{a_{x,j},a_{x,j+1},\ldots,a_{x,j+m-1}\},
 \qquad 1\le j\le m+1.
\tag{1.2}
\]

Exact anchored ownership gives the disjoint partition

\[
 \boxed{
 \{P_{x,j}:x\in D_m,\ 1\le j\le m+1\}
       =\binom Vm.}
\tag{1.3}
\]

For \(D\in\binom Vm\), let

\[
                         x_F(D)
\tag{1.4}
\]

be its unique primary owner row in \(F_m\).  The target \(D\) is a
literal consecutive \(m\)-block in \(\pi_{x_F(D)}\).

If \(K\) is one ownership component between \(F_m\) and \(\tau F_m\),
its two shores contain the same complete \(X/Y\)-resource block.  In
particular, their primary \(X\)-targets form one common set

\[
                         \Omega_K\subseteq\binom Vm,
\tag{1.5}
\]

and

\[
                         |\Omega_K|=(m+1)|K|,
\tag{1.6}
\]

where \(|K|\) denotes the row count on one shore.  The sets
\(\Omega_K\) partition \(\binom Vm\).

For the unique top hierarchy component, (1.6) and (0.4) prove (0.6).

## 2. Every provider incidence has a literal owner-row witness

Fix \(D\in\binom Vm\) and a compatible promotion root

\[
 A\in\mathcal R(D):=\binom D{m-H}.
\tag{2.1}
\]

Put

\[
 U=A^c,\qquad J=D\setminus A.
\tag{2.2}
\]

Then \(|U|=M\), \(|J|=H\), and \(J\subset U\).

### Theorem 2.1 (canonical owner-star lift)

Let \(\pi_D=\pi_{x_F(D)}\), and restrict its cyclic order to \(U\):

\[
                         \Phi_F(A,D):=\pi_D|_U.
\tag{2.3}
\]

Then \(J=D\setminus A\) is a cyclic length-\(H\) interval in
\(\Phi_F(A,D)\).  Consequently

\[
                         D=A\cup J
\tag{2.4}
\]

belongs to the promotion deck rooted at \(A\).

If \(D\in\Omega_K\), the owner row on the other shore of \(K\) gives a
second witness \(\Phi_{\tau F}(A,D)\).  Both witnesses exist for every
\(A\in\mathcal R(D)\), and the shore choice is one common component bit
over the whole star.

#### Proof

The set \(D\) is one consecutive \(m\)-block of \(\pi_D\).  Passing from
\(\pi_D\) to \(\pi_D|_U\) deletes precisely the labels in \(A\), all of
which lie inside that block.  Its surviving labels are \(D\setminus A=J\).
No label of \(D^c\) can appear between two surviving labels of the old
block, so \(J\) is consecutive in the restricted cyclic order.  This
proves (2.4).

The other component shore owns exactly the same primary resource \(D\)
in one of its rows.  Applying the same argument gives the second witness.
The component switch chooses that shore simultaneously for every resource
in \(\Omega_K\), hence simultaneously over every incidence in
\(\mathcal R(D)\). \(\square\)

Every \(\Phi_F(A,D)\) is a complete labelled cyclic order.  Therefore its
shorter and longer intervals form a nested, chronologically literal
*promotion* frame.  The theorem is stronger than a profile or Hall edge:
it gives a full promotion-frame witness for each individual
source--target incidence.  It does **not** say that all those shorter and
longer intervals remain windows of the ambient owner row.  That stronger
provenance assertion is exactly what fails in Section 8.

It is weaker than a frame selection.  Different targets
\(D,E\supset A\) generally give different orders
\(\Phi_F(A,D)\) and \(\Phi_F(A,E)\).  One promotion root may use only one
of them.

### Theorem 2.2 (exact nested-provenance loss in the natural lift)

Fix a primary owner row of \(D\), rotate it cyclically to

\[
 \pi=(d_1,\ldots,d_m,e_1,\ldots,e_m),
 \qquad D=\{d_1,\ldots,d_m\},\quad D^c=\{e_1,\ldots,e_m\}. \tag{2.5}
\]

For \(A\in\binom D{m-H}\), put \(J=D\setminus A\), list \(J\) in the
\(d\)-order as \(j_1,\ldots,j_H\), and let \(U=A^c\).  Then

\[
 \pi|_U=(j_1,\ldots,j_H,e_1,\ldots,e_m).                \tag{2.6}
\]

Use the oriented fixed-start promotion flag whose middle complement is
\(D^c\): its rank-\((m+r)\) member is the interval of (2.6) starting at
\(e_1\) and having length \(m+r\).  For \(0\le d\le H\), the whole flag
through radii \(-d,\ldots,d\) consists of ambient intervals of \(\pi\)
if and only if

\[
 T_d:=\{d_1,\ldots,d_d\}\subseteq J
 \quad\Longleftrightarrow\quad A\cap T_d=\varnothing.   \tag{2.7}
\]

Consequently the exact good-root count in the complete target star is

\[
 \boxed{
 |\mathcal G_\pi(D,d)|
   =\binom{m-d}{m-H}
   =\binom{m-d}{H-d},\qquad
 \frac{|\mathcal G_\pi(D,d)|}{\binom mH}
   =\frac{(H)_d}{(m)_d}.}                               \tag{2.8}
\]

#### Proof

For \(r\le0\), the fixed-start member is

\[
                         \{e_1,\ldots,e_{m+r}\},
\]

and is automatically an interval of \(\pi\).  For \(r\ge0\), it is

\[
                         D^c\cup\{j_1,\ldots,j_r\}.      \tag{2.9}
\]

This is the length-\((m+r)\) interval of \(\pi\) starting at \(e_1\) if
and only if \(j_t=d_t\) for \(1\le t\le r\).  Requiring this for every
\(r\le d\) is exactly (2.7).  Once \(T_d\) is forced into \(J\), its
remaining \(H-d\) elements can be chosen arbitrarily from the other
\(m-d\) labels of \(D\), giving (2.8). \(\square\)

Reverse orientation replaces \(T_d\) by the terminal \(d\)-block and
does not change the count.  For the fixed canonical orientations of the
two component shores let their boundary blocks be \(T_d^0,T_d^1\), put
\(u=|T_d^0\cup T_d^1|\), and use the convention that a binomial
coefficient is zero when its lower argument exceeds its upper argument.
Then inclusion--exclusion gives the exact two-witness atlas size

\[
 |\mathcal G_0\cup\mathcal G_1|
 =2\binom{m-d}{m-H}-\binom{m-u}{m-H}
 \le2\binom{m-d}{m-H}.                                 \tag{2.10}
\]

The two good-root sets need not be disjoint.  A legal component shore bit
uses one set, not their targetwise union.  Even granting the union, at
depth one its star density is at most

\[
                         \frac{2H}{m}=o(1).              \tag{2.11}
\]

If reversal is granted as an additional independent choice for each
shore, the crude ceiling becomes \(4H/m=o(1)\).  Thus the conclusion is
unchanged, while (2.10) is the exact formula for the fixed oriented
two-shore atlas.

Thus Theorem 2.1 is an exact complete promotion-order witness and a
one-phase ambient certificate, but its natural same-owner continuation
is not near-monochromatic for nested chronology.  This is a statewise
obstruction to the owner-row lift itself, not to a braid which changes
ambient rows between depths or selects a different owner source.

## 3. Exact colouring of the mechanical clone graph

Fix the mechanical atlas of
MATH_THEOREM_GLOBAL_PROMOTION_MECHANICAL_ATLAS_AND_CLONE_HALL_20260726.md.
Its middle clone graph has left vertices \((A,i)\), one for each root and
phase, and right vertices \(D\in\binom Vm\).  An edge means that some
mechanical labelling at root \(A\) puts target \(D\) at phase \(i\).

Colour every right target and every incident clone edge by

\[
                         \kappa(D)=K
 \quad\Longleftrightarrow\quad D\in\Omega_K.
\tag{3.1}
\]

Then every target star is exactly monochromatic: all edges ending at
\(D\), over every compatible root and phase, have colour \(\kappa(D)\).
The exact clone--Hall matching of size \(W-o(W)\) remains valid after this
colouring, because no edge has been removed.

The colour does not itself turn a mechanical edge into the restricted
owner-row witness (2.3).  A target-dependent relabelling can always align
one witness with one permitted mechanical cell when their
\(P/P^c\)-counts agree, but such a relabelling conjugates the ambient
factor and depends on \((A,D)\).  It is not one common component
conjugation.  Thus (3.1) is an exact resource provenance atlas, not yet a
physical component action on the mechanical frames.

## 4. Why the unique top component cannot suffice

The canonical owner-star lift from the top component reaches exactly the
targets in \(\Omega_{\rm top}\).  Formula (0.6) proves that this is only
\(5/16+o(1)\) of the middle layer.

There is also an assignment-independent double-count bound.  Let
\(\mathcal B\subseteq\binom V{m-H}\) be any block of \(b\) promotion
roots.  Every root lies in exactly

\[
                         L=\binom{m+H}{H}
\tag{4.1}
\]

middle target stars, while every target star has size

\[
                         R=\binom mH.
\tag{4.2}
\]

The regular-incidence identity is

\[
                         N_HL=WR.
\tag{4.3}
\]

If \(\mathcal T_\varepsilon(\mathcal B)\) is the family of targets
whose stars have at least \((1-\varepsilon)R\) roots in \(\mathcal B\),
then

\[
\begin{aligned}
 (1-\varepsilon)R|\mathcal T_\varepsilon(\mathcal B)|
 &\le\sum_D|\mathcal B\cap\mathcal R(D)|\\
 &=bL.
\end{aligned}
\tag{4.4}
\]

Using (4.3),

\[
 \boxed{
 |\mathcal T_\varepsilon(\mathcal B)|
 \le\frac{b}{(1-\varepsilon)N_H}W.}
\tag{4.5}
\]

An injective use of the top component has

\[
 \frac b{N_H}=\frac5{16}+o(1),
\tag{4.6}
\]

and (0.7) follows.  This theorem permits unrestricted placement of those
roots; it is not tied to the natural MSW labels.

The injectivity qualification is essential.  Reusing one ambient row as
a restriction witness at many promotion roots can exceed (4.6), but then
the uses are not disjoint ambient certificates and their common owner
resources must be reconciled by the missing global braid.

## 5. Exact global dependency collapse

Define a bipartite graph \(\mathfrak G\) with vertex classes

\[
 \mathcal A=\binom V{m-H},
 \qquad
 \mathcal K=\{\text{MSW ownership components}\}.
\tag{5.1}
\]

Join \(A\in\mathcal A\) to \(K\in\mathcal K\) if

\[
 \text{there exists }D\in\Omega_K\text{ with }A\subset D.
\tag{5.2}
\]

### Theorem 5.1 (component--root incidence is connected)

For every \(1\le H<m\), the graph \(\mathfrak G\) is connected.

#### Proof

The Johnson graph on \(\binom V{m-H}\) is connected.  Let adjacent roots
\(A,A'\) differ by one exchange.  Then

\[
                         |A\cup A'|=m-H+1\le m.
\tag{5.3}
\]

Extend \(A\cup A'\) to an \(m\)-set \(D\).  The primary partition places
\(D\) in a unique \(\Omega_K\).  Then (5.2) gives the two-edge path

\[
                         A-K-A'
\tag{5.4}
\]

in \(\mathfrak G\).  Connectivity of the Johnson graph puts all root
vertices in one component of \(\mathfrak G\).

Every \(K\in\mathcal K\) owns a nonempty set \(\Omega_K\).  Choose
\(D\in\Omega_K\) and any \(A\in\binom D{m-H}\); then \(A-K\) is an
edge.  Thus every component vertex lies in the same connected component.
\(\square\)

### Corollary 5.2 (no independent-component owner-star compiler)

Suppose every incidence \(A\subset D\) is controlled by the shore bit of
\(\kappa(D)\), as in the exact owner-star lift.  If two promotion roots
or MSW components joined in \(\mathfrak G\) must belong to the same
dependency block, then there is exactly one dependency block.

Thus the complete owner-star lift is compatible with the
superpolynomial block theorem only in its fully global escape.  It cannot
be rounded by independent MSW hierarchy components, including the unique
top component as one independent block.

This is a dependency theorem, not a nonexistence theorem.  A diagonal law
which correlates all component bits lies outside the block-product
obstruction.

## 6. Cut-only conversion pays a linear collar

One cut MSW row has the complementary Johnson path

\[
 X_0,X_1,\ldots,X_m.
\tag{6.1}
\]

For every segment of \(\ell\) consecutive owners,

\[
 \left|\bigcup_{i=a}^{a+\ell-1}X_i\right|
                         =m+\ell-1.
\tag{6.2}
\]

Indeed the path is a geodesic: its successive exchanges remove distinct
old coordinates and insert distinct new coordinates.  Every new owner
adds one fresh coordinate to the union.

If this unchanged segment is assigned to one promotion top \(U\) of size
\(m+H\), (6.2) forces

\[
                         \ell\le H+1.
\tag{6.3}
\]

The top component contains \(b_{\rm top}\) such paths and
\((m+1)b_{\rm top}\) primary owner positions.  Partitioning them into
unchanged fixed-top pieces therefore gives

\[
 p_{\rm top}\ge
 \left\lceil\frac{(m+1)b_{\rm top}}{H+1}\right\rceil,
\tag{6.4}
\]

which is (0.8).  Every independently compiled piece has the standard
two-sided collar \(2H\), proving (0.9).

To reduce the component count to \(o(W/H)\), a construction must add
\[
                         \Theta(W/H)
\tag{6.5}
\]

legal cross-row splices between pieces.  This is precisely the nonlocal
braid absent from cut-only inheritance.

## 7. The exact lag-\(H\) statewise gate

At one promotion root \(A\), let the assigned middle targets be

\[
                         D_i=A\cup J_i,
 \qquad J_i\in\binom{A^c}{H},
 \qquad i\in\mathbb Z_M.
\tag{7.1}
\]

The mechanical clone matching chooses the \(D_i\)'s independently.  They
come from one common cyclic frame if and only if, after filling the one
deleted phase in a repaired ring,

\[
 |J_i\cap J_{i+1}|=H-1
\tag{7.2}
\]

for every \(i\), the singletons

\[
                         x_i=J_i\setminus J_{i+1}
\tag{7.3}
\]

are all distinct and exhaust \(A^c\), and

\[
 \boxed{
 J_{i+1}\setminus J_i
   =J_{i+H}\setminus J_{i+H+1}
 \qquad(i\in\mathbb Z_M).}
\tag{7.4}
\]

These are necessary and sufficient: (7.4) says that the label inserted
at transition \(i\) is the label deleted \(H\) phases later.  The cyclic
order is then

\[
                         (x_0,x_1,\ldots,x_{M-1}).
\tag{7.5}
\]

The owner-star lift proves that every individual pair \((A,D_i)\) has a
full literal witness and the clone--Hall theorem proves a near-perfect
phasewise matching.  Neither theorem couples the choices so that
(7.2)--(7.4) hold simultaneously.  Corollary 5.2 shows that enforcing
them through MSW owner components is necessarily a global, rather than
component-product, problem.

There is a final useful action ceiling.  If a covariant rootwise mapping
sends the two shores of the top component to frame systems which differ
at each \(\tau\)-invariant top only by the coordinate transposition
\(\tau\), then at most \(2H\) length-\(H\) windows of one frame change.
Indeed, the starts of windows containing either transposed coordinate
form two cyclic intervals of length \(H\), and only their symmetric
difference changes.  Therefore the total middle histogram action over
all \(N_H\) roots is at most

\[
                         2HN_H=O(WH/m)=o(W).
\tag{7.6}
\]

Thus a covariant two-shore image cannot repair a pre-existing
\(\Omega(W)\) mechanical grouping defect.  This does not obstruct a
baseline whose defect is already \(o(W)\), nor a noncovariant global
braid using many component states.

## 8. The conditional common-chronology cut and its MSW correction

The owner-star lift supplies a different restricted order for each
incidence.  This section proves that those orders cannot be grouped by
the most direct rule: choose one order at each promotion top and inherit
every protected depth from ambient rows which restrict to that complete
order.

The applicability premise is essential.  The staircase capacity below
holds with coefficient one only for a row family in which every cyclic
\(m\)-window occurs in at most one row.  An infinity-cut exact MSW factor
is exact only for its designated primary windows; its complete cyclic
middle catalogue has multiplicity two on every nonport.  Therefore the
coefficient-one and \(1/64\) conclusions in this section are conditional
and do not apply automatically to a completed MSW factor or to one
Catalan component shore.

Fix a top \(U\in\binom V M\), put \(A=V\setminus U\), and write the
desired cyclic order as

\[
                         \sigma=(u_0,u_1,\ldots,u_{M-1}). \tag{8.1}
\]

Let \(\pi\) be an ambient cyclic row on \(V\) such that
\(\pi|_U=\sigma\).  Write \(g_i\) for the gap after \(u_i\), and let

\[
 B(\pi,U)=\{i:g_i\text{ contains at least one label of }A\}. \tag{8.2}
\]

For a phase \(a\) and \(-H\le r\le H\), define

\[
 X_a(r)=\{u_a,u_{a+1},\ldots,u_{a+m+r-1}\}.              \tag{8.3}
\]

At \(r=0\), this is the complement of the corresponding promotion
target \(A\cup I_\sigma(a+m,H)\), up to a fixed phase translation.
Since an \(m\)-interval in a cyclic order of length \(2m\) has an
\(m\)-interval complement, ambient certification of either member is
equivalent.

### Lemma 8.1 (exact inherited staircase)

Let

\[
 P(\pi,U)=\{a:X_a(0)\text{ is a cyclic }m\text{-interval of }\pi\}.
                                                               \tag{8.4}
\]

If \(P(\pi,U)\ne\varnothing\), then it is one cyclic interval of phases,
of some length \(L\le H+1\).  Among those \(L\) phases, the largest
depths through which the whole nested family

\[
                         (X_a(r))_{-d\le r\le d}          \tag{8.5}
\]

remains ambient-consecutive are exactly

\[
                         0,1,\ldots,L-1.                 \tag{8.6}
\]

Consequently the exact number of inherited phases of depth at least
\(d\) is

\[
                         (L-d)_+.                         \tag{8.7}
\]

#### Proof

The internal gaps of \(X_a(r)\) are

\[
                         g_a,g_{a+1},\ldots,g_{a+m+r-2}.
\]

Thus every set in (8.5) remains consecutive in \(\pi\) if and only if
all occupied gaps lie in the smallest complementary gap interval,

\[
 B(\pi,U)\subseteq
 Q_a(d):=\{a+m+d-1,\ldots,a-1\},                         \tag{8.8}
\]

which has exactly \(H-d+1\) gaps.  In particular, at depth zero the
occupied gaps must lie in an interval of \(H+1\) gaps.

Because \(A\ne\varnothing\), the occupied-gap set is nonempty.  Also
\(H+1<M/2\) for all sufficiently large \(m\).  Hence, whenever (8.4) is
nonempty, \(B(\pi,U)\) has a unique minimal cyclic hull, say of length
\(s\le H+1\).  The length-\((H+1)\) gap intervals containing that hull
have consecutive starts and number

\[
                         L=H-s+2\le H+1.                 \tag{8.9}
\]

As the containing interval moves through those \(L\) starts, its slack
before the fixed hull is \(0,1,\ldots,L-1\).  Passing from \(Q_a(0)\) to
\(Q_a(d)\) removes precisely the first \(d\) gaps, so this slack is the
largest admissible depth.  This proves (8.6)--(8.7). \(\square\)

### Theorem 8.2 (middle-owner-simple chronology capacity)

Let \(\mathcal F\) be a family of ambient rows in which no middle set is
an \(m\)-window of two distinct rows.  Suppose that at every promotion
top one fixes one complete order \(\sigma\), and only rows satisfying
\(\pi|_U=\sigma\) are used to inherit its flags.  Then the total number
\(C_d\) of inherited phase flags reaching depth \(d\) obeys

\[
 \boxed{C_d\le MN_H\left(1-\frac d{H+1}\right)}
 \qquad(0\le d\le H).                                   \tag{8.10}
\]

#### Proof

At a fixed \((U,\sigma)\), the phase intervals \(P(\pi,U)\) belonging
to distinct rows are disjoint.  Otherwise their common phase would give
the same ambient \(m\)-window in two rows, contradicting the hypothesis.
If their nonzero lengths are \(L_1,\ldots,L_b\), then

\[
                         \sum_jL_j\le M.                 \tag{8.11}
\]

Lemma 8.1 and the elementary inequality

\[
 (L-d)_+\le L\left(1-\frac d{H+1}\right)
 \qquad(0\le L\le H+1)                                 \tag{8.12}
\]

give the same bound with \(M\) in place of \(MN_H\) at one top.  There
are \(N_H\) tops, proving (8.10). \(\square\)

### Corollary 8.3 (exact failed grouped Hall cut)

Put \(N_d=\binom{2m}{m-d}\).  The retained-chain census has
\(N_e-N_{e+1}\) chains of terminal radius \(e<H\) and \(N_H\) chains of
radius \(H\).  Hence the number of demanded flags reaching depth \(d\)
is exactly

\[
 \sum_{e=d}^{H-1}(N_e-N_{e+1})+N_H=N_d.                 \tag{8.13}
\]

Therefore the entire demand shore at depth \(d\) violates Hall by at
least

\[
 \boxed{
 \Delta_d=
 \left[N_d-MN_H\left(1-\frac d{H+1}\right)\right]_+.}   \tag{8.14}
\]

Assume now the exact packing-side floor

\[
                         (M-1)N_H\le W.                  \tag{8.15}
\]

The exact ratio and the union bound give

\[
 \frac{N_d}{W}
 =\prod_{j=0}^{d-1}\frac{m-j}{m+j+1}
 =\prod_{j=0}^{d-1}
   \left(1-\frac{2j+1}{m+j+1}\right)
 \ge1-\frac{d^2}{m}.                                    \tag{8.16}
\]

Moreover, (8.15) implies

\[
 MN_H\le W\left(1+\frac1{M-1}\right).                   \tag{8.17}
\]

Substituting (8.16)--(8.17) into (8.14) yields

\[
 \Delta_d\ge W\left(
       \frac d{H+1}-\frac{d^2}{m}-\frac1{M-1}
                         \right).                        \tag{8.18}
\]

Set

\[
 q_0=\lceil m^{1/4}\rceil,qquad
 d_\star=\left\lfloor\frac{m}{4(H+1)}\right\rfloor.     \tag{8.19}
\]

Uniformly for \(q_0\le d\le d_\star\), and all sufficiently large
\(m\),

\[
 \frac{d^2}{m}\le\frac d{4(H+1)},qquad
 \frac1{M-1}\le\frac d{4(H+1)}.                         \tag{8.20}
\]

Thus

\[
 \boxed{\Delta_d\ge\frac{Wd}{2(H+1)}}.                  \tag{8.21}
\]

Since \(q_0=o(d_\star)\), summing gives

\[
 \boxed{
 \sum_{d=q_0}^{d_\star}\Delta_d
 \ge\left(\frac1{64}+o(1)\right)\frac{Wm^2}{H^3}
 =\Omega\!\left(\frac{W\sqrt m}{(\log m)^{3/2}}\right)
 =\omega(W).}                                           \tag{8.22}
\]

The conclusion through (8.22) applies only under cyclic-window
simplicity.  It does not apply to the full cut MSW row bank unless the
chosen row set is first proved independent in the cut complement graph.
With cyclic multiplicity at most \(\mu\), the same proof gives only

\[
 C_d\le \mu MN_H\left(1-\frac d{H+1}\right).             \tag{8.23}
\]

For the cut MSW factor \(\mu=2\), and (8.23) is larger than the demand
throughout the claimed shallow range.  Hence it supplies no positive
deficiency there.  Restricting to designated primary occurrences restores
uniqueness but not the staircase decay: intersecting a staircase with the
primary arc can retain only its high-radius endpoint.

### Lemma 8.4 (exact cyclic multiplicity-two correction)

For a cut row

\[
 \pi_x=(a_{x,1},\ldots,a_{x,2m})
\]

with primary windows \(P_{x,j}\) from (1.2), its complete cyclic
middle deck is the disjoint union

\[
 \boxed{
 E_m(\pi_x)
 =\{P_{x,j}:1\le j\le m+1\}
  \mathbin{\dot\cup}
  \{P_{x,j}^{\,c}:2\le j\le m\}.}                       \tag{8.24}
\]

The two port primaries \(P_{x,1}\) and \(P_{x,m+1}\) are complements.
The nonport primary family is complement-closed globally, and a
complementary nonport pair is owned by two distinct rows.  Consequently,
over the whole cut factor every port target has cyclic load one and every
nonport target has cyclic load two.

#### Proof

The \(m+1\) windows not crossing the cut are exactly the primary family.
A cyclic \(m\)-window crossing the cut has a complementary noncrossing
window whose start lies in \(2,\ldots,m\), giving the second family in
(8.24).  Distinct cyclic starts give distinct proper intervals.
The only complementary primary pair within one row is the pair at starts
1 and \(m+1\).  Since all primary targets over all rows form the
partition (1.3), complementation pairs the remaining nonports and their
two primary owners must be distinct. \(\square\)

Equivalently, form the cut complement multigraph whose vertices are rows
and whose edges join the primary owners of complementary nonports.  A row
subfamily is cyclic-window-simple exactly when it is an independent set
of this graph.  No such property follows from Catalan component size, and
the full completed factor is not independent: the complement graph is
\((m-1)\)-regular.

## 9. Proved boundary

The exact advance is positive at the incidence level and negative at the
component-local physical level.

* Every promotion provider incidence has a complete MSW owner-row frame
  witness.
* The two shores of an ownership component lift coherently over every
  target star in its resource block.
* The mechanical clone graph can be coloured by these component resources
  without losing a single Hall edge.
* The unique top component alone controls only
  \((5/16+o(1))W\) canonical target stars.
* Using all owner components makes the root--component dependency graph
  connected, so independent component rounding collapses to one global
  block.
* Direct cut-only physical inheritance pays at least
  \((5/8-o(1))W\) collar on the top component alone.
* A cyclic-window-simple row bank has the exact staircase spectrum (8.7)
  and the conditional aggregate \(\omega(W)\) shallow deficiency.
  A completed cut MSW factor has multiplicity two, so this particular
  deficiency conclusion is unavailable.
* For the actual natural owner-row lift, the exact radius-\(d\) good-root
  density is \((H)_d/(m)_d\) per shore and at most twice that over both
  shores; it is \(o(1)\) already at \(d=1\).

What remains is exactly a globally coupled, chronology-changing cross-row
braid solving (7.2)--(7.4), or equivalently a common-order grouping of the
near-perfect mechanical clone matching which uses complementary owner
mates or changes ambient rows between depths.  No cardinality or
individual clone-Hall obstruction remains, but no literal global braid is
constructed here.
