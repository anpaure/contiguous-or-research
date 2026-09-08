# Source--helper atomization, trapped-menu gammoids, and the coatom reset

**Date:** 2026-08-03

**Status:** unconditional abstract same-child theorem, exact min-cut
characterization, exact loss-compensated contraction recurrence, a minimal
non-gammoid obstruction, and a near-perfect coatom helper-allocation lemma.
The literal all-dimensional source/helper rescue relation, private bundle
bank, supplier-port nesting, and complete casualty bound remain unproved.
No unconditional additive bound is claimed.

## 0. Outcome

The canonical K17 source--helper architecture isolates the correct all-\(k\)
primitive.

* A supplier-positive source can be occurrence-invalid by itself and become
  valid only after a helper installs a new host.  Exact primitive-mode
  feasibility therefore cannot equal gammoid independence on such a face.
* Even after replacing modes by source/helper pair options, exact pair
  packing is generally not a matroid.
* After an injective private-helper assignment has been fixed, all bundles
  have been materialized in one child, and every non-supplier dependency has
  been closed or priced, the remaining supplier service claims form a
  capacity-faithful gammoid represented as a restriction of one strict
  gammoid network.

For that strict gammoid, the exact hereditary expansion row is a
**trapped-menu cut**.  If \(W\) is a finite-cut-admissible sink-avoiding
side of the fixed
vertex-split alternating network, \(c(W)\) is its literal outgoing capacity,
and

\[
 t_X(W)=|\{u\in X:P_u\subseteq W\}|,
\]

then the maximum number \(p(X)\) of routed occurrence-labelled claims is

\[
 \boxed{p(X)=\min_W\bigl(|X|-t_X(W)+c(W)\bigr).}       \tag{0.1}
\]

Hence

\[
 p(X)\ge\eta|X|-\gamma\quad(X\subseteq\overline U)
                                                                  \tag{0.2}
\]

is equivalent to

\[
 \boxed{c(W)\ge\eta\,t_{\overline U}(W)-\gamma
        \quad\hbox{for every such }W.}                \tag{0.3}
\]

This is the weakest checkable same-child expansion condition.  It involves
neither marginal mode scores nor a union of representation-dependent
supplier graphs.

There is a stronger loss-compensated endpoint.  If one child loses \(q\)
units of a parent matching and exposes \(g\) genuine deficit-reducing gain
claims, expose \(q\) compensation claims as well.  If the
combined claim bank has gammoid deficiency at most \(C\), then

\[
                         \boxed{\delta'\le\delta-g+C.} \tag{0.4}
\]

Thus even extensive core loss cancels when every lost unit is represented
in the same near-perfect linkage bank.

The mixed-coatom two-ray geometry gives a finite reduction.  If its actual
occurrence-labelled port menus are nested along two rays, the full
hereditary deficiency is the maximum of only quadratically many prefix-pair
ranks.  Existing notes prove the two physical nested chains, not this
same-child supplier-port nesting.

## 1. The exact same-child alternating gammoid

Fix an authenticated parent completed supplier graph

\[
                    \widehat G^0=(L,R;E^0)
\]

and a parent maximum matching \(M\) of size \(r\).  Fix one fully
materialized child

\[
                    \widehat G^+=(L,R;E^+)
\]

on the same semantic vertex universe.  All root/common-basis choices,
source/helper modes, occurrence witnesses, flags and representation choices
are already fixed in this child, and its supplier graph has been rebuilt
from the literal table.

Let

\[
 M_0\subseteq M\cap E^+,\qquad |M_0|=r-q.             \tag{1.1}
\]

Another retained matching may reduce \(q\); nothing below requires the
displayed choice to be optimal.  Put

\[
 L_0=V_L(M_0),\qquad F=L-L_0,\qquad
 T=R-V_R(M_0).                                        \tag{1.2}
\]

Orient every child edge outside \(M_0\) from \(L\) to \(R\), orient every
edge of \(M_0\) from \(R\) to \(L\), and split every literal
capacity-one vertex.  Call the resulting directed network \(D^+\).  Its
sinks are the unmatched right vertices \(T\).

For \(Z\subseteq F\), let \(\rho(Z)\) be the maximum number of
vertex-disjoint directed paths from distinct members of \(Z\) to \(T\).

### Theorem 1.1 (exact free-head gammoid)

The linkable subsets of \(F\) form a gammoid, represented as the restriction
to \(F\) of the strict gammoid \(L(D^+,T)\), and

\[
 \boxed{
 \rho(Z)=
 \nu\!\left(\widehat G^+[L_0\cup Z,R]\right)-|M_0|
 =
 |Z|-\max_{Q\subseteq L_0\cup Z}
       \bigl(|Q|-|N_{\widehat G^+}(Q)|\bigr).
 }                                                       \tag{1.3}
\]

For \(Z=F\), if \(p=\rho(F)\), then

\[
 \nu(\widehat G^+)=r-q+p,\qquad
 \delta(\widehat G^+)=\delta(\widehat G^0)+q-p.        \tag{1.4}
\]

#### Proof

A directed \(Z\)-to-\(T\) path is exactly an \(M_0\)-augmenting path.
Disjoint paths augment simultaneously.  Conversely, compare \(M_0\) with a
maximum matching of the displayed induced child graph.  Their symmetric
difference has no component containing one more \(M_0\)-edge, since
toggling such a component would augment the maximum child matching.
Every unit of rank difference is therefore a vertex-disjoint
\(M_0\)-augmenting component beginning in \(Z\).  This proves the first
equality.

Hall's deficiency formula on the left shore \(L_0\cup Z\), whose size is
\(|M_0|+|Z|\), gives the second equality.  Taking \(Z=F\) and comparing
both ranks with the common semantic left-shore size proves (1.4).
\(\square\)

This network is capacity-faithful only for supplier matching.  An address
equality, history identity, root/common-basis choice, compiler relocation,
or all-or-none source/helper dependency is not made path-like merely by
drawing an anonymous capacity vertex.  Such rows must be fixed before
\(D^+\) is formed, proved to have a separate path representation on
physically disjoint resources, or priced as casualties.

## 2. Why source/helper modes must first be atomized

### Definition 2.1 (private source/helper bundle)

In one jointly materialized child, a private source/helper bundle consists
of:

1. one supplier source mode and every helper or circuit mode needed for its
   occurrence closure;
2. fixed phase-specific predecessor/successor witnesses with a common
   declared state and consistent physical flags;
3. its complete endpoint, donor, host, address, history, reset, residence,
   upper and compiler footprint;
4. a verified local or global accounting of every parent matching edge
   destroyed by the bundle; and
5. a finite list of actual \(M_0\)-unmatched free-head service portals.

Different bundles must have disjoint non-supplier footprints.  Alternatively,
every overlapping family must have a proved capacity-safe zero-boundary
circuit and be contracted as one larger bundle.  Zero boundary without
joint capacity safety is not enough.  The only uncontracted interaction is
then the advertised supplier-port linkage in \(D^+\).

The order of quantifiers is load-bearing:

\[
 \boxed{\text{choose and atomize the bundle bank}
 \;\longrightarrow\;
 \text{materialize one child}
 \;\longrightarrow\;
 \text{replay suppliers}
 \;\longrightarrow\;
 \text{form }D^+.}                                    \tag{2.1}
\]

Helper alternatives from different child representations cannot be united
as arcs of one network.

### Proposition 2.2 (primitive-mode nonheredity)

Suppose a source mode \(s\) is occurrence-invalid alone, while
\(\{s,h\}\) is occurrence-valid because helper \(h\) installs a required
host.  Exact feasibility on the primitive mode ground cannot be the
independent-set family of a strict gammoid.

#### Proof

Gammoid independence is hereditary.  It cannot contain \(\{s,h\}\) while
excluding its subset \(\{s\}\). \(\square\)

### Proposition 2.3 (minimal shared-helper nonmatroid)

Let the three pair options be

\[
 e_{11}=(s_1,h_1),\qquad
 e_{12}=(s_1,h_2),\qquad
 e_{22}=(s_2,h_2),
                                                               \tag{2.2}
\]

and call a set feasible when no source or helper is repeated.  This
feasible family is not a matroid and therefore not a strict gammoid.

#### Proof

The two-edge set \(I=\{e_{11},e_{22}\}\) and the singleton
\(J=\{e_{12}\}\) are feasible.  Neither member of \(I-J\) can be added to
\(J\): one repeats \(s_1\), the other repeats \(h_2\).  The matroid
augmentation axiom fails.  No obstruction exists on a ground of size at
most two, so this is ground-size minimal. \(\square\)

There is an equivalent two-resource example.  If one option uses
\(\{a,b\}\), a second uses \(\{a\}\), and a third uses \(\{b\}\), then
\(\{a,b\}\) as one option and the two singleton options give the same
augmentation failure.  Arbitrary occurrence-resource hypermatching is not
a gammoid.

If helper choice is supplier-port transparent in one already fixed child,
then, on the source ground, shared-helper allocation is a transversal
matroid and supplier linkability is a gammoid.  Their common feasible sets
are a two-matroid intersection, not generally a matroid.  Without that
transparency there are not even two fixed matroids on one ground.
Preassigning an injective private helper, or proving an exact switch-safe
rectangular network, is what removes this obstruction.  A layered
source--helper--supplier drawing without supplier-port transparency is only
a relaxation: a path may enter through one option and leave through another
source's continuation.

## 3. Occurrence-labelled service claims and the trapped-menu cut

After the child and bundle bank are fixed, let \({\cal C}\) be a finite
set of unit service claims.  Claims are occurrence-labelled.  A physical
packet which loses \(q_b\) parent matching units and seeks one genuine gain
may contribute \(q_b+1\) claims; one packet is not synonymous with one
augmenting path.

For each claim \(u\), let \(P_u\subseteq F\) be its actual menu of free-head
entry portals in \(D^+\).  Any private spoke from a packet boundary to such
a head is already authenticated and contracted into this menu.  Add a
private start vertex for \(u\), with arcs to \(P_u\), and retain all literal
unit capacities in \(D^+\).  The resulting linkable claim sets form a
gammoid \(\Gamma_{\rm pkt}\), represented as the restriction to the claim
starts of the expanded strict gammoid.

For \(X\subseteq{\cal C}\), write

\[
                         P(X)=\bigcup_{u\in X}P_u .
\]

### Theorem 3.1 (exact packet rank)

The claim rank is

\[
 \boxed{
 r_{\rm pkt}(X)
 =\min_{Y\subseteq X}
    \left(
      |X-Y|+\rho(P(Y))
    \right).
 }                                                       \tag{3.1}
\]

Equivalently, all but \(h\) claims in \(X\) can be routed if and only if

\[
 \nu\!\left(\widehat G^+[L_0\cup P(Y),R]\right)
       \ge |M_0|+|Y|-h
       \qquad(Y\subseteq X).                            \tag{3.2}
\]

#### Proof

Equation (3.1) is the deficient form of Rado's independent-transversal
theorem applied to the port menus in the free-head gammoid of Theorem 1.1.
Substitute (1.3) to obtain (3.2).  The same result follows directly by
max-flow after adjoining the private claim vertices. \(\square\)

For the exact cut form, fully split every unit-capacity physical vertex into
an in-half and out-half joined by a unit arc.  Claim-to-port arcs have
infinite capacity and enter the specified in-half of the free-head port.
Adjoin a supersink after the unmatched-right outputs.  Let \(W\) range over
subsets of the split base-network vertices that exclude that supersink and
its output terminals and are finite-cut-admissible: no infinite-capacity arc
may leave \(W\).  Let \(c(W)\) be the
total capacity of every finite outgoing arc (including every crossed unit
vertex-capacity arc).  Equivalently one may let \(W\) range over all source
sides and put \(c(W)=+\infty\) when an infinite arc leaves \(W\).  For
\(X\subseteq{\cal C}\), put

\[
 t_X(W)=|\{u\in X:P_u\subseteq W\}|.                  \tag{3.3}
\]

### Theorem 3.2 (trapped-menu min-cut)

\[
 \boxed{
 r_{\rm pkt}(X)
   =\min_W\bigl(|X|-t_X(W)+c(W)\bigr)
   =|X|-\max_W\bigl(t_X(W)-c(W)\bigr).
 }                                                       \tag{3.4}
\]

#### Proof

Add a supersource with a unit arc to every claim vertex and infinite arcs
from claim \(u\) to its menu \(P_u\).  In a finite cut whose base-network
portion is \(W\), a claim vertex can remain with the supersource precisely
when the specified in-halves of all its ports lie in \(W\).  The other
\(|X|-t_X(W)\) supersource arcs cross the cut, and the base network
contributes \(c(W)\).  Integral max-flow/min-cut proves (3.4).
\(\square\)

Fix a finite occurrence-labelled master claim universe
\(\overline{\cal C}\).  Repeated structural types remain distinct claims.

### Corollary 3.3 (weakest hereditary cut)

For \(0\le\eta\le1\) and \(\gamma\ge0\), the following are equivalent:

\[
 r_{\rm pkt}(X)\ge\eta|X|-\gamma
       \qquad(X\subseteq\overline{\cal C}),             \tag{3.5}
\]

and

\[
 \boxed{
 c(W)\ge\eta\,t_{\overline{\cal C}}(W)-\gamma
       \qquad\hbox{for every finite-cut-admissible sink-avoiding }W.
 }                                                       \tag{3.6}
\]

#### Proof

If (3.6) holds, (3.4) gives

\[
 r_{\rm pkt}(X)
 \ge |X|-(1-\eta)t_X(W)-\gamma
 \ge\eta|X|-\gamma
\]

for every cut \(W\).  Conversely, fix \(W\) and take
\(X=\{u:P_u\subseteq W\}\).  Its rank is at most \(c(W)\), while (3.5)
lower-bounds it by \(\eta|X|-\gamma\). \(\square\)

For one already fixed exposure \(X\), the weakest target \(r_{\rm pkt}(X)
\ge R\) is simply

\[
 c(W)\ge R-|X|+t_X(W)\qquad(W).                       \tag{3.7}
\]

The hereditary row is needed only when the later exposed occurrence subset
is not yet known.

There is an equivalent blocked-separator form.  Work in the **full augmented
claim network**, including the unit supersource--claim arcs and all physical
vertex capacities.  Let \(C\) be any finite-capacity arc separator in this
network and let \(\|C\|\) denote its total capacity.  (After unit expansion,
this is its cardinality.)  Let \(B(C)\) be the claims for which every
supersource-to-sink route through that claim meets \(C\).  Thus claim-start
arcs are allowed in \(C\); restricting
\(C\) to base-network physical resources would not give an equivalent test.
For \(\Lambda\ge1\) and \(\Gamma\ge0\),

\[
 r_{\rm pkt}(X)\ge\frac{|X|-\Gamma}{\Lambda}
        \quad(X\subseteq\overline{\cal C})              \tag{3.8}
\]

if and only if

\[
 \boxed{|B(C)|\le\Lambda\|C\|+\Gamma
       \quad\hbox{for every full-network finite-capacity separator }C.}
                                                               \tag{3.9}
\]

Necessity applies (3.8) to \(B(C)\).  For sufficiency, fix a trapped-menu
cut side \(W\).  Its outgoing separator \(C=\delta^+(W)\) blocks every one
of the \(t_X(W)\) trapped claims, so

\[
 t_X(W)\le |B(C)|\le\Lambda\|C\|+\Gamma
          =\Lambda c(W)+\Gamma.
\]

Substitution in (3.4) gives
\(r_{\rm pkt}(X)\ge(|X|-\Gamma)/\Lambda\).

Thus a bounded shared helper or owner cut is a sharp obstruction.  If
\(\eta>0\) and all
routes for \(X\) cross capacity \(b\), then \(r_{\rm pkt}(X)\le b\), and
(3.5) forces

\[
                         |X|\le\frac{b+\gamma}{\eta}.   \tag{3.10}
\]

Menu abundance behind one bottleneck has no extensive rank.

## 4. Loss-compensated contraction

Relative to \(M_0\), each of the \(q\) parent matching units omitted from
\(M_0\) creates one compensation claim at its unmatched left endpoint.  If
\(M_0=M\cap E^+\), these are precisely the lost parent edges; a deliberately
smaller \(M_0\) merely creates extra, immediately checkable compensation
claims.  Choose \(g\) distinct parent-unmatched semantic heads as genuine
gain claims.  The combined bank therefore has \(q+g\) claims.

### Theorem 4.1 (near-perfect compensation)

If the combined claim bank has gammoid deficiency at most \(C\), equivalently

\[
 r_{\rm pkt}({\cal C})\ge q+g-C,                       \tag{4.1}
\]

then

\[
 \boxed{
 \nu(\widehat G^+)\ge r+g-C,\qquad
 \delta(\widehat G^+)\le\delta(\widehat G^0)-g+C.
 }                                                       \tag{4.2}
\]

#### Proof

The routed claims give \(p\ge q+g-C\) disjoint
\(M_0\)-augmenting paths.  Substitute in (1.4):

\[
 \delta'\le\delta+q-(q+g-C)=\delta-g+C.
\]

\(\square\)

The core loss \(q\) may be extensive.  Suppose there are \(g\) packets, one
per gain claim, and every edge of \(M\setminus M_0\) is attributed either
to one of their packet damage sets or to a
boundary set of size at most \(b_q\), and each packet damage set contains at
most \(w\) edges of \(M\).  Equivalently, one may choose \(M_0\) to retain
every unaffected edge of \(M\).  Then

\[
                         q\le wg+b_q,                  \tag{4.3}
\]

so the total claim bank still has size at most
\((w+1)g+b_q\).  Equation (4.2), not an absolute bound on \(q\), is the
stronger regenerative target.

### Theorem 4.2 (fractional compensation and complete casualties)

Suppose \(0\le\eta\le1\) and all rate and additive parameters below are
nonnegative, and suppose

\[
\begin{aligned}
 r_{\rm pkt}({\cal C})&\ge\eta(q+g)-\gamma,\\
 q&\le a\Phi+b_q,\\
 g&\ge\kappa\Phi-b_g,\\
 c_{\rm ns}&\le\zeta\Phi+b_{\rm ns},
\end{aligned}                                             \tag{4.4}
\]

where \(c_{\rm ns}\) prices every owner, occurrence, endpoint, address,
history, reset, residence, upper, compiler and chronology casualty not
already canceled inside the bundle.  Assume the separately verified
complete-potential row

\[
                 \Phi'\le\Phi+q-p+c_{\rm ns}.          \tag{4.5}
\]

Then

\[
 \boxed{
 \Phi'\le
 \left[1-\eta\kappa+(1-\eta)a+\zeta\right]\Phi
 +(1-\eta)b_q+\eta b_g+\gamma+b_{\rm ns}.
 }                                                       \tag{4.6}
\]

Put

\[
 \varrho=1-\eta\kappa+(1-\eta)a+\zeta.
\]

The numerical surplus condition

\[
 \boxed{\eta\kappa>(1-\eta)a+\zeta.}                   \tag{4.7}
\]

is exactly \(\varrho<1\).  If \(0\le\varrho<1\), (4.6) is an ordinary
strict affine contraction.  If \(\varrho<0\), nonnegativity of \(\Phi'\)
and (4.6) instead force the current \(\Phi\) to be at most the displayed
additive constant divided by \(-\varrho\).  Thus (4.7) is sufficient for
contraction-or-already-bounded behavior, but the phrase ``affine
contraction'' is reserved for the first case.

#### Proof

The first row of (4.4) gives

\[
 p-q\ge\eta g-(1-\eta)q-\gamma.
\]

Substitute the remaining bounds into (4.5). \(\square\)

At the near-perfect endpoint \(\eta=1\), extensive core loss cancels
completely.  If \(g\ge\alpha\Phi-b_0\), the routing deficiency is at most
\(C\), and

\[
                         c_{\rm ns}\le\theta g+b_{\rm ns}
                                                               \tag{4.8}
\]

with \(0\le\theta<1\), then

\[
 \boxed{
 \Phi'\le
 [1-\alpha(1-\theta)]\Phi
 +(1-\theta)b_0+C+b_{\rm ns}.
 }                                                       \tag{4.9}
\]

In particular, \(g\ge\Phi-b_0\), \(\theta=0\), and
\(C+b_{\rm ns}=O(1)\) give an \(O(1)\) reset in one transition.

Bounded compiler eviction contributes to \(c_{\rm ns}\) only after its
complete damage set is shown to meet \(O(1)\) cells of one reference
matching.  Marginal ticket legality does not prove that bound.

## 5. A concrete Pascal/coatom helper-allocation lemma

Let

\[
 G_r=(L,R;E),\qquad
 L={[2r-1]\choose r-1},\quad R={[2r-1]\choose r},
\]

be the odd-central containment graph.  Both shores have the same size and
every vertex has degree \(r\).  Every nonempty proper \(X\subsetneq L\)
satisfies

\[
                         |N_{G_r}(X)|\ge|X|+1.          \tag{5.1}
\]

Fix a protected matching \(P\) of size \(t\), and delete its left and right
endpoints.  Let \(G_r-P\) denote the residual graph.

### Theorem 5.1 (near-perfect protected coatom allocation)

If \(t=0\), the residual transversal rank is full.  If \(t\ge1\), then for
every \(X\subseteq L-L(P)\),

\[
 \boxed{r_{G_r-P}(X)\ge |X|-(t-1).}                   \tag{5.2}
\]

More generally, suppose a literal source--helper rescue graph \(R_{\rm lit}\)
on the same shores obeys the bounded-erosion sufficient condition

\[
 |N_{R_{\rm lit}}(X)|\ge|N_{G_r}(X)|-E
       \qquad(X\subseteq L-L(P)).                       \tag{5.3}
\]

Then

\[
 \boxed{
 r_{R_{\rm lit}-P}(X)
 \ge |X|-C_H,\qquad
 C_H=E+\max\{t-1,0\}.
 }                                                       \tag{5.4}
\]

#### Proof

For \(t\ge1\), every residual nonempty \(X\) is proper in \(L\).  Removing
the \(t\) protected right endpoints from (5.1) gives

\[
 |N_{G_r-P}(X)|\ge|X|+1-t.
\]

Every Hall deficit is therefore at most \(t-1\), which is (5.2).
With (5.3), the same argument loses another \(E\) neighbors.

For \(t=0\), regular bipartite Hall gives full rank in \(G_r\).  Under
(5.3), the full shore can lose at most \(E\) neighbors and proper shores at
most \(E-1\) units of Hall slack, so the uniform bound in (5.4) is valid.
\(\square\)

Condition (5.3) is a concrete checkable sufficient bridge, not a necessary
condition.  A rescue graph can have near-perfect Hall rank while deleting
many coatom edges.

Theorem 5.1 is genuine all-\(r\) progress.  It shows that the bare coatom
\(+1\) proper-shore expansion absorbs a bounded protected bank with only
bounded hereditary helper deficiency.  What remains unproved is that the
literal Pascal source--helper rescue relation is a bounded erosion of this
containment graph and that the chosen helper envelopes are private.

## 6. The two-ray prefix reduction

Let \(u_1,\ldots,u_m\) and \(v_1,\ldots,v_n\) be two claim chains in one
fixed child.  Suppose their port menus are nested:

\[
 A_1\subseteq A_2\subseteq\cdots\subseteq A_m,\qquad
 B_1\subseteq B_2\subseteq\cdots\subseteq B_n.         \tag{6.1}
\]

Put \(A_0=B_0=\varnothing\).

### Theorem 6.1 (two-ray prefix uncrossing)

For any matroid rank \(r_\Gamma\), in particular for the strict gammoid rank
of Section 3, the deficient-Rado residual of all \(m+n\) claims is

\[
 \boxed{
 C_{\rm ray}
 =\max_{\substack{0\le i\le m\\0\le j\le n}}
   \left(i+j-r_\Gamma(A_i\cup B_j)\right).
 }                                                       \tag{6.2}
\]

More generally, for \(0\le\eta\le1\),

\[
 \max_{X}
 \left(\eta|X|-r_\Gamma(P(X))\right)
 =
 \max_{i,j}
 \left(\eta(i+j)-r_\Gamma(A_i\cup B_j)\right).         \tag{6.3}
\]

#### Proof

Take any subset \(X\).  Suppose it contains \(k\) claims from the first
chain and \(\ell\) from the second, and let \(a\ge k\), \(b\ge\ell\) be
their largest selected indices, with zero for an empty part.  Nesting gives
\(P(X)=A_a\cup B_b\).  Hence

\[
 \eta|X|-r_\Gamma(P(X))
 \le \eta(a+b)-r_\Gamma(A_a\cup B_b).
\]

The right side is attained by taking both complete prefixes.  Conversely
every prefix pair is an allowed subset, so the maximum is attained among
them.
\(\square\)

Thus near-perfect two-ray routing with defect \(C\) is equivalent to only

\[
 r_\Gamma(A_i\cup B_j)\ge i+j-C
 \qquad(0\le i\le m,\ 0\le j\le n),                  \tag{6.4}
\]

and fractional expansion replaces \(i+j-C\) by
\(\eta(i+j)-\gamma\).  Each row is one same-child max-flow/min-cut.  This is
quadratic rather than exponential in the two ray lengths.

The current mixed-coatom theorem proves two nested physical provider chains
with fixed opposite endpoints.  It does **not** prove that the
occurrence-labelled compensation/gain port menus in one common child satisfy
(6.1).  That exact nesting/port-transparency statement is now the smallest
two-ray bridge.

Nor may the quadratic formal coatom relabelling atlas be used as a menu at
one incumbent anchor.  A fixed old word recovers its active labels and has
only one canonical option.  Extensive rank must come from extensively many
prepared literal anchors, not from relabelling one fixed slot.

## 7. K17 calibration rebased on the anchored pair no-go

On the authoritative canonical K17 deficiency-21 parent:

Phase 1 remains transported-owner evidence; no native-phase-1 conclusion is
used below.

1. there are 468 one-mode supplier-positive children;
2. their retained-parent losses are \(q=0,1,2\) for respectively
   \(226,194,48\) sources;
3. because every child has rank \(r+1\), their maximum augmentation counts
   are \(p=1,2,3\), respectively;
4. every one of the 468 sources has no native/transported common occurrence
   state even after own-host self-support;
5. every row-disjoint set drawn only from the 3,483 exact-common helper pool
   has zero or negative credit on the fixed \(23/2\) shore; and
6. any feasible pair on the declared \(468\times112,621\) anchored
   source/partner lane would have to use the partner's newly created host in
   a source witness; and
7. the complete directed scan of all 52,664,349 such incidences leaves 94
   host-aperture upper survivors, but exact replay gives every one of their
   partners an empty native-phase-0 occurrence menu.  Hence none is an exact
   two-mode occurrence packing.

Thus every occurrence-valid atom containing one of these 468 authenticated
sources needs at least three primitive modes.  Three is only the first
cardinality not excluded: no live triple is proved.  On the 94-survivor
extension lane, a third mode can create a partner phase-0 tuple only through
its newly installed host, giving the forced second aperture link

\[
                 \text{source}\leftarrow\text{helper}
                 \leftarrow\text{third rescuer}.
\]

The complete six-endpoint-disjoint extension domain has 10,536,324 rows.
A lossless phasewise screen leaves 70, and two exact complete-menu replays
agree that the third mode has zero native-P0 tuples on all 70.  Hence this
entire **single-helper linear-chain branch is empty**.  In any remaining
H-containing triple, the selected source option must use both helper hosts
across its phase tuples.  Thus the next surviving candidate is a bilateral
fork/circuit module, not the chain displayed above.

This does not make the directed pair graph a complete triple oracle.  A
general triple may be a fork or circuit, the third ticket and the partner's
phase-1 ticket remain unchecked, and simultaneous supplier replay remains
open.  Nor is this a global K17 pair classification: the 47 rank-stagnant
positive anchors and their 5,267,978-child residual two-mode face remain
outside the authenticated 468-source no-go.

The capacity-only helper-ID graph is already abundant.  Every source has
between 3,477 and 3,483 row-safe helper IDs.  Therefore every nonempty source
set \(X\) has

\[
 |N(X)|\ge3477\ge468\ge|X|,                            \tag{7.1}
\]

so the helper-ID graph has a source-saturating matching.  Even after deleting
any 3,009 helper IDs, every source retains degree at least 468, and the same
argument still applies.

This is only a helper-ID/capacity Hall factor and is now known not to close a
two-mode atom on the authenticated source lane.  It does not certify a
terminal rescuer, changed-long-state compatibility, private physical
envelopes, simultaneous materialization, root/common-basis recoupling, or
final supplier rank.

The smallest survivor-extension **candidate form** of an
authenticated-source gammoid-ready module is therefore

\[
 \boxed{\text{one terminally closed bilateral three-mode fork/circuit
 + private/controlled closure + all loss/gain service claims}.} \tag{7.2}
\]

Equation (7.2) is not an existence assertion.  Its phase-paired tuples must
be replayed in the final simultaneous child; composing pairwise rescue edges
is unsound because a later donor deletion may destroy an earlier tuple and
the links may reuse a capacity-one row.  The complete bilateral natural-join
domain remains unenumerated.  Zero signature is the clean sufficient
endpoint, not a general
minimality claim: Theorem 4.2 permits a nonzero casualty rate below the
available augmentation surplus.  One new carried casualty per one-unit gain
makes \(\theta=1\) in (4.8) and removes strict surplus from this one-step
recurrence.

## 8. A checkable coatom--gammoid reset theorem

The preceding rows combine into one concrete target.

### Theorem 8.1 (private coatom reset)

Let a reachable same-parity state have complete carried potential \(\Phi\)
and an occurrence-labelled source set \(S\) with

\[
                         |S|\ge\alpha\Phi-b_0.         \tag{8.1}
\]

Assume, on one child and one compatible spine:

1. the literal rescue graph satisfies Theorem 5.1 with helper deficiency
   \(C_H\);
2. a \(g\)-edge matching of the same graph \(R_{\rm lit}-P\) assigns
   private helpers to \(g\ge|S|-C_H\) sources, and its complete selected
   bundle family, not merely each edge separately, is jointly materialized
   and fully replayed in the child used below;
3. all \(q\) lost matching units and the \(g\) gain units form one
   same-child claim bank with gammoid deficiency at most \(C_G\), certified
   by (3.6), or by the prefix-pair rows (6.4);
4. every remaining non-supplier casualty satisfies
   \(c_{\rm ns}\le\theta g+b_{\rm ns}\), where
   \(0\le\theta<1\); and
5. the complete potential obeys (4.5).

Then

\[
 \boxed{
 \Phi'\le
 [1-\alpha(1-\theta)]\Phi
 +(1-\theta)(b_0+C_H)+C_G+b_{\rm ns}.
 }                                                       \tag{8.2}
\]

In particular, if \(\alpha=1\), \(\theta=0\), and
\(b_0,C_H,C_G,b_{\rm ns}=O(1)\), the child has
\(\Phi'=O(1)\) in one transition.

#### Proof

Theorem 4.1 gives \(p-q\ge g-C_G\).  Therefore (4.5) and item 4 give

\[
 \Phi'\le\Phi-(1-\theta)g+C_G+b_{\rm ns}.
\]

Use \(g\ge\alpha\Phi-b_0-C_H\). \(\square\)

For the exact iteration consequence, suppose (8.2) regenerates for
\(N=N(k)\) consecutive same-parity transitions, its additive term is at
most \(D=O(1)\), and

\[
 0<\lambda:=\alpha_0(1-\theta_0)\le
 \alpha_i(1-\theta_i)\le1
 \qquad(0\le i<N).                                   \tag{8.3}
\]

Then

\[
 \boxed{
 \Phi_N\le(1-\lambda)^N\Phi_0+\frac{D}{\lambda}.
 }                                                       \tag{8.4}
\]

This follows by iterating (8.2) and bounding the resulting geometric sum.

If some \(\alpha_i(1-\theta_i)>1\), nonnegativity of the next potential
and (8.2) instead force that parent potential to be bounded by the additive
term divided by \(\alpha_i(1-\theta_i)-1\).  Thus, for terminal word cost
\(B(k)+A\Phi_N+C_{\rm term}\), the exact remaining quantitative condition
is either the one-step reset above or

\[
                  (1-\lambda)^{N(k)}\Phi_0(k)=O(1).   \tag{8.5}
\]

Together with \(A=O(1)\), \(C_{\rm term}=O(1)\), and a valid even
terminal-child transfer on the same spine, (8.5) gives \(B(k)+O(1)\).

## 9. Exact present boundary

The following ingredients are proved independently:

* the same-child matching and gammoid identities of Sections 1, 3 and 4;
* the primitive and shared-helper obstructions of Section 2;
* the odd-central proper-shore expansion and Theorem 5.1;
* the two-ray prefix uncrossing of Section 6;
* the K17 helper-ID Hall calibration of Section 7;
* the exact single-helper three-mode no-go and bilateral-source-support
  invariant of Section 7;
* the mixed-coatom packet's local owner, immediate-palette, upper,
  residence and topology transparency; and
* the bounded-eviction implication once a complete bounded damage set is
  supplied.

The following rows are **UNPROVED**:

1. a literal all-\(k\) bounded-size rescue-module relation satisfying (5.3),
   or any equally strong near-perfect Hall row at every required layer;
2. an extensive bank of prepared, mutually private terminally closed rescue
   modules in one Pascal child;
3. simultaneous root/common-basis materialization and full supplier replay
   of that bank;
4. occurrence-labelled supplier-port nesting (6.1), or the general
   trapped-menu cuts (3.6), with uniform constants;
5. a complete all-resource casualty estimate with \(\theta<1\);
6. regeneration of the same private module class at the next same-parity
   child; and
7. co-instantiation of these rows on one compatible odd spine and its even
   terminal children; and
8. enough regenerated transitions to satisfy (8.5), unless the one-step
   reset parameters \(\alpha=1,\theta=0\) are obtained.

Therefore Theorem 8.1 is a sharper sufficient route to an unconditional
\(B(k)+O(1)\), not such a theorem itself.

Proof-bearing inputs:

MATH_THEOREM_ADAPTIVE_PROTECTED_RECOURSE_DEFICIENCY_CONTRACTION_20260803.md

MATH_THEOREM_K17_DEF21_DM_CUT_CREDIT_AND_COMMON_HELPER_NOGO_20260803.md

MATH_THEOREM_K17_DROP12_COMMON_COMMON_HALL_NOGO_AND_CROSS_HOST_PAIR_RECOURSE_20260803.md

MATH_THEOREM_K17_DROP12_COMPLETE_ANCHORED_SOURCE_PARTNER_OCCURRENCE_NOGO_20260803.md

MATH_THEOREM_K17_DROP12_THIRD_MODE_NATIVE_P0_APERTURE_SCREEN_20260803.md

MATH_THEOREM_K17_DROP12_MINIMAL_THREE_MODE_DIRECTED_RESCUE_20260803.md

MATH_THEOREM_K17_DROP12_H_SOURCE_TRIPLE_APERTURE_JOIN_FACTORIZATION_20260803.md

MATH_AUDIT_K17_DROP12_H_SOURCE_TRIPLE_FACTORIZATION_INDEPENDENT_20260803.md

MATH_THEOREM_ROTOR_ODD_COATOM_ONECOPY_AND_PROTECTED_OWNER_CIRCUITS_20260802.md

MATH_THEOREM_INDEPENDENT_COATOM_TWO_CHAIN_PROVIDER_SWITCH_AND_SERIAL_LAMBDA_GATE_20260801.md

MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md

MATH_THEOREM_O1_ZERO_DEFECT_COATOM_TEMPLATE_REGENERATION_AND_MENU_QUANTIFIER_20260801.md

MATH_THEOREM_BOUNDED_COMPILER_EVICTION_AND_PHASE_DECOUPLING_20260801.md
