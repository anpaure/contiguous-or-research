# The fixed parameter-three actuator embeds in fixed four-uniform side hosts, but its protected root cylinder does not follow from common-basis marginals

Date: 2026-07-31  
Status: exact dimension-uniform fixed-4 embedding, exact slot/root/graphic
guard, exact constant-risk raw atlas, and sharp common-basis/compiler interface.
No all-parameter rooted absorber atlas, exact cover-down, or word compiler is
claimed.

## 0. Verdict

The parameter-three AGCF `2 -> 3` actuator should not be suspended as a
whole complement path when it is used on a side shore.  Its **fixed active
six-coordinate body** already has a genuine dimension-uniform embedding in
the four-uniform side-slot host: add a common spectator core to every active
set and atomize each Johnson edge separately.  The packet then has

\[
                         6\longrightarrow9
\]

fixed-4 atoms, hence gain three, in every ambient dimension.  It adds three
previously uncovered colours on each outer palette.  Its unlabelled closed
support has only

\[
                  9+9+12=30
\]

rank-set resources and at most `42` occurrence-labelled host vertices after
all owner slots are closed.  A symmetry-greedy raw atlas therefore has
linear order in the side target size `P`.

This positive embedding does **not** yet give the all-guard protected
absorber requested by exact recursion.  The precise boundary is:

1. seven of the twelve physical owners must be ordinary capacity-two
   owners;
2. graphic compatibility is automatic only on the face with exactly one
   seam root on each of the two old and three new paths;
3. on that face the fixed anchor bank must realize one of four exact
   positive/negative cylinders on the twelve owners, and the third new path
   necessarily consumes the new root `045`;
4. the ordered tail/head lift transports one head hole instead of having a
   nonnegative boundary on all four ordered shores; and
5. four of the six inherited pointwise cap assignments change.  Local
   Boolean cap existence is automatic, but a protected downstream compiler
   trace is not supplied.

The balanced common-basis theorem controls every one-point marginal and is
enough to prove that the **negative** puncture/cap risk of a fixed packet is
`O(1/n)`.  It gives no lower bound for the positive root cylinder, even for
two partition matroids.  Therefore the current ingredients prove a
constant-support palette/slot absorber and a conditional rooted absorber,
not a rooted private atlas.  The missing statement is a packet-indexed
common-basis cylinder or an explicit long-ear gluing theorem which supplies
the roots and compiler trace after the local switches.

## 1. The fixed active packet

Use active coordinates `012345`.  The two off paths are

\[
\begin{array}{c|cccc}
 P_1&012&123&234&345\\
 P_2&014&024&025&235,
\end{array}                                                    \tag{1.1}
\]

and the three on paths are

\[
\begin{array}{c|cccc}
 Q_1&012&124&234&345\\
 Q_2&014&015&025&235\\
 Q_3&123&023&024&045.
\end{array}                                                    \tag{1.2}
\]

For adjacent rank-three sets `X,Y`, write

\[
              a(X,Y)=(X\cap Y,X\cup Y,X,Y).             \tag{1.3}
\]

The first two coordinates are the lower and upper outer colours.  The last
two may be read either as ordered tail/head resources or as the two physical
owners whose slot incidences are used.

Let `A_off` and `A_on` be the six and nine atoms obtained from (1.1) and
(1.2).  Each phase is a matching separately on the lower, upper, tail and
head shores.  On the two outer shores one has the **positive** identities

\[
\begin{aligned}
 L(A_{\rm off})={}&\{12,23,34,04,02,25\},\\
 L(A_{\rm on})={}&L(A_{\rm off})\mathbin{\dot\cup}\{24,01,05\},\\[1mm]
 U(A_{\rm off})={}&\{0123,1234,2345,0124,0245,0235\},\\
 U(A_{\rm on})={}&U(A_{\rm off})
       \mathbin{\dot\cup}\{0145,0125,0234\}.          \tag{1.4}
\end{aligned}
\]

Thus this is a gain-three fixed-4 packet, not merely an equality circuit.
It absorbs exactly three lower and three upper outer defects.

### Proposition 1.1 (exact physical degree ledger)

The physical degrees differ only as follows:

\[
\begin{array}{c|ccccc}
 x&123&124&015&023&045\\ \hline
 d_{\rm off}(x)&2&0&0&0&0\\
 d_{\rm on}(x) &1&2&2&2&1.
\end{array}                                                   \tag{1.5}
\]

Every other owner keeps its degree.  Consequently the owners which must
have residual capacity two in **both** phases are exactly

\[
       I=\{123,234,024,025,124,015,023\}.                \tag{1.6}
\]

The union of the two owner banks has order twelve.

#### Proof

Count path incidences in (1.1)--(1.2).  Each endpoint has degree one and
each internal path vertex degree two.  The common vertices other than `123`
retain the same endpoint/internal status.  The vertex `123` changes from an
internal vertex of `P_1` to the first endpoint of `Q_3`; the other four
displayed vertices are new.  This proves (1.5)--(1.6).  The total degree
gain is `7-1=6`, as required by three new fixed-4 atoms. `square`

In particular the packet is cap-safe after deleting its off atoms whenever
all slots at its twelve owners have been closed against the outside support,
the owners in (1.6) are ordinary, and any cap-one owner is used only as an
endpoint.  The common physical atoms `234-345` and `025-235` may retain their
slot labels; the other labels can be assigned independently along the five
paths.

## 2. Dimension-uniform spectator embedding

Let the ambient side parameter be `r>=4`, on a ground set of order `2r`.
Choose the six active coordinates above.

### Theorem 2.1 (minus-shore embedding)

Choose a spectator set `S` of order `r-4`, disjoint from the active six,
and replace every active set `X` by

\[
                            \widehat X=S\cup X.          \tag{2.1}
\]

Then (1.1)--(1.2) become legal fixed-4 side packets with owner, lower and
upper ranks

\[
                         r-1,\quad r-2,\quad r.          \tag{2.2}
\]

Thus they embed in the minus capacity-slot shore at parameter `r`.

### Theorem 2.2 (plus-shore embedding)

If instead `|S|=r-2`, the same rule gives owner, lower and upper ranks

\[
                         r+1,\quad r,\quad r+2,          \tag{2.3}
\]

and embeds the packet in the plus shore.  Both constructions fit in the
`2r`-point ground set for every `r>=4`.

#### Proof of Theorems 2.1--2.2

For sets containing the same spectator core,

\[
\begin{aligned}
 (S\cup X)\cap(S\cup Y)&=S\cup(X\cap Y),\\
 (S\cup X)\cup(S\cup Y)&=S\cup(X\cup Y).              \tag{2.4}
\end{aligned}
\]

Adding `r-4` to the active ranks `(2,3,4)` gives (2.2); adding `r-2`
gives (2.3).  The used coordinate counts are `r+2` and `r+4`, both at most
`2r` for `r>=4`.  Equation (2.4) carries every identity and degree ledger
from Section 1 unchanged. `square`

This is the genuine dimension-uniform embedding.  Appending the growing
`F -> G` tail from the whole-path AGCF suspension is unnecessary here and
would obscure the fixed support.

## 3. Exact root and graphic face

Let `R` be the cap-one seam-anchor set on the chosen physical shore.  On the
twelve packet owners, impose both:

* every internal owner of either phase is outside `R`; and
* every path component of both phases contains exactly one endpoint in
  `R`.

### Theorem 3.1 (twelve-owner root cylinder)

The preceding conditions hold if and only if, after suppressing the common
spectator core,

\[
 R\cap X_{\rm packet}\in
 \left\{
 \begin{array}{l}
 \{012,014,045\},\quad\{012,235,045\},\\
 \{345,014,045\},\quad\{345,235,045\}.
 \end{array}\right.                                      \tag{3.1}
\]

In particular the third on path forces the fresh root `045`.  The two old
roots are preserved on `Q_1,Q_2`.

#### Proof

The first old path and `Q_1` have the common endpoint pair
`{012,345}`; exactly one must be selected.  Likewise the second old path
and `Q_2` require exactly one of `{014,235}`.  The endpoints of `Q_3` are
`{123,045}`, but `123` is internal in the off phase and hence cannot be a
cap-one owner.  Thus `045` is forced.  All seven internal owners are then
excluded, giving exactly (3.1). `square`

### Corollary 3.2 (automatic graphic and short-cycle guard on this face)

Suppose the fixed central/seam scaffold is a forest and the nonroot packet
owners are closed against every exterior side atom.  Under (3.1), replacing
the two off paths by the three on paths preserves acyclicity and creates no
projected short-cycle configuration.

#### Proof

Each phase is a vertex-disjoint union of paths.  Every path meets the fixed
scaffold at exactly one cap-one root.  Hence each is attached to the
scaffold as a pendant tree, and repeated pendant-tree attachment cannot
create a cycle.  Closing the other owners excludes a mixed exterior cycle.
`square`

The one-root hypothesis is load-bearing.  With two roots, a packet path is
an ear between two contracted scaffold components and must pass the ordinary
graphic loop/circuit test; with no root it remains an anchor-free component.
Thus the local packet does not make the contracted graphic row automatic
off the face (3.1).

## 4. A constant-size raw private atlas

Ignore punctures and anchor labels temporarily.  A packet's unlabelled
closed support contains exactly

\[
        9\text{ lower colours},\quad9\text{ upper colours},
             \quad12\text{ owners}.                         \tag{4.1}
\]

Closing both slots at every owner uses at most `42` host vertices.  On the
rooted face (3.1), the three roots have one residual slot and the other nine
owners have two, giving `9+9+21=39`.

Let `O_r` be the coordinate-permutation orbit of one minus-shore lift.  Put

\[
 P_r={2r\choose r-2},\qquad
 M_r={2r\choose r},\qquad
 N_r={2r\choose r-1}.                                  \tag{4.2}
\]

Every lower colour lies in exactly `9|O_r|/P_r` supports, every upper colour
in `9|O_r|/M_r`, and every owner in `12|O_r|/N_r`.

### Proposition 4.1 (raw private packing)

The orbit contains a pairwise unlabelled-resource-disjoint family of order
at least

\[
 \left\lceil
 {1\over 81/P_r+81/M_r+144/N_r}
 \right\rceil
 \ \ge\ \left\lceil {P_r\over306}\right\rceil .       \tag{4.3}
\]

The complement-dual plus shore has the same bound.

#### Proof

The group is transitive on every rank shore, so the displayed support
degrees follow by double counting.  A fixed support meets at most the sum
of `d(v)-1` over its `9+9+12` resources.  Therefore its intersection-graph
degree plus one is at most

\[
 |O_r|\left(81/P_r+81/M_r+144/N_r\right).
\]

Greedy independent-set packing gives the first bound.  Since
`M_r,N_r>=P_r`, the denominator is at most `306/P_r`. `square`

Thus lack of raw packets is not the obstruction.

## 5. Negative puncture risk is controlled by one-point marginals

Assume the balanced strict-common-basis law is available at parameter `r`.
Every child edge then has marginal

\[
 \theta_r={C_r\over N_r}
       ={2(2r+1)\over r(r+2)}=O(1/r),                 \tag{5.1}
\]

where `C_r=Cat_(r+1)`.  The endpoint and turn maps of the child linear
forest are injective on the relevant images.

For a fixed minus-shore packet, its nine upper colours must avoid the
puncture bank `h(Q)`, and its seven internal owners must avoid the anchor
bank `L(Q)`.  Each forbidden rank set is the image of at most one child
edge.  Hence the union bound gives

\[
 \Pr(\text{palette and capacity clean})
                      \ge 1-16\theta_r.                \tag{5.2}
\]

The plus-shore statement is the complement-dual one, using `t(Q)` and
`U(Q)`.  Requiring that the two unchosen endpoint roots also remain ordinary
changes `16` to `18`.  Consequently, for any fixed raw private atlas from
Proposition 4.1, some common basis in the balanced distribution leaves at
least a `(1-16 theta_r)` fraction of its packets palette/cap clean whenever
the right side is positive.

This is the promised **constant puncture-risk** statement.  It is only a
negative-avoidance statement; it does not select the positive roots.

## 6. Why balanced marginals do not supply the rooted atlas

The rooted event (3.1) requires three specified owners in the anchor image
and the other nine packet owners out, simultaneously with the nine outer
puncture exclusions.  Equal one-point marginals imply no positive lower
bound for such a cylinder.

The failure already occurs for common bases of two partition matroids.
On ground `{0,1,2,3}`, let the first partition have blocks

\[
                     \{0,2\},\{1,3\},
\]

and the second have blocks

\[
                     \{0,3\},\{1,2\}.
\]

Their common bases are exactly `{0,1}` and `{2,3}`.  The uniform law on
them has marginal `1/2` at every element, while

\[
                 \Pr(0\in Q,\ 1\notin Q)=0.             \tag{6.1}
\]

Thus even one positive and one negative condition can be locked despite
perfectly balanced common-basis marginals.  A fortiori (5.1) does not imply
the twelve-owner cylinder (3.1).  If the two old rooted paths are preloaded,
the only new positive requirement is the root `045`, but its conditional
probability after the capacity and puncture exclusions is still not
controlled by one-point marginals.

There is also a sharp scale warning.  A resource-private packet bank on the
automatic graphic face uses three distinct roots per on-state packet, so
its order is at most `C_r/3` and its total gain at most `C_r=Theta(P_r/r)`.
The local rooted packet is therefore a Catalan-scale finisher, not by itself
a mechanism which repairs an arbitrary `Theta(P_r)` leave.  Using a linear
raw atlas requires a later gluing theorem which attaches or merges its
temporarily unrooted path segments without spending one private root per
segment.

## 7. Ordered-four-transversal and compiler-cap mismatch

In the ordered atom interpretation, the tail shore has the positive
boundary

\[
 T(A_{\rm on})=T(A_{\rm off})
              \mathbin{\dot\cup}\{124,015,023\},       \tag{7.1}
\]

but the head shore satisfies

\[
 H(A_{\rm on})=
   \bigl(H(A_{\rm off})\setminus\{123\}\bigr)
       \mathbin{\dot\cup}\{124,015,023,045\}.          \tag{7.2}
\]

Hence the packet is a legal `6 -> 9` ordered-matching exchange only when
the four added heads are free and `123` is allowed to become a head hole.
It is not a nonnegative-boundary absorber for a pointwise protected head
leave.  The untagged AGCF middle-resource identity hides this one-unit head
transport.

The outer common-cap map changes as well.  Of the six inherited lower
colours, only

\[
             34\mapsto2345,\qquad25\mapsto0235          \tag{7.3}
\]

are preserved.  The other four change:

\[
\begin{array}{c|cc}
 D&\text{off cap}&\text{on cap}\\ \hline
 12&0123&0124\\
 23&1234&0123\\
 04&0124&0245\\
 02&0245&0234.
\end{array}                                             \tag{7.4}
\]

Therefore:

* after a complete palette/slot/forest switch, the **existential Boolean**
  two-step cap is automatic by the fixed-4 common-cap theorem;
* a pointwise cap map protected on all inherited rows rejects this packet;
  and
* no maximal-envelope or downstream word-compiler cap follows from the
  local packet.  Such a use requires an explicitly exported trace-guarded
  packet bank which accepts the four changes in (7.4).

This is a type mismatch, not a finite search failure: the AGCF resource
column has no tail/head split, no fixed seam-root cylinder, and no compiler
trace coordinate.

## 8. Exact conditional interface and remaining theorem

The fixed parameter-three packet is a valid protected fixed-4 absorber in a
given side host provided all of the following are supplied externally:

1. all nine on-state values of each outer palette survive the fixed
   punctures;
2. the anchor intersection on its twelve owners is one of (3.1), with all
   owner slots closed outside the named roots;
3. the off paths are isolated pendant components of the retained scaffold,
   or the more general contracted graphic test is verified explicitly;
4. in the ordered model, the head-hole transport (7.2) is accepted; and
5. the selected compiler bank accepts the cap remapping (7.4).

Under these hypotheses, any pairwise closed-support-disjoint family of the
packets is serializable in arbitrary order, preserves every exterior palette,
slot and protected scaffold incidence, and gains three atoms per packet.

The weakest missing positive theorem is consequently not another local
actuator identity.  It is either:

* a packet-indexed common-basis theorem giving many cylinders (3.1) together
  with the nine puncture exclusions and a trace guard; or
* a Catalan-scale long-ear system which starts from the palette/cap-clean raw
  atlas of Sections 4--5, attaches its unrooted components through a
  contracted graphic forest, performs the head-hole transport, and exports
  the compiler cap.

One-point common-basis marginals alone cannot prove either statement.

### 8.1 Exact C6-target-bank / sparse-rerouter template

The native fixed-4 incidence hexagon gives a cleaner unit boundary than the
three-unit packet above.  In the notation of

```text
MATH_THEOREM_CATALAN_ML_HEX_FIXED4_SUSPENSION_AND_FULL_GUARD_MISMATCH_20260731.md
```

one full hex has equal-incidence phases

\[
                       E_t^0=\{t\}\mathbin{\dot\cup}B_t^-,
            \qquad E_t^1=B_t^+,                       \tag{8.1}
\]

so `B_t^- -> B_t^+` has the positive boundary of the one target atom `t`.
This leads to the following exact target-bank formulation.

Fix `Q`, delete the affine slot baseline `S_0`, and let `Ghat_Q=G_Q-S_0`.
Choose a pairwise support-disjoint target bank `T` together with its C6 off
and on phases.  A DP near-forest `M` is **target aligned** when, for some
`J subseteq T`,

\[
 \operatorname {Leave}_{\widehat G_Q}(M)
       =\mathbin{\dot\bigcup}_{t\in J}\operatorname {inc}(t),
 \qquad
       \mathbin{\dot\bigcup}_{t\in J}B_t^-\subseteq M.  \tag{8.2}
\]

Equation (8.2) is literal on both outer palettes and on occurrence-labelled
slots.  If the final on phases also pass the contracted graphic/root and
compiler rows, simultaneous switching fills the leave exactly.

The sparse Boolean `ell <-> ell` cycles of

```text
MATH_THEOREM_CATALAN_SPARSE_FIVE_CYCLE_PHYSICAL_SWITCH_20260731.md
```

are the correct intermediate rerouters.  Every such cycle has zero boundary
on both outer palettes but a generally nonzero signed slot/owner boundary.
For chosen rerouters `R_j^- -> R_j^+`, measure the following slot leave in
the full host `G_Q` (equivalently delete the `S_0` term and measure it in
`Ghat_Q`).  The exact alignment equation is

\[
 \operatorname {Leave}^{G_Q}_{\rm slot}(M)
  -\sum_j\bigl(\operatorname {inc}_{\rm slot}(R_j^+)
                   -\operatorname {inc}_{\rm slot}(R_j^-)\bigr)
   =\operatorname {inc}_{\rm slot}(S_0)
       +\sum_{t\in J}\operatorname {inc}_{\rm slot}(t). \tag{8.3}
\]

At the same time their outer matching permutation must install the off
states `B_t^-`.  After deleting all old rerouter and absorber-off edges,
contract the retained scaffold.  The union of every new rerouter edge and
every absorber-on edge must be loopless and independent there; the selected
root edges must give the prescribed one-root component equation; and the
whole ordered list must lie in one compiler trace bank or pass its exact
blocker deadlines.  These are the literal graphic/root/compiler guards, not
consequences of (8.3).

There is an immediate sharp obstruction to this template.  Since every
sparse rerouter has

\[
             \partial_{L,U}(R_j^+-R_j^-)=0,             \tag{8.4}
\]

no sequence of them changes the two outer leaves.  Therefore, if the outer
leave of the selected DP colour is not already the disjoint outer projection
of a subset of the target bank `T`, equations (8.2)--(8.3) are impossible,
regardless of slot freedom, path length, or graphic choices.  This is the
first target-bank obstruction.  The full DP colouring and constant-risk
prepacking do not currently prove the required outer alignment.

Even after (8.2) holds on the outer shores, our local audit exposes the next
two exact rows: positive root cylinders are not implied by common-basis
marginals, and a pointwise protected compiler cap can forbid the necessary
outer permutation.  Thus the remaining Catalan-scale long-ear theorem is
precisely a **fixed-`Q` target-aligned rerouter selection** satisfying
(8.3), contracted graphic/root independence, and a literal compiler trace.

## 9. Independent finite replay

Run

```text
python3 scratch/audit_catalan_n3_actuator_fixed4_embedding_20260731.py
```

It verifies the six/nine ordered matchings, both outer identities, the
complete degree change, all four exact root cylinders, the two preserved and
four changed cap rows, the tail/head boundary, both spectator-rank lifts for
ambient parameters `4..12`, the symmetry-greedy raw-packing formula, and the
two-partition-matroid marginal counterexample.  It writes

```text
scratch/catalan_n3_actuator_fixed4_embedding_20260731.audit.json
```

The replay is finite corroboration of the fixed active packet.  The
all-parameter claims are the spectator identity (2.4), the orbit double
count, and the union-bound argument proved above.
