# Exact `z`-cut effect of the two-stage SCD short ear

Date: 2026-08-01  
Lane: Thread D / SCD phase forest / short-chain paired ears  
Status: **exact fixed-`M_0` signed endpoint ledger and exact correction of
the apparent gain-two packet.  After restoring the displaced ordinary
target bundle, a palette-preserving paired ear contributes exactly one
`z`-cut unit, not two.  Hence the `c=Cat_{m-1}` short bank leaves the exact
residual `I_m-1-c` for every `m>=6`.**

## 1. The relevant retained state

Put

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad |G|=2m-3.
\]

For a standard short chain `S<L=S+x`, set

\[
 A=aS,\qquad B=zS,\qquad C=L.
\]

The frozen matching has

\[
 M_0(A)=aL,\qquad M_0(B)=azS,\qquad M_0(C)=zL.       \tag{1.1}
\]

For `b_0,b_1` outside `L`, put

\[
 U_0=L+b_0,\qquad U_1=L+b_1,\qquad V_1=S+b_1,
\]

and

\[
 P_0=M_0^{-1}(U_0),\qquad Q_1=M_0^{-1}(aV_1).       \tag{1.2}
\]

Thus

\[
 z\notin C,A,U_0,aV_1,
 \qquad z\in B,M_0(B),M_0(C),                       \tag{1.3}
\]

while

\[
 z\notin M_0(A),M_0(P_0),M_0(Q_1).                 \tag{1.4}
\]

The tight identity is commonly displayed from the virtual provider

\[
 C\to A\longmapsto A\to B+C\to P_0
 \longmapsto B\to C+C\to P_0+A\to Q_1.             \tag{1.5}
\]

For the phase-forest connector problem, however, the retained standard
short edge is `A->B`; the roots `B` and `C` are unused as lower tickets,
and `C` is an isolated component endpoint.  Therefore the two useful
states relative to that retained forest are

\[
\begin{array}{c|c|c|c|c}
\text{state}&\text{arcs on the short block}&\text{new lower tickets}
 &\text{sources}&\text{new upper repeats}\\ \hline
0&A\to B&-&A,C&-\\
1&A\to B,\ C\to P_0&C&A,C&zU_0\\
2&B\to C,\ C\to P_0,\ A\to Q_1&C,B&A,B&zU_0,aU_1.
\end{array}                                                   \tag{1.6}
\]

Here the source lists suppress sources of untouched background components.
The edge into `P_0` consumes the old source ticket at `P_0`; the edge into
`Q_1` similarly consumes the old source ticket at `Q_1`.  By (1.4) neither
consumed ticket contains `z`.

## 2. Signed cut potential

Let `H_z` be the number of unused lower roots containing `z`, and let
`S_z` be the number of physical source endpoints containing `z`.  The
connector cut is

\[
                         H_z-1\le S_z.              \tag{2.1}
\]

Equivalently, define its slack

\[
                         \kappa_z=S_z-H_z+1.         \tag{2.2}
\]

For the upper-exact SCD phase forest before short-ear insertion,

\[
                         \kappa_z=-(I_m-1),          \tag{2.3}
\]

where

\[
 c=\operatorname {Cat}_{m-1},\qquad
 I_m=\operatorname {Cat}_m-2c
 ={2(m-2)\over m+1}c.                               \tag{2.4}
\]

### Theorem 2.1 (one short block supplies at most one cut unit)

In the retained-provider embedding (1.6), the state changes have exact
signed effect

\[
\begin{array}{c|c|c|c}
\text{change}&\Delta H_z&\Delta S_z&\Delta\kappa_z\\ \hline
0\to1&0&0&0\\
1\to2&-1&0&+1.
\end{array}                                                   \tag{2.5}
\]

Thus a first ear creates neither a new `z`-source nor a `z`-hole
exemption.  A second rotation exempts exactly the one lower hole `B=zS`
and creates no additional `z`-source.

#### Proof

The first ear uses lower root `C=L`, which does not contain `z`.  It joins
the component ending at `C` to the component beginning at `P_0`.  The
surviving source on the first component is physically `M_0(C)=zL`, while
the consumed source is `M_0(P_0)=U_0`, which does not contain `z`.
Consequently neither `H_z` nor `S_z` changes.

The second rotation consumes the formerly unused lower root `B=zS`, so
`H_z` falls by one.  Its rethread replaces source `C`, whose physical
owner is `zL`, by source `B`, whose physical owner is `azS`; both contain
`z`.  Its other source remains `A`, and the consumed `Q_1` source is
physically `aV_1`; neither contains `z`.  Hence `S_z` is unchanged.  This
proves (2.5).  \(\square\)

### Remark 2.2 (the virtual provider does not give a second unit)

If one literally installs `C->A` as an isolated provider before applying
(1.5), then the isolated `B` is initially an additional `z`-source.  The
first rotation consumes that source, and the second rotation consumes the
`z`-lower ticket `B`.  The two effects cancel in `S_z-H_z`: the complete
literal two-stage replacement has net cut gain zero.  Therefore Theorem
2.1 uses the most favourable relevant embedding, namely the actual retained
`A->B` short edge of the long-ear phase forest.  The virtual `C->A`
identity cannot be counted as an extra source-capacity actuator.

## 3. Exact palette-preserving packet and the apparent gain-two error

In the exact upper-palette model, a paired packet is not compared with
three isolated old colour edges.  It occupies two provider rows and one
missing-target row:

* the short `azL` provider;
* the native long `zU_0` provider; and
* one ordinary option which services the missing target `aU_1`.

The selected packet inserts

\[
 \boxed{B\to C,\qquad C\to P(U_0),\qquad A\to Q(V_1)}          \tag{3.1}
\]

with upper colours `azL,zU_0,aU_1`.  It has three edges.  This is
edge-neutral relative to the two provider rows plus one target row, because
an ordinary target option already replaces one provider edge by two edges.

### Theorem 3.1 (exact gain is one)

Let `r` be the number of resource-disjoint paired packets selected in an
exact-upper, lower-injective degree-at-most-two phase forest.  Then

\[
 \boxed{H_z=c+I_m,\qquad t_z=c-r,\qquad S_z=c+r.}              \tag{3.2}
\]

Hence every packet contributes exactly one cut unit and the `z` row is

\[
                              \boxed{r\ge I_m-1.}              \tag{3.3}
\]

#### Proof

Every ordinary missing-target option has exactly one auxiliary lower tail
containing `z`.  The short second rotation uses `B=zS`, but displacing the
ordinary `aU_1` option frees its old `z`-containing auxiliary tail.  Thus
the apparent lower-hole exemption cancels in the complete target/provider
ledger and `H_z=c+I_m` remains unchanged.

What really changes is the native `zU_0` provider.  Replacing it by
`C->P(U_0)` consumes the short root `C=L`.  The `c` short roots are exactly
the holes `K` with `M_0(K)=K+z`; tail capacity permits at most one packet
per short root.  Therefore `t_z` falls from `c` to `c-r`.  The directed
endpoint identity `S_z=2c-t_z` gives `S_z=c+r`.  Substitution into
`H_z-1<=S_z` proves (3.3).  \(\square\)

### Corollary 3.2 (all-dimensional residual cut)

Since `r<=c`, the paired bank alone is impossible for every `m>=6`.  Even
after activating all short roots, the exact unpaid amount is

\[
 \boxed{I_m-1-c={m-5\over m+1}c-1},                         \tag{3.4}
\]

namely `5,32,142,571,2001,...` for `m=6,7,8,9,10,...`.

The tempting gain-two calculation releases the old `zU` head and consumes
the non-`z` head `P(U_0)`, which is a genuine one-unit source conversion.
Its claimed second unit treats the `aU_1` primary edge as independently
deletable.  It is not: an exact target option carries an old-colour return
edge and one `z`-auxiliary lower tail.  Restoring the displaced provider
frees that old `z` tail exactly when the packet consumes `B=zS`.  Therefore
there is no independent lower-hole exemption.

Dimensions `m=4,5` survive this scalar row only; the common provider,
target, head and graphic rows remain.

### 3.3 Typed selection gate

A proof-safe final-state variable `p_{S,U_0,U_1}` must simultaneously:

1. occupy the short `azL_S` provider and native `zU_0` provider;
2. occupy the unique target row `aU_1` in place of one ordinary option;
3. insert all three arcs in (3.1) in the common in/outdegree rows;
4. make the `P(U_0)` and `Q(U_1-x_S)` heads injective, including release
   against retained background heads; and
5. satisfy the contracted graphic inequalities or exact cycle cuts.

The exact provider equations, not an anonymous capacity-two row, perform
the old-colour return accounting.  They imply the valid cut

\[
                         \sum_{S,U_0,U_1}p_{S,U_0,U_1}\ge I_m-1,          \tag{3.5}
\]

which together with one short-provider capacity proves the `m>=6` no-go.

## 4. Contrast: the add-only family cut

Let `J_1` be the short chains receiving a first ear and let
`J_2 subseteq J_1` be those receiving the second rotation.  Assume all
displayed lower tickets are free, all `P_0,Q_1` tickets are legal sources,
and no external edge is released.  Then Theorem 2.1 sums without overlap:

\[
 H_z'=H_z-|J_2|,\qquad S_z'=S_z.                    \tag{3.1}
\]

The remaining connector Hall row therefore forces

\[
                         \boxed{|J_2|\ge I_m-1.}     \tag{3.2}
\]

But every short chain has only one `B=zS` lower ticket, so

\[
                         |J_2|\le c.                \tag{3.3}
\]

For `m>=6`, (3.2)--(3.3) contradict each other.  The exact uncovered cut is

\[
 \boxed{
 I_m-1-c={m-5\over m+1}c-1>0.}                     \tag{3.4}
\]

It begins

\[
                         5,32,142,571,2001,\ldots   \tag{3.5}
\]

for `m=6,7,8,9,10,...`.

For `m=4,5`, the scalar row alone leaves room: it asks for respectively
`3` of `5` and `13` of `14` short blocks to be doubled.  This is not an
existence theorem, because the typed SDR, free-ticket, and graphic rows
below remain.

## 5. Why anonymous capacity two does not repair the add-only cut

The projected short-boundary matching has `I_m` anonymous demands and
capacity two on each of the `c` short chains.  Give its two serial slots
variables `x^0_{S,U},x^1_{S,U}`, where slot zero is the first ear and slot
one is the second rotation.  The exact `z`-cut contribution is not

\[
 \sum_{S,U}(x^0_{S,U}+x^1_{S,U}),
\]

but only

\[
                         \boxed{\sum_{S,U}x^1_{S,U}.}          \tag{4.1}
\]

Indeed, slot zero uses `C=L` and slot one uses `B=zS`.  Therefore the
capacity-two Hall theorem is a type-erased projection and cannot be used
as two cut units per chain.

If exactly `I_m` anonymous services are selected and serial precedence is
imposed, then

\[
 \sum x^1\le\sum x^0,\qquad
 \sum(x^0+x^1)=I_m,
\]

so

\[
                         \sum x^1\le\lfloor I_m/2\rfloor.     \tag{4.2}
\]

Such an exact-size projected bank leaves at least

\[
                         \lceil I_m/2\rceil-1                  \tag{4.3}
\]

of the original `z` cut unpaid.  Allowing surplus repeated upper colours
can raise the number of doubled chains to `c`, but never beyond (3.3).

## 6. Exact surviving add-only joint system

The paired-ear layer can still be useful as part of a larger release.
Its proof-safe integral system is the following.

1. Choose `x^0,x^1` with one first and one second slot at most per short
   chain and with serial precedence.
2. Require `U_0` injective wherever distinct `P(U_0)` heads are needed,
   and require `V_1` injective for the `Q(V_1)` heads.  If repeated upper
   colours are allowed, `U_1` need not be colour-injective; if the new
   upper bank must itself be simple, impose `U_1` injective as well.
3. If `V_1(S)=L_T`, activate `T` so that the old head at `A_T` is released.
4. Delete every candidate meeting an occupied background tail/head ticket.
5. After inserting the ear bundles, match all but one remaining lower-hole
   terminals to compatible component sources.  Equivalently, adjoin one
   dummy source and impose the full Hall rows

   \[
       |Y|\le |N(Y)|+1                              \tag{5.1}
   \]

   on every family `Y` of remaining holes.
6. Impose graphic independence after contracting the retained background;
   the directed degree rows plus the graphic row make the result one linear
   forest after the connector matching.

The `z` member of (5.1) is exactly

\[
 \sum x^1+r_z^{\rm ext}+s_z^{\rm ext}\ge I_m-1,     \tag{5.2}
\]

where `r_z^{ext}` counts additional `z`-hole exemptions and
`s_z^{ext}` counts genuinely new independent `z`-source tickets supplied
by an external release/rethread.  Hence the weakest possible repair beyond
the entire doubled short bank is

\[
 r_z^{\rm ext}+s_z^{\rm ext}
 \ge \max\{0,I_m-1-c\}.                             \tag{5.3}
\]

Equation (5.3) is the sharp resource statement.  Raw short-ear menu counts,
upper-target coverage, and capacity-two matching do not alter it.

## 7. Signature test for a genuine gain-two actuator

The preceding calculation has a useful packet-independent form.  For a
lower root `K`, define

\[
 \eta_z(K)={\bf1}_{\{z\notin K,\ M_0(K)=K+z\}},\qquad
 w_z(K)={\bf1}_{\{z\in K\}}+\eta_z(K).              \tag{7.1}
\]

The two summands in `w_z` are disjoint, so `w_z(K)` is zero or one.  Let a
palette-preserving exchange delete tails `D^-` and insert tails `D^+`, after
cancelling every common tail.  Assume `D^+` were holes, `D^-` were used,
and the result is again an upper-exact lower-injective forest.

### Theorem 7.1 (signed tail criterion)

The exact cut gain of the exchange is

\[
 \boxed{
 \Delta\kappa_z=\sum_{K\in D^+}w_z(K)
                  -\sum_{K\in D^-}w_z(K).}          \tag{7.2}
\]

#### Proof

The hole change gives

\[
 \Delta H_z=\sum_{K\in D^-}{\bf1}_{z\in K}
             -\sum_{K\in D^+}{\bf1}_{z\in K},
\]

and similarly

\[
 \Delta t_z=\sum_{K\in D^-}\eta_z(K)
             -\sum_{K\in D^+}\eta_z(K).
\]

Since `S_z=2c-t_z`, subtracting `Delta H_z` from `Delta S_z` proves
(7.2).  \(\square\)

This criterion immediately classifies the currently proved local banks.

* A single tight one-to-two augmenter introduces only one exclusive new
  lower tail.  Therefore its gain is at most one.  Comparing two target
  options only exchanges their one auxiliary tail and again has gain at
  most one.
* The exact paired packet has exclusive new tails `B,C`, both of weight
  one, but it frees the ordinary target option's `z`-auxiliary tail, also
  of weight one, together with a weight-zero native provider tail.  Its net
  gain is `2-1=1`.
* An aligned rooted pentagonal `C6` preserves its three selected tails
  pointwise.  Hence its gain is zero, independently of its raw menu size.
* Every fixed-`M_0` `C6` or `C8` switch which preserves the complete lower
  label set has gain zero by (7.2).  The current folded-C8 endpoint socket
  removes three old lower colours and introduces only one new lower colour;
  before its missing sidecars are embedded, its local exchange has gain at
  most one.  Moreover that endpoint construction is not supplied with the
  frozen SCD root matching, so no stronger typed `z` claim is available.

Thus none of the presently proved tight-augmenter, aligned-C6, or literal
C8 signatures supplies a genuine gain-two fixed-`M_0` actuator.  Such an
actuator must exhibit, literally,

\[
 \sum_{K\in D^+}w_z(K)-\sum_{K\in D^-}w_z(K)\ge2,   \tag{7.3}
\]

while also passing provider/target/head and graphic rows.  In particular,
it must consume two more roots from the union of the `z`-lower bank and the
`M_0(K)=K+z` short-root bank than it releases.  Two disjoint first-stage
provider rethreads satisfy (7.3) only by spending two short roots, so their
total supply remains at most `c` and does not improve (3.4).  A useful new
packet must obtain its second unit from a different abundant rooted bank,
or recycle one short root while consuming an additional `z`-hole without
freeing an ordinary `z` auxiliary.

The exact next selection problem is consequently a weighted Rado/graphic
packing: select resource-disjoint packets `j` with gains `g_j` from (7.2)
so that

\[
                         \sum_j g_jx_j\ge I_m-1,     \tag{7.4}
\]

all provider and target rows have capacity one, all rooted heads are
injective, and the inserted bundles are graphic-independent after the
retained forest is contracted.  Raw packet counts do not imply (7.4).

## 8. Scope

The add-only calculation assumes the frozen `M_0` rows and no external
release.  Section 3 then restores the complete provider/target ledger and
shows that the exact palette-preserving packet still gains only one unit.
The resulting residual cut applies to this paired-ear grammar, not to a
different actuator which releases another independent `z` tail or creates
another independent `z` source.  Such an actuator must supply at least
`I_m-1-c` additional units for `m>=6`.
