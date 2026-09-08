# Mode-transparent `B_5` actuators preserve the gammoid carry

**Date:** 2026-08-02  
**Status:** exact composition and prescribed payload-planting theorems.
The local regenerative modules are unconditional, and their undecorated
containment carry is mode-transparent.  Planting enough copies with
address, history, state, upper, and compiler transparency is **UNPROVED**.
No all-`k` chronology or contiguous-OR word is claimed.

## 0. Outcome

The movable-frontier recurrence and the new `B_5` actuator suite fit
without an integrality loss.

For one chronology transition, let

\[
 L=M_B/F,\qquad N=L^*,\qquad
 K=Q_A/(A^+\mathbin{\dot\cup}\widehat B)              \tag{0.1}
\]

be respectively the occupied-slot matroid, the exposed-minimum carry
gammoid, and the contracted successor matroid of the entire earlier
prefix.  A protected placement exists exactly when

\[
 r_L(X)+r_{K^*}(H\setminus X)\ge r(L)\qquad(X\subseteq H). \tag{0.2}
\]

Every actuator in the displayed `B_5` suite is a union of alternating
cycles between the same rank-`m-1` bottoms and the same occurrence-labelled
rank-`m,m+1` suffix slots.  Hence its two modes use the same occupied slot
set and have the same undecorated containment carry.  More generally, if
an interval actuator preserves the complete occurrence-labelled interface
which defines `M_B`, `Q_A`, and every extra guard row, then it preserves
`L`, `N`, `K`, every cut in (0.2), and the realized carry base.  It may
then be toggled after the layer is frozen without reopening any payload
decision.

The concrete local choices are now exact:

\[
\begin{array}{c|c|c|c}
\text{module}&\text{range}&\text{topology}&\Delta\beta\\ \hline
\text{one closed socket}&m\ge4&5C_4\longrightarrow C_{20}&-4\\
\text{one opened socket}&m\ge5&5C_4+2K_2\longrightarrow P_{22}+P_2&-5\\
\text{three closed sockets}&m\ge5&15C_4\longrightarrow3C_{20}
 \longrightarrow C_{60}&-14\\
\text{three opened sockets}&m\ge6&15C_4+2K_2
 \longrightarrow P_{62}+P_2&-15.
\end{array}                                                   \tag{0.3}
\]

Thus local circuit existence is closed on a planted transparent face.  A
prescribed local bottom-relay circuit extends to the full active layer if
and only if its residual graph satisfies the same two explicit Hall
families as the movable-frontier theorem.  The remaining actuator-side
hypothesis is protected cross-core planting with mode-transparent
occurrence interfaces.  The local exterior-reset rule is also explicit:
two opened sockets can share the first sidecar and still carry exactly one
`P_2`; any already planted relay chain therefore has a bounded one-edge
sidecar.  What remains is planting an extensive such chain on one protected
host.  Equality of the four named palettes alone is insufficient because
it need not preserve addresses or complete suffix tuples.
Nor does a bounded signature alphabet force transparent sockets: an exact
two-colouring kills every saturated `C10`, while opening a named `C20`
requires a rooted same-signature `C6` Hall condition.

## 1. The occurrence interface

Fix one transition of a chronology.  The current block is a named token
set `B`.  Its receiver ground is

\[
                         E=F\mathbin{\dot\cup}H,                \tag{1.1}
\]

where `F` is mandatory and `H` is optional.  The fixed current
compatibility graph is

\[
                         G_B\subseteq B\times E.                \tag{1.2}
\]

For pure containment, `be` is an edge exactly when the target named by
`b` is strictly contained in the exposed minimum of receiver occurrence
`e`.

Let `A` be the whole earlier prefix.  Its successor graph has left shore
`A` and occurrence-labelled right shore

\[
             A^+\mathbin{\dot\cup}\widehat B\mathbin{\dot\cup}H.
                                                                    \tag{1.3}
\]

Here `A^+` contains the available internal right copies of earlier
targets, while `\widehat B` contains the always exposed right copies of
the current targets.  Denote this graph by `G_A` and its receiver
transversal matroid by `Q_A`.

The **external occurrence interface** of a local interval module consists
of the following data.

1. The occurrence sets `B,F,H,A^+,\widehat B`, their named Boolean targets,
   and the mandatory/optional partition.
2. Every exposed suffix tuple read outside the module, not merely the four
   unordered row palettes.
3. The edge sets of `G_B` and `G_A` incident with a module occurrence.
4. The occupied receiver support `J\subseteq H` of the realized current
   placement.
5. Every protected boundary label and every declared state, reset,
   address, aggregate-history, residence, upper, source, and compiler menu
   read outside the module.

Items 1--4 are the pure reserve-carry interface.  Item 5 is the literal
protected interface.

### Definition 1.1 (mode transparency)

Let `T^0,T^1` be the two modes of a planted local interval module.  They
are **carry-transparent** if there is a bijection `phi` between their
occurrence interfaces which

* fixes every exterior occurrence and preserves `F,H` and all named
  exposed suffix tuples;
* is a graph isomorphism for both `G_B` and `G_A`; and
* maps the occupied optional support `J` in mode zero to the same named
  support in mode one.

They are **protected mode-transparent** if, in addition, `phi` preserves
every item in 5 occurrencewise.  Equality only as an unordered deck is not
enough unless every consumer of that deck is invariant under the induced
permutation.

### Definition 1.2 (exact rank-level transparency)

Put `C=A^+\dot\cup\widehat B` and identify `H` pointwise in the two modes.
The weakest condition which preserves the two complete matroid rank
oracles is

\[
\begin{aligned}
 r_{M_B^0}(F\cup X)-r_{M_B^0}(F)
   &=r_{M_B^1}(F\cup X)-r_{M_B^1}(F),\\
 r_{Q_A^0}(C\cup X)-r_{Q_A^0}(C)
   &=r_{Q_A^1}(C\cup X)-r_{Q_A^1}(C)
\end{aligned}
\qquad(X\subseteq H).                                  \tag{1.4}
\]

These identities say exactly that `L^0=L^1` and `K^0=K^1` as matroids on
the same literal ground `H`.  Definition 1.1 is a directly checkable
sufficient lift of (1.4).  A mere permutation of `H` is not enough unless
it is an automorphism of both matroids and of every protected row.

## 2. Exact carry-invariance theorem

Let `M_B^epsilon` be the receiver transversal matroid of `G_B` in mode
`epsilon`, and define

\[
 L^\epsilon=M_B^\epsilon/F,
 \qquad N^\epsilon=(L^\epsilon)^*.                 \tag{2.1}
\]

Let `Q_A^epsilon` be the earlier-prefix receiver transversal matroid and
put

\[
 K^\epsilon
   =Q_A^\epsilon/(A^+\mathbin{\dot\cup}\widehat B)\quad
   \text{on }H.                                    \tag{2.2}
\]

### Theorem 2.1 (protected actuator/carry commutation)

If `T^0,T^1` are carry-transparent, then `phi` induces matroid
isomorphisms

\[
 M_B^0\cong M_B^1,qquad L^0\cong L^1,qquad
 N^0\cong N^1,qquad K^0\cong K^1.                 \tag{2.3}
\]

Consequently:

1. the two movable-frontier Hall families agree;
2. every rank inequality
   \[
     r_{L^\epsilon}(X)+r_{(K^\epsilon)^*}(H\setminus X)
        \ge r(L^\epsilon)                           \tag{2.4}
   \]
   has the same truth value in both modes;
3. the realized exposed carry
   \[
                            D=H-J                    \tag{2.5}
   \]
   is unchanged, up to the displayed interface identification; and
4. if mode zero admits a completion of the whole earlier prefix using
   `D`, then mode one admits such a completion using the same `D`.

If the modes are protected mode-transparent, the same toggle also
preserves every declared literal guard and may be performed after the
current suffixes have been frozen.

#### Proof

A transversal matroid is determined by its occurrence-labelled bipartite
graph.  The two graph-isomorphism clauses therefore give
`M_B^0\cong M_B^1` and `Q_A^0\cong Q_A^1`.  The interface bijection maps
`F` to `F` and maps `A^+\dot\cup\widehat B` to itself.  Matroid contraction
and duality commute with isomorphism, which proves (2.3).

Rank is invariant under isomorphism, so both the rectangular Hall tests
and every cut (2.4) agree.  The support clause gives (2.5).  A carry
completes the earlier prefix exactly when it spans `K`; this property is
also invariant under the isomorphism.  Finally, protected transparency is
the explicit assertion that no additional guard distinguishes the two
modes.  Hence the toggle and the one-layer freeze commute. \(\square\)

### Corollary 2.2 (disjoint actuator bank)

Suppose `s` planted two-mode modules have pairwise disjoint complete
old/new footprints and each is protected mode-transparent.  Then their
toggles commute.  All `2^s` modes have the same `L,N,K`, the same viable
carry bases, and the same protected interface.  In particular, selecting
the all-new topology cannot consume reserve or invalidate an already
certified whole-prefix cut.

This statement is about the displayed planted face.  It does not say that
an arbitrary table contains the modules.

### Theorem 2.3 (exact prescribed bottom-relay planting)

Let `B_0\subseteq B` and `R_0\subseteq F\dot\cup H` have equal size.  Suppose
`mu_0,mu_1:B_0\to R_0` are perfect matchings in the same fixed
bottom-to-receiver compatibility graph.  Prescribe either local mode and
require the matching outside `B_0\dot\cup R_0` to be the same.  Put

\[
 B'=B\setminus B_0,\qquad F'=F\setminus R_0,
 \qquad H'=H\setminus R_0.                           \tag{2.6}
\]

Then both local modes extend to a complete movable-frontier placement, or
neither does.  Extension holds exactly when, for every `X\subseteq B'`,

\[
\boxed{
\begin{aligned}
 |N_{F'}(X)|+|N_{H'}(X)|&\ge |X|,\\
 |N_{F'}(X)|&\ge |X|-(|B'|-|F'|).
\end{aligned}}                                               \tag{2.7}
\]

When (2.7) holds, the two modes may be extended using the same residual
matching.  These paired completions occupy the same optional receiver set
`J`, expose the same carry `D=H-J`, and have the same current transversal
matroids `M_B,L,N`.

#### Proof

Delete the equal shores `B_0,R_0`.  The dummy count of the rectangular
movable-frontier graph remains

\[
 |F'|+|H'|-|B'|=|F|+|H|-|B|.                       \tag{2.8}
\]

The residual graph is independent of the choice `mu_0` or `mu_1`.
Theorem 2.1 of the movable-frontier note says that it has a completion
exactly under (2.7).  Reattaching either prescribed perfect matching uses
the same receiver set `R_0`, so the full occupied support and its complement
are identical.  The ambient compatibility graph, hence its transversal
matroid and contraction, never changed. \(\square\)

The theorem removes payload integrality from prescribed socket planting.
It does not prove that sufficiently many desired sockets can be chosen so
that their common residual graph satisfies (2.7).

### Proposition 2.4 (checkable boundary-column condition)

For a local alternating circuit, let `mu_epsilon(b)` be the suffix slot
receiving bottom `b` in mode `epsilon`.  Let `kappa(b,v)` denote the
complete receiver column exported to the earlier-prefix and protected
systems when `b` occupies slot `v`.  If

\[
                 \kappa(b,\mu_0(b))=\kappa(b,\mu_1(b))
                 \qquad(b\in B_0),                            \tag{2.9}
\]

then `Q_A^0=Q_A^1` occurrencewise and hence `K^0=K^1`.  On the pure
containment face, `kappa` depends only on the named exposed bottom `b`, so
(2.9) holds automatically.  More generally, if
`kappa(b,v)=(kappa_0(b),sigma(v))` and `sigma` is the complete slot-inherited
part of the protected column, then (2.9) holds if and only if `sigma` is
constant on each slot cycle of the actuator.

#### Proof

Every right column outside the circuit is fixed.  Equation (2.9) fixes the
column exported by each moved bottom, so the complete earlier-prefix graph
is the same in both modes.  Contraction gives the claim.  In the factored
case, the old-to-new assignment is a permutation of the slot shore;
equality along every assignment edge is exactly constancy on each orbit of
that permutation. \(\square\)

### Example 2.5 (palette and carry equality do not protect `K`)

Let `H={h}`, `\widehat B={b}`, and let the earlier prefix consist of one
target `a`.  Give both modes the same current matroid `L=U_{1,1}` on `H`;
thus both occupy \(J=\{h\}\) and carry \(D=\varnothing\).  In mode zero let
`Q_A^0` have edges `ab,ah`, while in mode one let `Q_A^1` have only `ah`.  Both
graphs have full rank one, but

\[
             K^0=Q_A^0/b\text{ has rank }0,
             \qquad K^1=Q_A^1/b\text{ has rank }1.              \tag{2.10}
\]

Mode zero completes through `b`; mode one needs the unavailable receiver
`h`.  Thus identical palettes, occupied support, and carry cardinality do
not imply (1.4).  This is the smallest possible address-column
obstruction.

### Theorem 2.6 (exact Hall erosion under prescribed planting)

In Theorem 2.3, put `r=|B_0|=|R_0|`,
`r_H=|R_0\cap H|`, and define the two original Hall slacks

\[
\begin{aligned}
 s_1(X)&=|N_{F\cup H}(X)|-|X|,\\
 s_2(X)&=|N_F(X)|-|X|+(b-f).
\end{aligned}                                                \tag{2.11}
\]

The prescribed modes extend if and only if, for every
`X\subseteq B\setminus B_0`,

\[
\boxed{
\begin{aligned}
 s_1(X)&\ge |N_{F\cup H}(X)\cap R_0|,\\
 s_2(X)&\ge |N_F(X)\cap R_0|+r_H.
\end{aligned}}                                               \tag{2.12}
\]

Consequently `s_1(X)>=r` on every nonempty relevant `X` and
`s_2(X)>=r` on every relevant `X` is a uniform sufficient condition for
arbitrary prescribed shores of size `r`.  For an ordinary chronology
(`f=0`), the second row is automatic after deletion, and universal
`r`-shore robustness is exactly

\[
 |N_H(X)|\ge |X|+r
 \quad\text{for every nonempty }X\subseteq B, |X|\le b-r.    \tag{2.13}
\]

For a disjoint bank the required uniform slack is cumulative.  If the
numbers of closed one-socket, opened one-socket, closed three-socket, and
opened three-socket modules are `a,b,c,d`, respectively, then

\[
                           R=5a+8b+18c+21d                     \tag{2.14}
\]

receivers are prescribed at once.

#### Proof

After deletion,

\[
 b'=b-r,\quad f'=f-|R_0\cap F|,
 \quad h'=h-r_H,\quad f'+h'-b'=f+h-b.             \tag{2.15}
\]

For `X\subseteq B\setminus B_0`, the residual first neighbourhood has
size

\[
 |N_{F\cup H}(X)|-|N_{F\cup H}(X)\cap R_0|,
\]

so its Hall inequality is exactly the first row of (2.12).  The residual
second Hall inequality is

\[
 |N_F(X)|-|N_F(X)\cap R_0|
 \ge |X|-(b-f)+r_H,
\]

which is its second row.  This proves the equivalence and the uniform
sufficient condition.

When `f=0`, every residual set has size at most `b-r`, so the dummy Hall
row is automatic.  Deleting any `r` optional receivers can erase at most
`r` neighbours, proving sufficiency of (2.13).  Conversely, if (2.13)
fails, delete `r` receivers containing as much of `N_H(X)` as possible
and choose `B_0` disjoint from `X`; residual Hall fails.  Finally the four
module sizes are their numbers of changed bottom-relay atoms. \(\square\)

The full rectangular worst-case second erosion is
`min(r,h+|N_F(X)|)` rather than always `r`; thus the uniform second-row
condition can be stronger than necessary when `h<r`.  Formula (2.12), not
the uniform corollary, is the sharp fixed-bank test.

### Theorem 2.7 (incumbent-aligned zero-slack bank)

Let `M` be one augmented perfect matching.  Suppose pairwise shore-
disjoint planted modules have old modes `mu_i^0\subseteq M` and alternate
modes `mu_i^1` on the same local shores.  Put

\[
 M_{\rm res}=M\setminus\bigcup_i\mu_i^0.             \tag{2.16}
\]

Then for every phase vector `epsilon`,

\[
 M_{\rm res}\cup\bigcup_i\mu_i^{\epsilon_i}          \tag{2.17}
\]

is an augmented perfect matching.  Thus an arbitrarily large native,
incumbent-aligned disjoint bank consumes zero Hall slack and has its full
phase hypercube on the pure payload face.

For a fixed real-bottom shore `B_0`, let `T_{B_0}` be the transversal
matroid on `E=F\dot\cup H` presented by the remaining real bottoms
`B\setminus B_0` together with the unchanged dummies.  If the ambient
graph has a perfect matching, then

\[
 r(T_{B_0})=|E|-|B_0|,
 \qquad N_{B_0}=T_{B_0}^*                           \tag{2.18}
\]

is a rank-`|B_0|` strict gammoid.  A receiver shore `R_0` permits residual
completion if and only if it is a base of `N_{B_0}`.

#### Proof

In (2.17), the residual matching and the selected local modes have
disjoint shores and together cover the same two augmented shores as `M`.
For (2.18), restricting `M` after deleting `B_0` proves that `T_{B_0}` has
the displayed full rank.  A residual completion uses a base
`E\setminus R_0` of `T_{B_0}`.  By matroid duality this is equivalent to
`R_0` being a base of `T_{B_0}^*`. \(\square\)

If independently cloneable slot roles have menus `A_1,...,A_r`, Rado's
theorem gives the exact selectable-shore condition

\[
 r_{N_{B_0}}\!\left(\bigcup_{i\in I}A_i\right)\ge |I|
 \qquad(I\subseteq[r]).                              \tag{2.19}
\]

This applies only after proving that independent representatives really
assemble into the required `B_5` modes.  Correlated whole-module bundles
do not automatically factor into a Rado instance.

### Example 2.8 (ambient Hall plus a local circuit is insufficient)

For any `r>=2`, let

\[
 B=\{x\}\dot\cup B_0,qquad H=R_0\dot\cup\{q\},
 \qquad |B_0|=|R_0|=r.                              \tag{2.20}
\]

Join `x` to exactly `R_0`, and join every member of `B_0` to every receiver.
The ambient graph has a perfect matching, and `B_0\times R_0` contains two
cyclic local perfect matchings.  Prescribing either local mode consumes all
of `R_0` and leaves `x` isolated.  Here

\[
 s_1(\{x\})=r-1<r=|N(x)\cap R_0|.                  \tag{2.21}
\]

Thus the `+r` boundary is sharp by one.  At `r=5` the two local matchings
have the alternating `C10` pattern.  This is a matching-level obstruction,
not a literal Boolean-socket nonexistence theorem.

## 3. Instantiation by the exact `B_5` suite

All circuits used below admit a bottom-relay reading in one rank-`m-1`
movable layer against occurrencewise fixed rank-`m,m+1` suffix slots.
Every saturated `C10` is a 5-cycle of slot assignments and every Boolean
`C6` is a 3-cycle.  Theorem 2.3 therefore applies to the complete composite
after deleting the union of its local bottom and slot shores.  On the
untyped, undecorated containment face, Proposition 2.4 makes every such
circuit transparent to the whole dual-transversal carry recurrence.  The
three-socket fusion uses its tail shore as the fixed middle, so this last
sentence is not a standard fixed-head directed-carry theorem.

If protected data factors through a suffix-slot signature, a sufficient
condition is one five-slot clone class for each `C10` and one three-slot
clone class for each `C6`.  This is exactly the cyclewise form of (2.9).

### 3.1 Saturated `C10` as a movable-bottom relay

For a fixed consecutive suffix `M_v\subset U_v`, a legal movable bottom
`B` induces the other middle target

\[
                    \chi(B;v)=B\cup(U_v-M_v).                  \tag{3.1}
\]

The saturated `B_5` `C10` uses the same five bottom tokens and the same
five physical suffix slots in both phases, and its old and new `chi` decks
are cyclic shifts of one another.  Therefore it is carry-transparent on
the pure bottom-placement face: it is a matching circuit inside one base
of `L`, occupies the same receiver support `J`, and leaves `D=H-J`
unchanged.

This does **not** prove protected mode transparency.  The fixed `(M_v,U_v)`
slot remains occurrencewise, but `chi` generally changes address.  Any
state, history, or compiler row which reads that address must either be
transported by the same permutation or be proved invariant under it.

### 3.2 One-socket forest actuator

For every `m>=5`, the audited composite replaces eight interval atoms and
has the exact literal topology

\[
  5C_4+2K_2\longrightarrow C_{20}+2K_2
             \longrightarrow P_{22}+P_2.                       \tag{3.2}
\]

All 22 lower, upper, tail, and head resources and both bank labels agree
between the old and new modes.  Relative to the untouched support, the
old eight atoms have graphic rank three and the new eight have rank eight,
so `Delta beta=-5`.

In the notation of the local theorem, the private `P_2` has endpoints
`S+{a,c}` and `S+{b,c}`, while the main `P_{22}` has endpoints
`S+{a,b}` and `S+{q,c}`.  Every resource of the private edge contains the
locally fresh coordinate `c`.

The `C10` and the opening `C6` are respectively a 5-cycle and a 3-cycle
between fixed bottom and suffix shores.  Thus (3.2) is unconditionally
carry-transparent on the pure containment face.  If the module's complete
decorated interface satisfies Definition 1.1 or the sharper column test
(2.9), Theorem 2.1 makes it an exact protected regenerative step inside
the reserve-carry recurrence.  The circuit-complete disjoint product from
the local theorem then becomes a hypercube of carry-equivalent modes whose
all-new state is a forest.

Four-row palette equality is necessary here but not sufficient for the
decorated conclusion.  Although the `C6` preserves its fixed suffix slots,
its induced co-middle deck changes address.  Those addresses must be
internal to the protected module, constant on the slot 3-cycle, or
transported by the interface isomorphism.

### 3.3 Three-socket actuator and exact opening

For every `m>=5`, three pairwise resource-disjoint sockets and one Boolean
hex give

\[
                         15C_4\longrightarrow3C_{20}
                              \longrightarrow C_{60}.          \tag{3.3}
\]

For `m>=6`, choose `q` in the nonempty core and a coordinate `c` outside
the complete `m+5`-coordinate socket support.  The second Boolean hex then
uses one untouched vertical and two exterior old atoms and gives

\[
        15C_4+2K_2\longrightarrow3C_{20}+2K_2
        \longrightarrow C_{60}+2K_2
        \longrightarrow P_{62}+P_2.                            \tag{3.4}
\]

The complete replacement has 21 old and 21 new atoms and preserves all
62 resources in each of the four typed rows.  Under protected mode-
transparent planting, it is one carry-neutral toggle with
`Delta beta=-15`.

For the first, fusing `C6`, use the displayed **tail** as the fixed middle
of each suffix.  Its three fixed `(middle,upper)` slots, suppressing the
common core, are

\[
   (\alpha\gamma,\alpha\gamma\delta),\quad
   (\beta\gamma,\beta\gamma\delta),\quad
   (\alpha\beta,\alpha\beta\delta).                \tag{3.5}
\]

For the fresh-coordinate opening `C6`, use the displayed **head** as the
fixed middle.  It likewise cycles three bottoms through three fixed
suffix slots.  This tail/head distinction is essential: the first `C6`
does not preserve the displayed `(head,upper)` pairs.

The final private `P_2` is the fresh-coordinate edge whose endpoints are
`T+{gamma,c}` and `T+{delta,c}`; the `P_{62}` endpoints are
`T+{gamma,delta}` and `T+{q,c}`.  Hence disjoint opened modules create one
fresh-coordinate `P_2` each.  The local theorem proves these are forest
components, but it does not merge, relay, or reuse them.

### Proposition 3.1 (same-base target reuse is not a legal relay)

The private `P_2` of one opener cannot be reused as the target edge of a
second opener with the same base `S`, the same fixed marker `a`, and the
preceding main path frozen.

Suppress the fixed base and write an opener atom as

\[
 F(x,y)=(S+x,\ S+a+x+y;\ S+a+x\longrightarrow S+x+y).          \tag{3.6}
\]

One Boolean hex replaces

\[
 \{F(q,b),F(b,c),F(c,q)\}
 \quad\text{by}\quad
 \{F(b,q),F(c,b),F(q,c)\}.                                   \tag{3.7}
\]

The new private edge is `F(c,b)`.  With the same base and fixed marker, its
target representation is `F(q',b')` with `q'=c,b'=b`.  The second new phase
contains `F(b,c)`.  But the first new phase retains the main-path edge
`F(b,q)`, and `F(b,c)` and `F(b,q)` have the same lower resource `S+b`
and the same tail resource `S+a+b`.  Their union therefore violates both
row injectivity and the relevant bank matching.

Consequently, a same-base target relay must also rethread the adjacent old
main-path edge and its protected history.  This proposition does **not**
rule out using the sidecar as an exterior old atom of a later opener or
reparameterizing it after a cross-core base change; those possibilities
require a new complete-footprint collision and history audit.

#### Proof

Formula (3.6) shows that the lower and tail resources depend only on the
first argument.  The displayed duplication is therefore literal.  Since
the complete table requires those rows to be injective, the proposed
one-edge overlap is impossible. \(\square\)

### Theorem 3.2 (exact two-socket cross-core exterior relay)

For every `m>=6`, two opened one-socket modules can share exactly one
intermediate `P_2` so that ten old `C_4` cycles are absorbed while only one
`P_2` is carried.

Choose pairwise disjoint data

\[
 |R|=m-5,\quad |K|=5,\quad
 q,s,c,z,a,b\notin R\cup K,                         \tag{3.8}
\]

and fix one `d`-type pair `X\in\binom{K}{2}` in a cyclic order of `K`.  Put

\[
\begin{aligned}
 C_1&=R+q+s,& S_1&=R+s+X,\\
 C_2&=R+c+z,& S_2&=R+c+X=(S_1-s)+c.
\end{aligned}                                      \tag{3.9}
\]

Use a closed `B_5` socket with core `C_1`, endpoint markers `(a,b)`, target
lower `C_1+X`, core pivot `q`, and opener coordinate `c`.  Use a second
closed socket with core `C_2`, endpoint markers `(a,s)`, target lower
`C_2+X`, core pivot `z`, and opener coordinate `b`.

In the notation (3.6), the first opener has

\[
\begin{aligned}
 O_1&=\{F_{S_1,a}(q,b),F_{S_1,a}(b,c),F_{S_1,a}(c,q)\},\\
 N_1&=\{F_{S_1,a}(b,q),F_{S_1,a}(c,b),F_{S_1,a}(q,c)\},
\end{aligned}                                      \tag{3.10}
\]

while the second has

\[
\begin{aligned}
 O_2&=\{F_{S_2,a}(z,s),F_{S_2,a}(s,b),F_{S_2,a}(b,z)\},\\
 N_2&=\{F_{S_2,a}(s,z),F_{S_2,a}(b,s),F_{S_2,a}(z,b)\}.
\end{aligned}                                      \tag{3.11}
\]

The first output sidecar is literally the first exterior old atom of the
second opener:

\[
             p=F_{S_1,a}(c,b)=F_{S_2,a}(s,b).       \tag{3.12}
\]

After cancelling `p`, the compound Boolean-hex trade has five old and five
new atoms,

\[
\begin{aligned}
 O={}&\{F_{S_1,a}(q,b),F_{S_1,a}(b,c),F_{S_1,a}(c,q),
        F_{S_2,a}(z,s),F_{S_2,a}(b,z)\},\\
 N={}&\{F_{S_1,a}(b,q),F_{S_1,a}(q,c),
        F_{S_2,a}(s,z),F_{S_2,a}(b,s),F_{S_2,a}(z,b)\}.
                                                               \tag{3.13}
\end{aligned}
\]

Together with the two `C10` switches, this is a 15-atom old/new
replacement with identical lower, upper, tail, and head rows, fixed bank
labels, and topology

\[
\begin{aligned}
 10C_4+3K_2
 &\longrightarrow P_{22}+P_2+C_{20}+K_2\\
 &\longrightarrow 2P_{22}+P_2.                    \tag{3.14}
\end{aligned}
\]

Thus `Delta beta=-10`, and the number of live opening sidecars is one,
not two.  The complete support has size `m+6<=2m`.

#### Proof

Equation (3.12) follows by substituting `S_2=S_1-s+c` in the four entries
of `F`: both sides have lower `S_1+c`, upper `S_1+a+b+c`, tail
`S_1+a+c`, and head `S_1+b+c`.  Each Boolean hex separately has equal
four-row decks; cancelling their common atom proves equality for (3.13).

Every resource of the first closed socket contains `q`, while every
resource of the second contains `z` and omits `q`.  The remaining exterior
resources are separated by the missing-`s`/present-`c` signature and by
`z`; direct row comparison leaves (3.12) as the only cross-module atom.
Hence the old, intermediate, and new rows are injective and both declared
banks remain matchings.

The first `C10+C6` turns its `5C_4` and two exterior edges into
`P_{22}+P_2`.  The shared `P_2` and the one remaining exterior edge are
exactly the two old exterior atoms for the second compressed `C20`.
The second `C6` therefore creates another `P_{22}` and one new `P_2`,
which proves (3.14). \(\square\)

### Proposition 3.3 (one shared atom is minimal for a nontrivial relay)

Two distinct Boolean opener phases cannot share two atoms unless the
second phase is exactly the reverse of the first and merely undoes it.
Indeed an atom fixes its aperture `a=tail-lower` and its intrinsic second
coordinate `y=head-lower`.  For two atoms in one phase, their distinct
lower sets determine the common base as their intersection; the two
directed rim arcs then determine the third arc of the triangle.  Thus two
shared atoms determine the whole `C6` phase.

The relay in Theorem 3.2 shares one atom and is therefore overlap-minimal
among nontrivial compositions of two opener `C6`s. \(\square\)

### Theorem 3.4 (explicit clean relay chain of length at most `m-4`)

For every `m>=5` and `1<=t<=m-4`, there is a literal chain of `t` full
one-socket actuators carrying exactly one `P_2` through every phase.

Choose

\[
 |R|=m-5,\quad |K|=5,\quad
 X\in\binom{K}{2}\text{ of `d`-type},              \tag{3.15}
\]

and distinct coordinates

\[
 r_0,b_0,c_0,a,q_1,\ldots,q_t\notin R\cup K.         \tag{3.16}
\]

Enumerate `t-1` distinct elements of `R` as `r_1,...,r_{t-1}` and put
`s_1=r_0`, `s_i=r_{i-1}` for `i>=2`.  Start with

\[
 S_1=R+r_0+X,\qquad b_1=b_0,\qquad c_1=c_0,         \tag{3.17}
\]

and recurse

\[
 S_{i+1}=S_i-s_i+c_i,\qquad
 b_{i+1}=s_i,\qquad c_{i+1}=b_i.                   \tag{3.18}
\]

For module `i`, take core and pivot

\[
                         C_i=(S_i-X)+q_i,            \tag{3.19}
\]

the common five-set `K`, endpoint markers `(a,b_i)`, fresh opener
coordinate `c_i`, and target pair `X`.  Its old and new opener phases are

\[
\begin{aligned}
 O_i&=\{F_i(q_i,b_i),F_i(b_i,c_i),F_i(c_i,q_i)\},\\
 N_i&=\{F_i(b_i,q_i),F_i(c_i,b_i),F_i(q_i,c_i)\},
\end{aligned}                                      \tag{3.20}
\]

where `F_i=F_{S_i,a}`.  The relay identity is

\[
                 F_i(c_i,b_i)=F_{i+1}(b_{i+1},c_{i+1})
                 \qquad(1\le i<t).                 \tag{3.21}
\]

After `j` openings, the exact topology is

\[
 jP_{22}+P_2+(t-j)C_{20}+(t-j)K_2,qquad0\le j\le t. \tag{3.22}
\]

Including the initial `C10` compressors, the endpoint transition is

\[
                5tC_4+(t+1)K_2
                     \longrightarrow tP_{22}+P_2.              \tag{3.23}
\]

Every phase has `21t+1` atoms, injective lower/upper/tail/head rows, and
two matching banks.  The net replacement has `7t+1` old and `7t+1` new
atoms, `Delta beta=-5t`, and complete support size

\[
                         m+4+t\le2m.               \tag{3.24}
\]

#### Proof

The recurrence gives `S_{i+1}=S_i-s_i+c_i`,
`b_{i+1}=s_i`, and `c_{i+1}=b_i`; substituting into `F` proves (3.21)
entry by entry.  Hence precisely one intermediate atom cancels at every
interface.  Inductively \(s_i\in S_i-X\) while
\(b_i,c_i\notin S_i\); hence every displayed core, endpoint pair, and
fresh opener coordinate satisfies the one-socket hypotheses.

All socket-`i` resources contain the private pivot `q_i`.  To audit the
exterior rows, put

\[
 D_0=S_1+b_1,\qquad D_i=S_i+c_i\quad(1\le i\le t). \tag{3.25}
\]

With `T=R+r_0`, direct induction gives

\[
\begin{aligned}
 D_0&=X+T+b_0,\\
 D_1&=X+T+c_0,\\
 D_i&=X+(T-s_{i-1})+b_0+c_0\qquad(i\ge2).
\end{aligned}                                      \tag{3.26}
\]

The `D_i` are pairwise distinct.  These are exactly the lower resources
which do not carry a private `q_i`; the tail versions add the common
aperture `a`.  Every remaining exterior head or upper resource carries its
module's `q_i`, and the sole live `P_2` is the only exception.  Thus no
cross-module row collision occurs.  Local socket injectivity handles each
module.  The exterior tails contain the common aperture `a`, their heads
omit it, and the private pivots separate socket middles across modules;
hence the two bank-middle rows remain matchings.

At phase `j`, each completed module contributes `P_{22}`, each uncompleted
compressed socket contributes `C_{20}`, the current relay atom contributes
one `P_2`, and each future opener contributes one isolated old edge.  This
proves (3.22)--(3.23).  Counting the `t-1` cancelled relay atoms gives
`8t-(t-1)=7t+1`, and (3.24) is the displayed coordinate inventory.
\(\square\)

A tempting period-three pointwise reset which reuses an earlier `D_i`
fails: the next module's other old exterior atom then has the same lower
and tail as an earlier live or retained atom.  The distinct sequence in
(3.26) is essential.  The theorem gives `Theta(m)` clean sockets, not an
extensive all-table socket packing.

### Corollary 3.5 (abstract protected relay chain)

More generally, let `t` opened one-socket modules be ordered so that the
output `P_2` of module `i` is one exterior old atom of module `i+1`.
If all other complete old/new footprints are pairwise disjoint and all
interfaces are protected mode-transparent, then (3.23) preserves the
gammoid carry and every protected row and has exactly one live sidecar.

#### Proof

Induct on `t` using the same cancellation and topology argument, and apply
Theorem 2.1 to every toggle. \(\square\)

The explicit chain is only linear in `m`.  Planting an extensive actuator
bank into `O(1)` such protected chains, or splicing clean chains without a
row/history collision, remains an existence problem.

### Corollary 3.6 (quantitative transparent-bank regeneration)

Let an ambient frozen transition contain `p` pairwise footprint-disjoint
copies of (3.2) and `q` pairwise footprint-disjoint copies of (3.4), all
protected mode-transparent and disjoint from a fixed forest background.
Then the all-new state

* preserves the exact carry base and the whole-prefix condition (0.2);
* preserves every declared protected row; and
* decreases graphic nullity by exactly `5p+15q` and leaves a forest on the
  union of the module footprints.

No additional chronology block or dummy receiver is used.  Thus the
actuators contribute zero reserve-carry overhead once the transparent bank
has been planted.

#### Proof

Carry and guard preservation is Corollary 2.2.  Complete-footprint
disjointness and the disjoint forest background make graphic nullity
additive.  The one-socket and three-socket deltas are respectively `-5`
and `-15`. \(\square\)

The disjoint-bank conclusion deliberately leaves `p+q` private `P_2`
components.  Replacing a group of one-socket copies by a relay chain from
Theorem 3.4 or Corollary 3.5 leaves one `P_2` for the whole group.  The
remaining global task is therefore a bounded-chain-cover planting, not
local discovery of a relay atom.  Proposition 3.1 excludes only the
same-base target version.

## 4. What slot signatures do and do not force

### Theorem 4.1 (two protected signatures can kill every `C10` clone)

Finite signature cardinality alone does not force a mode-transparent
saturated `C10`, even when every five-set and cyclic order is available.

Fix a linear order of the free coordinates.  For an occurrence-labelled
slot

\[
 v_i=\bigl(C+\{a_i,a_{i+2}\}
       \subset C+\{a_i,a_{i+1},a_{i+2}\}\bigr),                \tag{4.1}
\]

let `x_i=a_{i+1}` be its distinguished point `U_i-M_i`.  Give the slot
signature `M` if `x_i` lies strictly between `a_i,a_{i+2}` in the fixed
order, and `E` if it is extremal.  Every legal `C10` five-cycle is
bichromatic.

#### Proof

An all-`M` cycle is impossible: take the globally least `a_j`; in the slot
where it is distinguished, both neighbours are larger, so it is extremal.
If every slot were `E`, then for every `i` the two consecutive signs

\[
 \operatorname {sgn}(a_{i+1}-a_i),qquad
 \operatorname {sgn}(a_{i+2}-a_{i+1})                         \tag{4.2}
\]

would be opposite.  Signs cannot alternate consistently around an odd
cycle of length five. \(\square\)

This is a literal occurrence signature: the core `C` is part of the slot
address.  Taking one protected exported bit to be this signature gives a
genuine mode-transparency obstruction.  Thus `q=1` versus `q=2` signatures
is already sharp, and the uncoloured positive-density socket theorem may
coexist with zero protected `C10` compressors.

### Theorem 4.2 (conditional Johnson packing of clone-good sockets)

For the fixed-five-set Johnson bank, put

\[
 N=\binom{2m-5}{m-2},\qquad
 \Delta=(m-2)(m-3),\qquad
 \Lambda=3m^2-14m+13.                              \tag{4.3}
\]

Let `G` be the endpoint cores whose prescribed five-slot `C10` cycle has
one constant complete signature, and put `g=|G|`.  Then at least

\[
                    \left\lceil\frac{g\Delta}{2\Lambda}\right\rceil
                                                                  \tag{4.4}
\]

pairwise complete-resource-disjoint closed sockets can be planted and
oriented so that the switched endpoint is clone-good.  If `g=alpha N`,
this is `(alpha/6+o(1))N`.

If both endpoints must be clone-good, at least

\[
 \left\lceil
 \frac{
  \max\{0,\frac{m-3}{2}((m-1)g^2/N-g)\}}
 {\Lambda}
 \right\rceil                                                  \tag{4.5}
\]

such sockets exist; for fixed positive `alpha` this is
`(alpha^2/6+o(1))N`.

#### Proof

The Johnson graph has degree `Delta`.  Edges incident with `G` number

\[
                         g\Delta-e(G)\ge g\Delta/2.              \tag{4.6}
\]

The exact socket-conflict neighbourhood has size at most `Lambda`, so the
greedy conflict-graph bound proves (4.4).

The smallest Johnson eigenvalue here is `-(m-3)`.  Applying the standard
indicator-vector bound to the induced graph on `G` gives

\[
 2e(G)\ge(m-3)\bigl((m-1)g^2/N-g\bigr).             \tag{4.7}
\]

Greedy selection among these both-good edges proves (4.5). \(\square\)

For one signature class `tau`, if it occupies `x_tau` of the `5N`
specified endpoint slots, then the number `g_tau` of all-`tau` cycles
satisfies

\[
                         g_\tau\ge\max\{0,x_\tau-4N\}.          \tag{4.8}
\]

Indeed every nongood cycle contributes at most four such slots.  The bound
is sharp without further structure.  Density strictly above `4/5` in one
clone class therefore suffices; merely having boundedly many classes does
not.

### Theorem 4.3 (unrooted `C6` Ramsey versus rooted opener Hall)

For a complete hub menu with base `C`, hub `h`, and rim `R`, identify the
suffix slot

\[
                C+\{x,y\}\subset C+\{h,x,y\}                   \tag{4.9}
\]

with the rim edge `xy`.  Legal hub-`C6` slot cycles are exactly triangles.
Hence `q` slot signatures force an unrooted clone `C6` whenever

\[
                              |R|\ge R_q(3).                    \tag{4.10}
\]

Repeatedly deleting its three rim vertices gives

\[
              \left\lfloor\frac{|R|-R_q(3)}3\right\rfloor+1   \tag{4.11}
\]

vertex- and resource-disjoint clone `C6`s.  For two signatures,
`R_2(3)=6`; the threshold is sharp because a red 5-cycle and its blue
complement colour `K_5` with no monochromatic triangle.

This does not open a prescribed `C20` target.  For a target edge `xy` of
signature `d`, define

\[
             A_{xy}=\{z:\sigma(xz)=\sigma(yz)=d\}.             \tag{4.12}
\]

A transparent rooted `C6` through `xy` exists exactly when `A_{xy}` is
nonempty.  For several disjoint targets, restrict third coordinates to lie
outside every target endpoint.  Choosing distinct third coordinates is
then exactly Hall's theorem in the bipartite graph

\[
                             xy\sim z\iff z\in A_{xy}.          \tag{4.13}
\]

#### Proof

The slot/edge identification makes the first assertions ordinary
multicolour triangle Ramsey, and vertex deletion proves (4.11).  A triangle
through `xy` is monochromatic exactly under (4.12); simultaneous
resource-disjoint choices require distinct `z`, which is (4.13). \(\square\)

The rooted condition is genuinely extra.  Colour a prescribed matching of
target edges red and every other rim edge blue.  No red target belongs to
a monochromatic triangle, regardless of the rim size.  Thus neither
Ramsey nor the uncoloured socket bank supplies the named opening tickets.

### 4.4 The exact unresolved planting hypothesis

The weakest statement still needed to turn the preceding composition into
a regenerative all-`k` step is the following.

> **Protected cross-core planting/mode-transparency gate (UNPROVED).**
> For every selected reserve-carry transition and every carry base chosen
> by (0.2), materialize the central interval rows so that all but a bounded
> carried sidecar of the cyclic support is partitioned into complete
> one-socket or three-socket old footprints; plant the required exterior
> opening atoms and fresh coordinates; and give every old/new pair one
> occurrence-interface isomorphism preserving the exposed suffix tuples,
> carry support, endpoint aperture, protected state, aggregate histories,
> addresses, residence, upper/source rows, and compiler menus.

In addition, all but `O(1)` private opening edges must be linked by the
cross-core exterior relation (3.12), or by another protected construction,
into relay chains of Theorem 3.4 or Corollary 3.5.  A same-base target
relay is excluded by Proposition 3.1.  Every relay edge must preserve the
same pointwise receiver columns; a component-count argument alone is
insufficient.

The hypothesis must be asserted on the one frozen global host, not
separately on phase-dependent hosts.  It is stronger than named-palette
equality and stronger than a positive-density abstract socket packing.
It is exactly what lets Theorem 2.1 commute each local topology toggle
through the already frozen reserve-carry recurrence.

By Theorems 4.1--4.3, a proof cannot replace this clause by “there are
only finitely many signatures.”  It must produce a positive bank of
clone-good `C10` endpoint cycles and the rooted codegree/Hall condition
(4.12)--(4.13) for the selected opening targets.  Conditional on those two
inputs, (4.4)--(4.5) give an explicit disjoint closed-socket supply.

At the pure payload level, the weakest nonaccumulating route is now exact:
make the old modes a disjoint submatching of one incumbent placement, so
Theorem 2.7 supplies every phase at zero Hall cost, and organize them into
the clean relay chains of Theorem 3.4.  Without incumbent alignment, the
entire chosen bank must instead satisfy the cumulative erosion cuts
(2.12); testing each module separately is insufficient.

The existing positive-density theorem supplies disjoint **closed**
`5C_4->C_{20}` sockets only.  It does not supply their two exterior opener
atoms, an incumbent old phase, compatible protected columns, or the
contracted ambient rank gain.  For a non-isolated planting the latter must
be checked directly after contracting the whole untouched background;
the private-footprint values are five for (3.2) and fifteen for (3.4).

There is a sharp finite warning.  The authenticated K17 frozen suffix
catalogue has 96,619 raw hub-`C6` sockets and 287,269 raw hub-`C8` sockets,
but zero saturated `B_5` `C10` sockets before any bottom matching is
chosen.  Bottom relays cannot change this suffix catalogue.  Hence the
one-socket and three-socket actuators cannot be planted on that bottom-only
face; a suffix/cross-core rethread or a different host is mandatory.

## 5. Consequence ledger

The following statements are **PROVED**.

1. A carry-transparent toggle preserves `L,N,K`, all exact one-layer Hall
   and whole-prefix matroid-intersection cuts, and the realized carry.
2. A protected mode-transparent toggle commutes with freezing the current
   layer.
3. The exact `B_5` modules in (0.3) are concrete zero-overhead regenerative
   actuators on every planted transparent face.
4. Disjoint transparent banks have additive graphic improvement and a
   carry-equivalent hypercube of modes.
5. Prescribing any finite union of their bottom-relay cycles leaves one
   ordinary residual movable-frontier instance, governed exactly by the
   two Hall families (2.7).
6. Two opened one-socket modules admit an explicit, overlap-minimal
   cross-core exterior relay with one carried `P_2`; any planted relay chain
   has exactly one live sidecar.
7. The Hall erosion caused by a prescribed module bank is exactly (2.12);
   incumbent-aligned native banks consume zero Hall slack and have a
   strict-gammoid shore criterion.
8. Two protected signatures can eliminate every `C10` clone.  Conditional
   clone-good Johnson packing and rooted `C6` Hall are quantified by
   Theorems 4.2--4.3.

The following statements remain **UNPROVED**.

1. An all-`k`, `d(k)+O(1)` chronology satisfying the propagated carry-rank
   inequalities.
2. Protected cross-core planting of enough `B_5` modules on the same
   frozen host and carry base.
3. Mode transparency for occurrence addresses, aggregate histories,
   state/reset, residence, upper/source, and compiler rows.
4. A phase-common protected host planting all but `O(1)` modules into the
   proved cross-core relay-chain relation, so that the local one-edge
   sidecar bound becomes global.
5. Positive density of clone-good `C10` endpoint cycles and rooted
   same-signature Hall for the selected `C6` opening targets.
6. Bounded treatment of any cyclic support outside the planted modules.
7. The final literal serialization and contiguous-OR bound.

In particular, the available lossless flag lift for an isolated Boolean
`C6` does not supply a compatible `C10` or whole-module reset theorem, so
it does not discharge item 3.

## 6. Source and replay ledger

The local modules used here are proved in

```text
MATH_THEOREM_A_FIVE_FIBRE_C10_CYCLE_COMPRESSOR_AND_C6_C8_RIGIDITY_20260802.md
MATH_AUDIT_A_CENTRAL_B5_C10_C6_COMBINED_ABSORBER_20260802.md
MATH_THEOREM_A_THREE_SOCKET_B5_C10_BOOLEAN_C6_FUSION_20260802.md
MATH_COROLLARY_A_THREE_SOCKET_C60_EXACT_ROOT_OPENING_20260802.md
MATH_THEOREM_A_BOTTOM_RELAY_INTERVAL_ACTUATOR_PROJECTION_AND_K17_C10_NOGO_20260802.md
```

The movable-frontier rank interface is proved and independently audited in

```text
MATH_THEOREM_MOVABLE_FRONTIER_GAMMOID_CARRY_AND_TWO_LAYER_FUSION_20260802.md
MATH_AUDIT_MOVABLE_BOTTOM_FRONTIER_AND_GAMMOID_CARRY_20260802.md
```

The new occurrence-slot, contracted-prefix, Hall-erosion, and exterior-
relay audit
is

```text
python3 scratch/audit_mode_transparent_b5_carry_20260802.py
python3 scratch/audit_b5_cross_core_exterior_relay_20260802.py
```
