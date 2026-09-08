# Prospective square-collar planting is a factor problem, not an old-phase Hamilton problem

Date: 2026-08-01  
Lane: additive-constant q1/topology interface  
Status: exact conditional planting and endpoint-debt theorem; exact
fixed-Hamilton menu obstruction; positive finite `ML(7)` calibration.  No
all-dimensional rooted-target theorem is claimed.

## 0. Outcome

The old square-collar phase cannot be required to lie in a Hamilton cycle:
it contains the saturated physical cycle

\[
                         E-F-X-Y-E.                       \tag{0.1}
\]

The correct prospective object is instead either

1. a q1-rainbow Hamilton cycle containing the **all-plus** paths, which is
   then toggled backwards to create the named old sidecars; or
2. more weakly, a q1-rainbow source factor containing the old sidecars,
   followed by the all-plus toggles and an unrestricted q1 alternating
   reset.

The first route has an exact bounded endpoint ledger.  From a Hamilton
target containing `H` disjoint all-plus collars, the reverse toggles produce
exactly `H` private old `C4` sidecars and a residual two-factor with at most
`H+1` cycles.  Cutting one common, nonpacket edge in each residual cycle
gives

\[
 \begin{array}{c|c}
 \text{old state}&H\text{ named }C_4\text{s plus a linear forest},\\
 \text{all-plus state}&\text{a linear forest with }r\le H+1\text{ paths},
 \end{array}                                               \tag{0.2}
\]

and both states miss exactly the same `r` named lower-q1 colours.  Thus the
old phase is never put inside one Hamilton cycle.

The raw `Theta(m^4)` collar menu does **not** prove the prospective
Hamilton target.  On the odd Middle Levels host, a fixed directed Hamilton
cycle contains at most one collar from the entire fixed-oriented-target
menu.  The Hamilton cycle and the collar parameters must therefore be
chosen jointly; post-target forbidden-incidence abundance is unavailable.

The first finite case is positive.  At `m=4` an explicit `ML(7)` Hamilton
cycle contains the canonical all-plus collar.  Reversing it gives component
sizes `4+6+25`; two common cuts give old profile `C4+P6+P25` and all-plus
profile `P7+P28`, with exactly the same `33` retained lower-q1 colours.

## 1. The collar on the odd q1 host

Let `Gamma` have size `2m-1`, and work in `J(Gamma,m)`.  Fix an oriented
target

\[
 e=(L,U,E,F),\qquad |L|=m-1,\quad
 E=L+d,\quad F=L+a,\quad U=L+a+d.                         \tag{1.1}
\]

Choose ordered distinct labels

\[
 b,x\in L,\qquad c,y\in\Gamma\setminus U.                 \tag{1.2}
\]

Define

\[
\begin{array}{llll}
 A=U-b,&B=L-b+a+c,&C=L-b+c+d,&D=L+c,\\
 X=L-x+a+y,&Y=L-x+d+y.&&
\end{array}                                                \tag{1.3}
\]

The two phases are

\[
\begin{aligned}
 G^-={}&\{AB,CD,EF,FX,XY,YE\},\\
 G^+={}&\{AF,CB,ED,FX,XY,YE\}.                            \tag{1.4}
\end{aligned}
\]

They have the same six lower colours, six upper colours, six tails and six
heads.  Their physical shapes are

\[
 G^-=C_4(E,F,X,Y)\sqcup P_1(A,B)\sqcup P_1(C,D),
\quad
 G^+=P_5(A,F,X,Y,E,D)\sqcup P_1(C,B).                    \tag{1.5}
\]

The even-ground count in the original square-collar theorem must not be
copied literally here.  Since

\[
 |L|=m-1,\qquad |\Gamma\setminus U|=m-2,                  \tag{1.6}
\]

the exact odd-host menu size is

\[
 M_m=(m-1)(m-2)\,(m-2)(m-3)
     =(m-1)(m-2)^2(m-3)=\Theta(m^4).                     \tag{1.7}
\]

The anchors must be separated from the optional resources in this load
statement.  Every option contains the owners `E,F`, the lower colour `L`,
and the upper colour `U`; each of those mandatory anchors therefore has
load exactly `M_m`, not `O(m^3)`.  After declaring these anchors (including
their tail/head roles) mandatory and pairwise private across the target
bank, one fixed **nonanchor** typed resource or owner excludes only
`O(m^3)` menu items.  Hence a fixed bank of anchor-private targets admits
pairwise resource- and owner-disjoint formal collars for all sufficiently
large `m`.  This is a formal packet-bank statement, not yet a factor
embedding.

## 2. The exact prospective all-plus theorem

Orient a q1-rainbow Hamilton cycle `C` cyclically.  Say that a collar is
**aligned in `C`** when all six directed arcs of `G+` occur in `C`; in
particular

\[
 A\to F\to X\to Y\to E\to D,\qquad C_{\rm role}\to B     \tag{2.1}
\]

have the displayed cyclic directions.  The subscript distinguishes the
owner role `C_role` from the Hamilton cycle `C`.

### Theorem 2.1 (prospective sidecar extraction)

Let a directed q1-rainbow Hamilton cycle `C` contain `H` pairwise
vertex-disjoint aligned all-plus collars \(G_i^+\).  When the collars are used
as ordered four-resource packets, assume in addition that their complete
typed supports are pairwise disjoint (the q1 Hamilton hypothesis already
forces the lower, tail and head parts; upper-resource privacy is extra).
Reverse all `H` collar toggles.  Then:

1. the result contains the `H` intended private cycles
   `E_i-F_i-X_i-Y_i-E_i`, and no other component meets their vertices;
2. after deleting those `4H` sidecar vertices, the remaining graph is a
   two-factor with at most `H+1` cycles;
3. every residual cycle contains an edge of the original Hamilton cycle
   outside all packet supports; and
4. one may cut `r<=H+1` such common edges, one per residual cycle, so that
   the old state is the `H` named sidecars plus a linear forest and the
   all-plus state is `C` minus those same `r` edges.

The two cut states have the same lower-q1 support, namely the complete q1
palette minus the `r` distinct cut colours.  In particular the named q1
endpoint debt is at most `H+1`.

#### Proof

For one collar, the reverse toggle detaches

\[
                       F-X-Y-E+EF                         \tag{2.2}
\]

as the private `C4`.  Contract the long all-plus path from `A` to `D` to
one macro edge.  On the remaining vertices the reverse toggle is exactly
the two-switch

\[
                   \{AD,C_{\rm role}B\}
          \longmapsto
                   \{AB,C_{\rm role}D\}.                 \tag{2.3}
\]

This is a literal set exchange, not a multigraph shorthand.  The three
old-only edges `AB,CD,EF` have the same three distinct lower-q1 colours as
the three plus-only edges `AF,CB,ED`.  Since `C` already contains the
plus-only triple and is q1-rainbow, it contains none of the old-only triple.
Thus the reverse toggle really deletes the displayed plus edges and inserts
new physical edges.

The packet supports are vertex-disjoint, so these switches commute.  A
two-switch changes the number of cycles of a two-factor by at most one.
Starting from the single macro cycle obtained from `C`, after `H` switches
there are therefore at most `H+1` residual cycles.

The inserted edges `AB` and `C_role D`, over all packets, form a physical
matching.  No residual cycle can consist only of these inserted edges,
because a matching has degree at most one.  Thus every residual cycle has
an unchanged `C` edge outside the packet supports.  Cut one such edge in
each cycle.  The reverse-toggle state now has the `H` untouched sidecar
cycles and a residual linear forest.  Forward toggling restores `C` while
leaving the cuts fixed, hence gives the path forest `C-K`, where `|K|=r`.

The collar phases have identical lower-q1 resources.  The common cut edges
are outside the toggles, and a q1-rainbow Hamilton cycle has distinct edge
colours.  Both cut states therefore retain precisely all q1 colours except
the `r` colours of `K`.  This proves the theorem. \(\square\)

### Upper-witness scope

The six immediate upper resources inside each collar are identical between
the two phases.  A named adjacent-upper witness carried by a common,
uncut edge also survives literally.  If one cannot choose every cut away
from named witness edges, at most `r<=H+1` such edge occurrences are lost;
recreating them is a separate bounded task.  Nothing in Theorem 2.1
preserves interval witnesses of width at least two, residence, or a common
compiler cap.

## 3. Why the raw menu does not prove the rooted target

### Theorem 3.1 (fixed-Hamilton menu collapse)

Fix the oriented target (1.1) and a directed Hamilton cycle `C`.  At most
one of the `M_m` indexed odd-host collars has `G+ subset C`.  If the
orientation of the target edge `EF` is forgotten, the two orientations
give at most two indexed collars in total.

#### Proof

Let `s` be the successor map of `C`.  An aligned `G+` forces

\[
 A=s^{-1}(F),\quad X=s(F),\quad Y=s^2(F),\quad
 E=s^3(F),\quad D=s(E).                                  \tag{3.1}
\]

Consequently the parameters, if legal, are forced:

\[
 b\text{ is the unique element of }U\setminus A,\quad
 x\text{ is the unique element of }F\setminus X,\quad
 y\text{ is the unique element of }X\setminus F,\quad
 c\text{ is the unique element of }D\setminus L.         \tag{3.2}
\]

The remaining arc `C_role -> B` is only a consistency check.  Hence there
is zero or one indexed collar for the fixed orientation.  Reversing the
orientation of `EF` supplies the only second possibility. \(\square\)

Thus (1.7) is a menu available **before** the target cycle is chosen.  It
cannot be combined with a fixed-Hamilton forbidden-resource union bound:
the rooted sublist has size at most one, not `Theta(m^4)`.

## 4. The weaker factor-first route is an exact b-flow

The clarification that the old state may be a sidecar factor, rather than a
Hamilton cycle, gives a strictly weaker central route.

Let \(P^-\) be the incidence lift in `ML(Gamma)` of a private old collar bank.
For every owner or lower-colour vertex `v`, put

\[
                         b(v)=2-\deg_{P^-}(v).             \tag{4.1}
\]

Delete the used incidences of \(P^-\), obtaining the residual bipartite graph
`R`.  An **undirected** q1-rainbow spanning factor containing all old
collar edges exists iff `R` has a simple bipartite b-factor of degrees
(4.1).  This statement deliberately forgets the planted tail/head
orientations.

### Proposition 4.1 (exact min-cut row)

Write `O` for the rank-`m` owner shore and `Q` for the rank-`m-1` colour
shore, and put

\[
             N=|O|=|Q|={2m-1\choose m}.                 \tag{4.2}
\]

For a private `H`-collar bank,

\[
                       b(O)=b(Q)=2N-12H.                  \tag{4.3}
\]

The desired source factor exists iff, for every `S subset O` and
`T subset Q`,

\[
                  e_R(S,Q\setminus T)+b(T)\ge b(S).       \tag{4.4}
\]

When an orientation-compatible completion exists, toggle all collars to
plus.  The result is again a q1-rainbow spanning factor.  The unrestricted
q1 alternating-circuit reset then Hamiltonizes it, and opening one protected
terminal edge leaves one lower-q1 endpoint colour.

#### Proof

Each old collar already uses twelve incidence edges.  Its six lower-colour
vertices have degree two in \(P^-\); its four sidecar owners have degree two;
and the four endpoints of `AB,CD` have degree one.  This subtracts twelve
from the degree demand on each shore, proving (4.3).

Build the standard flow network with arcs `source -> O` of capacity and
demand `b(u)`, residual incidence arcs of capacity one, and arcs
`Q -> sink` of capacity and demand `b(q)`.  A cut with owner part `S` and
colour part `T` has capacity

\[
        b(O\setminus S)+e_R(S,Q\setminus T)+b(T).
\]

Max-flow/min-cut gives (4.4), and bipartite-flow integrality gives a literal
b-factor.  Adding \(P^-\) produces the source **undirected** q1 two-factor.
The collar identity preserves every lower q1 colour through the all-plus
toggle.  If the source components admit orientations agreeing with all
planted arcs, this is also a legal ordered source state.  The unprotected q1
reset theorem then applies to the resulting spanning factor and may retain
one chosen opening edge. \(\square\)

The missing orientation row is real.  Two planted directed edges on one
undirected cycle may demand opposite cyclic orientations.  An exact ordered
formulation uses binary variables

\[
 z_{q,u,v}\qquad(q\subset u,v,\ |q|=m-1,\ |u|=|v|=m,
                       \quad u\ne v),                     \tag{4.5}
\]

where `z_(q,u,v)=1` selects the directed Johnson arc `u -> v` of colour
`q`.  The constraints are

\[
 \sum_{u,v}z_{q,u,v}=1\quad(\forall q),\qquad
 \sum_{q,v}z_{q,u,v}=1\quad(\forall u\text{ as tail}),\qquad
 \sum_{q,u}z_{q,u,v}=1\quad(\forall v\text{ as head}),    \tag{4.6}
\]

with every planted old arc fixed to one.  Equivalently, one needs two
edge-disjoint incidence perfect matchings, one for tails and one for heads,
extending the planted partial matchings.  This ordered completion is a
strictly stronger gate than (4.4); the ordinary b-flow is not a typed
tail/head theorem.

This route proves only the immediate-lower q1 row after the unrestricted
reset.  The reset may destroy named adjacent-upper witnesses, deeper
interval witnesses, residence, or compiler structure.  Those guards need
a rooted terminal target or separate protected records.

## 5. Exact `m=4` calibration

Use `Gamma={0,...,6}`, owner rank four, and

\[
 L=\{0,1,2\},\quad (a,d,b,x,c,y)=(3,4,0,1,5,6).          \tag{5.1}
\]

The audit artifact supplies an explicit alternating `ML(7)` Hamilton cycle
whose Johnson projection contains all six aligned arcs of `G+`.  It checks:

* all `35` lower-q1 colours occur exactly once;
* reverse toggling has component profile `4+6+25`, with the four-component
  exactly `\{E,F,X,Y\}`;
* cutting the common edges `(27,75)` and `(39,45)` gives old profile
  `C4+P6+P25` and all-plus profile `P7+P28`;
* both cut states contain the same `33` lower-q1 colours;
* the odd-host target menu has size `12`, and exactly one of those twelve
  collars occurs in the displayed directed Hamilton cycle; and
* the six local adjacent-upper witnesses are distinct and equal between
  phases.

This is a positive base fixture, not an all-`m` induction.

## 6. Exact remaining theorem

There are now two sharply separated targets.

1. **Strong rooted route.**  For every fixed `H` and sufficiently large
   `m`, choose one option from each private odd-host collar menu and one
   directed q1-rainbow Hamilton cycle containing all `H` aligned all-plus
   motifs.  Theorem 2.1 then gives at most `H+1` named q1 cuts and preserves
   the packet's immediate upper resources.
2. **Weak factor route.**  Choose the old collar options so that the exact
   cut inequalities (4.4) hold.  This suffices for q1 after an unrestricted
   reset, but not for protected upper/residence/compiler rows.

Neither follows from the raw `Theta(m^4)` menus: Theorem 3.1 is the precise
type/count obstruction.  Conversely, the `m=4` fixture shows that this is
not a local incompatibility of the collar shape with Middle Levels
Hamiltonicity.  The missing result is a genuinely prospective, correlated
selection theorem (or a recursive construction), not another post-hoc
extension of a frozen Hamilton target.

## 7. Replay

Run

```text
python3 scratch/audit_o1_odd_square_collar_rooted_ml7_20260801.py
```

The replay writes

```text
scratch/o1_odd_square_collar_rooted_ml7_20260801.audit.json
```

and checks the literal fixture and all finite claims listed in Section 5.
