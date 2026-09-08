# Resident facet sockets transfer insertion-label current and export an exact cofacet-child star

Date: 2026-08-01  
Lane: Thread D / endpoint current / compact resident facet socket  
Status: **unconditional local current, all-depth lower, and child-upper
ledger.  The compact socket is not by itself a positive-current actuator.
Positive distinguished-coordinate current is possible only through its
ambient extraction arcs, and every such internal gain outside the parent
upper block exports a distinct exchanged upper child.  No all-dimensional
packing or child-cascade closure is claimed.**

## 0. Verdict

Let `U` have rank `r+1`, choose distinct

\[
                    v_0,\ldots,v_h\in U,
        \qquad F_i=U-\{v_i\},                         \tag{0.1}
\]

and orient the compact resident socket

\[
                    F_0\longrightarrow F_1\longrightarrow
                    \cdots\longrightarrow F_h.       \tag{0.2}
\]

For an oriented Johnson edge `e:X->Y`, write

\[
 \sigma(e)\text{ for the unique element of }Y-X,
 \qquad
 j_q(e)={\bf1}_{q\in X\cap Y}-{\bf1}_{q\in Y}.       \tag{0.3}
\]

Then

\[
                         j(e)=-{\bf e}_{\sigma(e)}.   \tag{0.4}
\]

Consequently the intrinsic current of (0.2) is

\[
                 \boxed{j(\text{socket})
                    =-\sum_{i=0}^{h-1}{\bf e}_{v_i}.} \tag{0.5}
\]

Thus the resident block itself creates no positive current.  If an ambient
rethread deletes arcs `D` and adds the socket plus exterior arcs `B`, its
exact endpoint-current change is

\[
 \boxed{\Delta\kappa_q
   =|\{e\in D:\sigma(e)=q\}|-
     |\{e\in B:\sigma(e)=q\}|.}                    \tag{0.6}
\]

In particular, a component-preserving rethread has zero *total* coordinate
current.  It can improve `kappa_a+kappa_z` only by transferring the same
amount of current out of ordinary coordinates.

There is also an exact upper-debt certificate.  An old outgoing edge from
`F_i` has insertion label

\[
                  \alpha_i\in\{v_i\}\cup(\Omega-U)  \tag{0.7}
\]

and upper colour

\[
 R_i=\begin{cases}
       U,&\alpha_i=v_i,\\
       U-\{v_i\}+\{\alpha_i\},&\alpha_i\notin U.
     \end{cases}                                    \tag{0.8}
\]

Replacing that edge by the socket edge out of `F_i` changes current by

\[
                         {\bf e}_{\alpha_i}-\mathbf e_{v_i}. \tag{0.9}
\]

The same replacement changes the coordinate-incidence vector of its upper
colour by the exact opposite amount:

\[
 {\bf1}_{U}-{\bf1}_{R_i}
          ={\bf e}_{v_i}-{\bf e}_{\alpha_i}.        \tag{0.10}
\]

Every positive unit in a distinguished coordinate outside `U` therefore
exports the named child `U-v_i+alpha_i`.  Distinct indices export distinct
children.  The two exterior seams of one socket can cover at most two of
these children; all remaining children require an external provider SDR.
This cofacet-star debt, not residence of the internal block, is the exact
all-dimensional gate.

## 1. Endpoint current is the insertion-label boundary

Consider a directed, lower-injective Johnson support on rank-`r` owners.
Let `H_q` be the number of unused rank-`(r-1)` lower colours containing
`q`, let `S_q` be the number of source owners containing `q`, and put

\[
                         \kappa_q=1+S_q-H_q.          \tag{1.1}
\]

### Lemma 1.1 (one-edge identity)

For every directed Johnson edge `e:X->Y`, (0.4) holds.

#### Proof

Write `X=K+x` and `Y=K+y`, where `K=X\cap Y`.  Then

\[
 {\bf1}_{X\cap Y}-{\bf1}_Y={\bf1}_K-{\bf1}_{K+y}
                         =-{\bf e}_y.
\]

Here `y=sigma(e)`.  \(\square\)

### Corollary 1.2 (exact rethread current)

If `F^-` and `F^+` are directed lower-injective supports on the same owner
set, and `D=F^- - F^+`, `B=F^+ - F^-`, then (0.6) holds and

\[
                 \sum_q\Delta\kappa_q=|D|-|B|
                    =c(F^+)-c(F^-),                 \tag{1.2}
\]

where the last equality applies when both supports are linear forests and
`c(F)` denotes their number of components.

#### Proof

Adding an edge changes used-lower incidence by `+1_(X\cap Y)` and used-head
incidence by `+1_Y`.  Since `Delta H` is the negative used-lower change and
`Delta S` is the negative used-head change, its contribution to
`Delta kappa=Delta S-Delta H` is (0.3).  Apply Lemma 1.1 and sum.  A forest
on a fixed owner set has `|E|=|V|-c(F)`.  \(\square\)

Equation (1.2) separates two phenomena which raw socket counts conflate.
A detached socket path contributes one component and hence one unit of
total current; the edge which reconnects that component consumes one unit
again.  A completed component-neutral socket can still transfer current
between coordinates, but cannot create total current.

## 2. Complete internal child ledger

For `0<=i<h`, put

\[
                         K_i=F_i\cap F_{i+1}
                            =U-\{v_i,v_{i+1}\}.       \tag{2.1}
\]

The immediate lower colours `K_i` are distinct and every immediate upper
colour is `U`.  More generally, for `0<=q<=h` and
`0<=s<=h-q`,

\[
 \boxed{\bigcap_{j=s}^{s+q}F_j
       =U-\{v_s,v_{s+1},\ldots,v_{s+q}\}.}           \tag{2.2}
\]

Thus the depth-`q` consecutive lower deck has exactly `h+1-q` distinct
members of rank `r-q`.  Every consecutive union of at least two owners is
`U`.

The coordinate degrees of the immediate lower children are

\[
 \sum_{i=0}^{h-1}{\bf1}_{q\in K_i}=
 \begin{cases}
 0,&q\notin U,\\
 h,&q\in U-\{v_0,\ldots,v_h\},\\
 h-1,&q=v_0\text{ or }v_h,\\
 h-2,&q=v_j,\ 1\le j\le h-1.
 \end{cases}                                      \tag{2.3}
\]

The consumed heads are `F_1,...,F_h`; subtracting their coordinate degrees
from (2.3) gives (0.5).  Reversing (0.2) instead gives

\[
                         j(\text{reverse socket})
                    =-\sum_{i=1}^{h}{\bf e}_{v_i}.   \tag{2.4}
\]

Hence orientation only chooses which endpoint omitted label is spared.
It does not turn the socket into a positive-current block.

The upper multiset supplied internally is

\[
                              h[U].                 \tag{2.5}
\]

Only one copy can repair a missing target `U`; the other `h-1` copies must
be charged to the repeat-upper cocycle.  In particular, the socket is not
an upper-exact replacement column without an ambient upper-palette ledger.

## 3. Two-sided embedding and the finite-cascade column

Let `X` and `Y` be exterior owners and insert

\[
 X\longrightarrow F_0\longrightarrow\cdots\longrightarrow F_h
   \longrightarrow Y.                               \tag{3.1}
\]

Write

\[
 \lambda=\sigma(X,F_0),\qquad \rho=\sigma(F_h,Y).   \tag{3.2}
\]

The added insertion-label multiset, lower palette, and upper palette are

\[
\begin{aligned}
 \Sigma^+&=[\lambda]+[v_0]+\cdots+[v_{h-1}]+[\rho],\\
 \mathcal L^+&=[X\cap F_0]+\sum_{i=0}^{h-1}[K_i]+[F_h\cap Y],\\
 \mathcal U^+&=[X\cup F_0]+h[U]+[F_h\cup Y].       \tag{3.3}
\end{aligned}
\]

If `D` is the complete multiset of active old arcs deleted to expose and
place (3.1), then

\[
\boxed{
 \Delta\kappa_q=d_D(q)-
  {\bf1}_{q=\lambda}-\sum_{i=0}^{h-1}{\bf1}_{q=v_i}
  -{\bf1}_{q=\rho},}                                \tag{3.4}
\]

and

\[
\begin{aligned}
 \Delta\mathcal L&=\mathcal L^+-
                     \sum_{e\in D}[\ell(e)],\\
 \Delta\mathcal U&=\mathcal U^+-
                     \sum_{e\in D}[\operatorname{up}(e)].   \tag{3.5}
\end{aligned}
\]

These are the exact columns required by the finite cascade.  In particular,

\[
                         \sum_q\Delta\kappa_q=|D|-(h+2).     \tag{3.6}
\]

The number of extraction cuts alone determines only (3.6), not the
direction of the current vector.  Deciding `a+z` gain requires the ordered
insertion labels in (3.4), and deciding whether the packet closes requires
the named lower and upper rows in (3.5).

For the currently audited `k=17`, `h=3` convention, a complete socket with
both exterior seams adds five arcs.  Hence rows deleting `3,4,5,6` active
arcs have total current respectively `-2,-1,0,+1`.  Even the final class
has only one unit of *total* current, whose coordinate and child-palette
closure are separate questions.  This arithmetic is not a claim that any
of the finite rows packs simultaneously.

## 4. Positive current exports a cofacet-child star

Suppose an old outgoing edge from `F_i` is

\[
                         e_i:F_i\longrightarrow G_i,
 \qquad \alpha_i=\sigma(e_i).                      \tag{4.1}
\]

Because the only coordinate of `U` absent from `F_i` is `v_i`,

\[
                         \alpha_i\in\{v_i\}\cup(\Omega-U).  \tag{4.2}
\]

Its old upper colour is exactly (0.8).  For `i<h`, replacing `e_i` by the
socket edge `F_i->F_(i+1)` has signed current (0.9).

Let `A` be any distinguished coordinate set.  A positive `A`-unit from
this replacement requires

\[
                         \alpha_i\in A\setminus U,
 \qquad v_i\notin A,                               \tag{4.3}
\]

and exports the child

\[
                         R_i=U-v_i+\alpha_i.         \tag{4.4}
\]

For distinct indices `i`, the children (4.4) are distinct, even if all
`alpha_i` are the same outside coordinate: intersecting `R_i` with `U`
recovers the omitted label `v_i`.

Moreover the signed coordinate ledger of the upper replacement is exactly
the negative of its current ledger:

\[
 \Delta\deg_{\mathcal U}(i)
   :={\bf1}_{U}-{\bf1}_{R_i}
   ={\bf e}_{v_i}-{\bf e}_{\alpha_i}
   =-\Delta\kappa(i).                              \tag{4.4a}
\]

Thus the child cascade is not merely a target-count warning.  At the
coordinate level it carries precisely the current removed from the old
upper bank.

### Theorem 4.1 (current--child injection)

In an outgoing-rooted compact extraction, every positive internal current
unit in `A-U` injects into a distinct deleted upper child (4.4).  The two
exterior seams in (3.1) supply at most two upper colours.  Therefore if the
old arcs are unique witnesses, a packet with `p` such positive units needs
an external provider matching for at least

\[
                              (p-2)_+                 \tag{4.5}
\]

of its named children.  Provider existence must be tested jointly with
owner capacity and the lower rows (3.5).

#### Proof

Equations (4.2)--(4.4) prove the injection.  The internal socket arcs have
upper colour `U` and cover none of the children.  Only the two exterior
arcs remain inside the displayed packet, so they can cover at most two
distinct children.  Every other deleted unique child needs a witness
outside the packet.  \(\square\)

### Proposition 4.2 (uniform raw gain, exactly paid by the child star)

The current--child gate is sharp for every `h`.  Let `z\notin U` and choose
one label

\[
                 x\in U-\{v_0,\ldots,v_h\};         \tag{4.6}
\]

such an `x` exists under the socket hypothesis `r>=2h+1`.  For
`0<=i<h`, put

\[
 G_i=F_i-\{x\}+\{z\},
 \qquad e_i:F_i\longrightarrow G_i.                \tag{4.7}
\]

The old arcs `e_i` have pairwise distinct tails, heads, lower colours

\[
                         U-\{v_i,x\},                \tag{4.8}
\]

and upper colours

\[
                         U-\{v_i\}+\{z\}.            \tag{4.9}
\]

Replacing all `e_i` by the `h` internal socket arcs is degree-legal on this
isolated local support (include `F_h` as an isolated old vertex) and has

\[
 \boxed{\Delta\kappa
      =h{\bf e}_z-\sum_{i=0}^{h-1}{\bf e}_{v_i}.}    \tag{4.10}
\]

Thus it has hard-coordinate gain `h` at `z` but zero total coordinate
gain.  Simultaneously it deletes exactly the `h` distinct children (4.9)
and replaces them by `h` copies of `U`.

More precisely, its entire upper coordinate ledger is

\[
 \boxed{
 h{\bf1}_{U}-\sum_{i=0}^{h-1}{\bf1}_{U-v_i+z}
    =\sum_{i=0}^{h-1}{\bf e}_{v_i}-h{\bf e}_z
    =-\Delta\kappa.}                               \tag{4.11}
\]

In particular, if the hard set is `A={a,z}` and none of
`v_0,...,v_(h-1)` equals `a`, then

\[
                         \Delta\kappa_A=h.          \tag{4.12}
\]

This is an all-`h` positive **hard-pair transporter**, but (4.11) shows
that it is not a closed actuator.

#### Proof

Every arc (4.7) inserts `z`, while the corresponding socket arc inserts
`v_i`; (4.10) follows from Lemma 1.1.  Intersecting (4.8) or (4.9) with
`U` recovers `v_i`, proving distinctness.  The tails lie inside `U` and the
heads contain `z`, so no tail is a head and all rooted degrees are at most
one in the old support.  The new support is one facet path plus the isolated
old heads.  Its edge count is unchanged.  \(\square\)

Proposition 4.2 answers the purely local sign question positively but does
not solve the actuator problem: its entire hard-current gain is exposed as
an equally large upper-provider cascade.  An all-dimensional closed gain
theorem is therefore equivalent to planting or rerouting this child star
without paying the `z` insertion label back.

There is a sharper zero-child consequence.  If `A\subseteq U`, then an old
outgoing arc can insert an `A`-coordinate only by inserting its own omitted
label `v_i`; the socket edge inserts the same label.  Thus the first `h`
replacements have nonpositive `A`-gain, indeed zero whenever the old
insertion lies in `A`.  Any remaining positive unit must come from an
unpaired terminal or exterior extraction boundary, and is component or
child-palette credit rather than an intrinsic socket gain.

This last assertion is only for the outgoing-rooted replacements above.
For an old incoming arc `G_i->F_i`, put

\[
 \beta_i=\sigma(G_i,F_i)\in F_i,
 \qquad x_i\in G_i-F_i.                              \tag{4.13}
\]

Then `x_i in {v_i} union (Omega-U)`, its lost upper is `F_i+x_i`, and
replacing it by `F_(i-1)->F_i` changes current by

\[
                         {\bf e}_{\beta_i}-{\bf e}_{v_{i-1}}. \tag{4.14}
\]

This can move current positively inside `U`; if `x_i=v_i`, the lost upper
is `U` and one repeated socket occurrence may absorb it.  Hence arbitrary
two-sided extraction is governed by the complete column (3.4)--(3.5), not
by Theorem 4.1 alone.  The exact-19 `z` gain is of this incoming/exterior
type.

## 5. Exact surviving all-dimensional gate

The compact resident facet theorem proves:

1. owner distinctness and the literal Johnson path;
2. the residence guards;
3. the internal lower tower (2.2); and
4. repeated coverage of its parent upper target `U`.

It does **not** prove a positive endpoint-current actuator.  An
all-dimensional use now has an exact finite-column formulation.  Select
socket columns `s` satisfying

\[
 \sum_s x_s\Delta\kappa_s(\{a,z\})
      \ge I_m-c+D_{\rm long}-2,                     \tag{5.1}
\]

where each column is computed by (3.4), and simultaneously require:

* every child in (3.5), or equivalently (4.4) in the rooted subcase, has a
  retained or newly selected provider;
* lower colours are injective;
* facet owners, source heads, and exterior endpoints have capacity one;
* the `h-1` repeat copies of each parent `U` satisfy the connector cocycle;
* all residence guards and the final graphic/path rows hold.

The local socket theorem supplies the internal part of these columns but
no lower bound on their positive supply.  The precise obstruction is the
current--child injection: deleting an outside distinguished insertion
label is useful current only because it simultaneously deletes a named
cofacet child.  A proof of (5.1) must therefore be a correlated
current-plus-child-provider theorem, not a count of available facet
sockets.

The independent finite calibration and its exact raw positive-current row
are recorded in
`MATH_AUDIT_THREAD_D_RESIDENT_FACET_SOCKET_ENDPOINT_CURRENT_20260801.md`.
That row confirms that positive hard-coordinate transfer can occur, while
also exhibiting the component, lower-collision, repeated-upper, and
unsupported-child debts which prevent calling it a closed actuator.
