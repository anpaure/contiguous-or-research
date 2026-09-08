# Audit: three-socket `C60` opening as an augmented-matching interface

**Date:** 2026-08-02  
**Status:** exact interface theorem and frozen-fibre obstruction.  The local
`15C4 -> 3C20 -> C60 -> P62+P2` construction is authenticated, and its
opening switch is one alternating `C6`.  However, the unchanged K17 suffix
fibre has exactly zero saturated `B5 C10` sockets, so the three-socket module
cannot be instantiated by bottom relocation on the current
`R/H/def=1918/1681/59` carrier.  Suffix rethreading or an explicit planted
suffix geometry is necessary.

## 1. The one circuit

Use the notation of
`MATH_COROLLARY_A_THREE_SOCKET_C60_EXACT_ROOT_OPENING_20260802.md` and put

\[
\begin{array}{lll}
A=L+\gamma,&B=T+\gamma+\delta,&C=T+\gamma+c,\\
A'=L+\delta,&B'=T+\delta+c,&C'=T+q+c.
\end{array}
\]

The old and new tail--head matchings are

\[
 Q^- = \{AA',BB',CC'\},\qquad
 Q^+ = \{BA',CB',AC'\}.                           \tag{1.1}
\]

All six vertices are distinct.  Hence `Q-` and `Q+` are the two alternating
halves of one `C6`, not three independent switches.  For the signed edge
vector

\[
             \zeta=\mathbf 1_{Q^+}-\mathbf 1_{Q^-},             \tag{1.2}
\]

the bipartite node--edge incidence matrix satisfies

\[
                              A\zeta=0.                          \tag{1.3}
\]

In the intended two-private-host use, `e=AA'` is the untouched edge already
on the `C60`, while `o1=BB'` and `o2=CC'` are the two exterior private
edges.  The switch nevertheless has a three-edge premise:

\[
                         e,o1,o2\in P.                           \tag{1.4}
\]

Pinning only `o1,o2` does not authorize the flip.  If the module is planted
in one shot, all three members of `Q-` are simply private pinned edges.

There is a more specific bottom-token interpretation; an arbitrary map of
the physical tail sets to matching vertices is not enough.  Put

\[
 b_0=L=T+q,\qquad b_1=T+\delta,\qquad b_2=T+c,                  \tag{1.5}
\]

and require three hard slots with fixed suffixes

\[
\begin{array}{c|cc}
 &M_v&U_v\\ \hline
 v_0&L+\delta&L+\gamma+\delta\\
 v_1&T+\delta+c&T+\gamma+\delta+c\\
 v_2&T+q+c&T+q+\gamma+c.
\end{array}                                                     \tag{1.6}
\]

Then the old and new bottom matchings are

\[
 \widehat Q^-=\{b_0v_0,b_1v_1,b_2v_2\},\qquad
 \widehat Q^+=\{b_1v_0,b_2v_1,b_0v_2\}.                       \tag{1.7}
\]

For `chi(b;v)=b+(U_v-M_v)`, their induced co-middle decks are respectively

\[
 (A,B,C)=(L+\gamma,T+\gamma+\delta,T+\gamma+c)
 \quad\hbox{and}\quad (B,C,A).                                 \tag{1.8}
\]

Thus (1.7) is the required hub `C6` in `G_bot` whenever the three named real
bottom tokens and three named suffix slots occur.  Dummy tokens cannot
represent these interval atoms: they create a bottomless short slot and have
no induced Boolean interval/co-middle.

## 2. Exact residual-matching test

Let `G_bot` be the labelled augmented bottom-token graph and suppose its real
bottom and hard-slot vertices contain the six typed objects (1.5)--(1.6),
with every edge in (1.7) legal.  This includes the fixed-suffix and induced
co-middle identities (1.6)--(1.8), not just abstract bipartite incidence.

### Theorem 2.1 (pin, extend, flip)

Let \(Q=\widehat Q^-\).  A perfect matching of `G_bot` containing `Q` exists if
and only if

1. `Q` is a partial matching; and
2. after deleting the six vertices incident with `Q`, the residual graph
   `G_Q` satisfies

\[
                  |N_{G_Q}(X)|\ge |X|                           \tag{2.1}
\]

for every subset `X` of its residual left shore.

Whenever `P` is such an extension,

\[
                   P'=(P\setminus Q)\cup\widehat Q^+            \tag{2.2}
\]

is automatically a perfect matching.  No second Hall test is needed.

#### Proof

The first equivalence is the ordinary forced-edge perfect-matching theorem:
disjoint forced edges may be deleted with their endpoints, and Hall is
necessary and sufficient on the residual bipartite graph.  Equation (1.7)
shows that `widehat Q+` is another perfect matching on exactly the same six deleted
vertices.  Replacing `Q-` by `Q+` therefore leaves every vertex degree one.
QED.

The two-private-host interpretation applies (2.1) conditional on the already
pinned edge `e`; the three-private-host interpretation pins all of `Q-` at once.
They are the same three-edge residual test, not different local switches.

### Corollary 2.2 (forcing two or three short hosts)

If the private requirement is instead expressed by forcing a set
`S0 subset H_slot`, `|S0|=t`, of hard slots to be dummy matched, where
`t` is two or three, require first

\[
                         S_0\cap\{v_0,v_1,v_2\}=\varnothing,     \tag{2.3}
\]

because all three opening slots are real-bottom occupied on both sides of
the circuit.  With no other pins, the exact dummy-quotiented Hall conditions
are

\[
\boxed{
\begin{aligned}
 |N_F(X)|+|N_H(X)\setminus S_0|&\ge |X|,\\
 |N_F(X)|&\ge |X|-16898
\end{aligned}}                                                   \tag{2.4}
\]

for every real-bottom family `X`.  The first row is the placement cut after
removing the forced-short hosts.  The second is the unchanged quota which
forces all `1748` singleton hosts to receive real bottoms.

To see sufficiency as well as necessity, force `t` distinct dummy edges into
`S0` and delete their endpoints.  A residual left subset with no dummy gives
the first row of (2.4).  If it contains dummies, their hard-slot
neighbourhood is all of `H_slot\setminus S0`; for fixed real part `X`, the
strongest Hall inequality uses all `1748-t` residual dummies and reduces to

\[
 |N_F(X)|+18646-t\ge |X|+1748-t,
\]

which is exactly the second row.  These are all residual left subsets.

More generally, let `Q_R` be any forced real-edge partial matching.  Delete
its real-bottom endpoints `B0`, its singleton-host endpoints `F0`, and its
hard-slot endpoints `H0`.  Put `q_H=|H0|`, and require
`S0` disjoint from `H0`.  The combined real-edge/dummy-pin extension exists
if and only if, for every residual real-bottom family
`X subset H_real\setminus B0`,

\[
\boxed{
\begin{aligned}
 |N_F(X)\setminus F_0|
 +|N_H(X)\setminus(H_0\cup S_0)|&\ge |X|,\\
 |N_F(X)\setminus F_0|&\ge |X|-16898+q_H.
\end{aligned}}                                                   \tag{2.5}
\]

This is merely residual Hall with the symmetric dummy shore compressed; it
is the one test to use when the opening `C6`, private short hosts, and a
state macro impose pins simultaneously.

For mixed requirements -- fixed real-bottom placements together with fixed
short hosts -- (2.1) or equivalently (2.5) is load-bearing.  A socket
geometry is not a substitute for this residual Hall test.

Condition (2.4) applies only to dynamic hard slots.  The authenticated
two-phase `2S` macro

```text
13416 -> 298 -> 292 -> 297, states 0,1,7,0
cells 66627,3143,2057,1166,2064,32
```

uses old fixed `P0-P2` row `298` and dynamic-hard short row `292`.  Only
`s_292=1` is a dummy-host pin; row `298` is not.  Its two long endpoint modes
also activate the real self placements `p_(13416,13416)=1` and
`p_(297,297)=1`.  Hence its outer *difference* is zero, but its activation
support is not empty.  Combining it with a planted opening circuit requires
putting those real pins and `S0={292}` into the single test (2.5).

## 3. State and reset boundary

In the free abelian group on physical middle vertices, put
`partial(u->v)=[v]-[u]`.  Then

\[
\begin{aligned}
 \partial Q^-&=[A']+[B']+[C']-[A]-[B]-[C],\\
 \partial Q^+&=[A']+[B']+[C']-[A]-[B]-[C],
\end{aligned}                                                    \tag{3.1}
\]

and consequently

\[
                         \partial(Q^+-Q^-)=0.                   \tag{3.2}
\]

The same identity holds for every additive endpoint-local reset label
`rho`, because the old and new tail multisets and head multisets agree
literally:

\[
 \sum_{a\in Q^+}(\rho(h_a)-\rho(t_a))
 =
 \sum_{a\in Q^-}(\rho(h_a)-\rho(t_a)).                           \tag{3.3}
\]

This is a **relative** zero boundary.  The common absolute value in (3.1)
is generally nonzero.  Indeed the authenticated endpoint topology after the
opening is `P62+P2`, with four degree-one vertices.  Those two path
signatures still need exterior endpoint routing.  Transition-dependent
history, address, or reset labels are not present in the local theorem and
must be replayed; (3.3) applies only to labels determined additively by the
literal endpoint.

The lower, upper, tail, and head resource multisets also have relative
boundary zero by the authenticated identity

\[
             \operatorname{res}\{e,o1,o2\}
             =\operatorname{res}\{n1,n2,n3\}.                   \tag{3.4}
\]

## 4. Exact frozen-suffix obstruction

The bottom-actuator audit table `029d3be5...` and the res1972 origin table
`db960ce5...` have byte-identical target-chain and root columns; only their
owners differ.  This common payload has `18,646` eligible real bottom tokens
and exactly `10,025` hard slots with consecutive suffix ranks `6<7<8`.  The
complete exact suffix census is

\[
\begin{array}{c|rr}
 &\text{raw suffix sockets}&\text{native circuits}\\ \hline
 C_6&96619&246\\
 C_8&287269&16\\
 \text{saturated }B_5\ C_{10}&0&0.
\end{array}                                                     \tag{4.1}
\]

The zero is a property of the fixed `(M_v,U_v)` catalogue before a bottom
perfect matching is chosen.  An exact rowwise comparison finds zero suffix
mismatches across all `18,663` original length-three rows after round-47
bottom relocation.  That relocation changes only which real bottom enters a
hard/free host, or which hard host is bottomless.  The s7 carrier transport
then changes only the owner of each physical row: each phase has zero
target-chain/root mismatches against round 47.  Therefore both authenticated
s7 owner phases have the same `10,025`-slot suffix catalogue and still have
saturated-`C10` census `0/0` under every matching in this bottom-relocation
fibre.

The three-socket construction requires three saturated `B5 C10` fibre
switches before its fusion and opening `C6` moves.  Since the unchanged
fibre cannot instantiate even one such socket, it certainly cannot
instantiate the required three.  Consequently the stronger exact verdict is

```text
FROZEN_SUFFIX_C10_NOGO
```

not merely absence of a recorded row map.  The additional hypothesis is a
suffix rethread, or an explicit planted geometry, which creates three
pairwise resource-disjoint saturated `B5 C10` suffix sockets together with
the opening `C6` slots.  Only after that expansion do the typed identities
(1.5)--(1.8) and residual Hall tests (2.1)/(2.5) become applicable.

This is scoped to the frozen lower `6<7<8` suffix face.  It is not an
all-K17 or all-dimensional no-go, and it says nothing against a construction
which genuinely moves/rethreads the suffix level.  If the intended module
acts on `7<8<9` instead, it is outside the bottom-TU face for the same reason:
rank-seven objects are suffix resources there, not movable bottoms.

## 5. Current carrier and state scope

The current authoritative carrier checkpoint has endpoint
`R/H/Phi=1918/1681/5517` and robust lower-projection score `(59,49)`.  The
separate six-cell macro `13416 -> 298 -> 292 -> 297` is an authenticated
two-phase positive `2S` state column covering two roles from the native
`5,969` one-short zero list.  Its exact state boundary is

\[
                    e_{(297,0)}-e_{(13416,0)},                  \tag{5.1}
\]

and its outer matching difference is zero.  It neither supplies a saturated
`C10` suffix nor closes its own state boundary, so it does not bypass (4.1).

Even after a suffix expansion, a promoted module would still need:

* a residual Hall certificate for all real and dummy pins;
* either carrier owner's literal address/history states at the four exposed
  `P62+P2` endpoints; and
* an accepting return packet which closes the nonzero absolute path
  boundary.

The local `C6`, palette identity, and topology calculation cannot be
promoted to a K17 source, compiler, or word claim without those tests.

## 6. Frozen inputs

The accompanying bundle is

```text
scratch/k17_three_socket_augmented_matching_interface_20260802/
```

It binds the local theorem and opening audit, the frozen K17 saturated-C10
no-go, the current carrier audit, the common two-phase `2S` calibration, both
six-edge ledgers, and this note.
