# K17 alternating bottom circuits, compound-state sockets, and the three-socket gate

**Date:** 2026-08-02  
**Status:** exact boundary theorem, two-phase `2S` witness, and fail-closed
three-socket interface.  The current authenticated carrier is the checkpoint
with residence `1918`, deep-upper-hole count `1681`, and robust lower
projection pair `(deficiency,zero hard heads)=(59,49)`.  Its common scalar
payload is `Phi=2*1918+1681=5517`; its manifest and model hashes are recorded
in Section 7.  Nothing below proves a complete state cycle cover, a connected
chronology, source, common-cap closure, a compiler, or a word.

## 0. Result

There are three distinct incidence operators in this problem, and they must
not be identified.

1. An alternating circuit in the augmented bottom-token graph has zero
   **matching-node** boundary and zero aggregate named-target boundary.
   Its fully row-labelled table boundary is generally nonzero.
2. A literal compound state word through `k` short roles has endpoint
   boundary

   \[
             [\mathrm{right}]-[\mathrm{left}],
   \]

   while its `k` short-demand incidences are positive resources, not
   cancelled internal states.
3. A replacement packet is closed only when its signed long-state, short
   cover, matching, and every declared additive ticket boundary all close.
   Nonlinear topology and history predicates still have to pass at every
   actual prefix.

The authenticated relay suffix

```text
29 -> 520 -> 2117
```

is exactly a one-dummy alternating matching circuit.  This gives a general
serialisation theorem for every such circuit.

On the current two transported `s7` owner phases there is also one exact
common compound-state column

```text
long(13416,0) -> short(298,1) -> short(292,7) -> long(297,0),
```

with literal six-cell word

```text
66627,3143,2057,1166,2064,32.
```

Both internal short roles occur in the frozen `5969`-row native one-short
zero list.  Their two addresses are canonical physical addresses.  This
turns two previously empty one-short demand rows into incidences of one
legal `2S` column, simultaneously in both transported phases.  The column
is not closed: its exact long-state boundary is

\[
              e_{(297,0)}-e_{(13416,0)}.                 \tag{0.1}
\]

The three-socket `C60` opening switch has relative state/reset boundary
zero, so it cannot cancel (0.1).  An exact common long-only return of length
at most two was exhaustively absent across `67652` possible middle states.
No claim is made about a longer return, a return containing short macros, or
a return after another bottom assignment.

A second common column hosts three frozen-zero roles:

```text
(15767,1) -> (2315,7) -> (2189,7) -> (2190,7) -> (1518,1).
```

It too is reset-neutral and state-open.  Exact full-list searches find no
common closed `2S` and no common closed canonical `3S` in the stated fixed
languages.  The current tables also contain one selected three-zero physical
fusion hex, but its dummy rotation is only a `G_bot` gauge circuit and none
of its `6300` audited completions supplies the full old `C60` module.

Finally, the abstract `C60` opening becomes one alternating bottom-token
`C6` only after a typed co-middle injection and a residual Hall test.  No
such injection is authenticated on the current carrier.  More sharply, the
frozen K17 suffix catalogue contains zero raw and zero native saturated
`B_5 C10` sockets, while the three-socket construction requires three.
Bottom relays do not alter those suffixes.  Thus the complete `C60` route is
blocked in the unchanged bottom-matching fibre; suffix rethreading or a
different actuator geometry is the exact missing expansion.

## 1. The augmented matching and its boundary maps

Let

\[
 G_{\rm bot}=(\mathcal B\mathbin{\dot\cup}\Delta,
              \mathcal F\mathbin{\dot\cup}\mathcal H^{\rm slot};E)
                                                               \tag{1.1}
\]

be the augmented graph from the bottom-token theorem.  Its real left
vertices are the named bottoms `b`; its `1748` dummy vertices represent
bottomless hard slots.  A real bottom can enter a singleton or hard host
exactly when the corresponding strict containment holds.  A dummy can enter
every hard host and no singleton host.

Fix a perfect matching `P`.  Orient a signed exchange vector by giving new
edges coefficient `+1` and old edges coefficient `-1`.  Let `N_bot` be the
head-minus-tail incidence matrix of (1.1).  If `C` is an alternating even
circuit, put

\[
       \gamma_C=\mathbf 1_{C-P}-\mathbf 1_{C\cap P}.          \tag{1.2}
\]

Then

\[
                         N_{\rm bot}\gamma_C=0.                \tag{1.3}
\]

Flipping `C` therefore gives another perfect matching.

For a hard host `v`, write `L_v(b)` for the long row with bottom `b` and
`S_v` for its bottomless short row.  For a singleton host `f`, write `T_f(b)`
for the resulting short row.  The exact row-labelled boundary of a matching
circuit is

\[
 \beta_{\rm row}(C)=
 \sum_{w\in V(C)\cap(\mathcal F\dot\cup\mathcal H^{\rm slot})}
 \bigl([\operatorname{row}(w,P\triangle C)]
       -[\operatorname{row}(w,P)]\bigr).                       \tag{1.4}
\]

This vector is generally nonzero.  Its projection to the multiset of named
targets is zero, since the same real bottom tokens occur on both halves of
the circuit and every fixed suffix remains on its host.  Its owner/root and
global chain-histogram projections are also zero.  The slotwise long/short
mode vector can be nonzero, although its total short count is zero.

The symmetric difference of any two perfect matchings is a vertex-disjoint
union of alternating even circuits.  This is the exact cycle-space normal
form for static bottom relocation.  It does not by itself supply a legal
chronological sequence or literal state compatibility.

## 2. One-dummy circuits are serial relay paths

### Theorem 2.1 (apertured circuit serialisation)

Suppose one alternating circuit has exactly one dummy `delta` and only hard
hosts.  Label its old matching edges

\[
       \delta h_r,\qquad b_i h_i\quad(0\le i<r),              \tag{2.1}
\]

and its new edges

\[
       \delta h_0,\qquad b_i h_{i+1}\quad(0\le i<r).          \tag{2.2}
\]

Then the flip has an exact relay serialisation: for
`i=r-1,r-2,...,0`, move `b_i` from `h_i` to the current short host
`h_(i+1)`.  Every prefix remains an exact strict-chain target partition.

Its exact row boundary is

\[
\begin{split}
 \beta_{\rm row}(C)={}&S_{h_0}-L_{h_0}(b_0)\\
 &+\sum_{i=1}^{r-1}\bigl(L_{h_i}(b_{i-1})-L_{h_i}(b_i)\bigr)\\
 &+L_{h_r}(b_{r-1})-S_{h_r}.                         \tag{2.3}
\end{split}
\]

After forgetting bottom labels, all internal modes cancel and the aperture
moves from `h_r` to `h_0`:

\[
 \beta_{\rm mode}(C)
 =(S_{h_0}-L_{h_0})+(L_{h_r}-S_{h_r}).                       \tag{2.4}
\]

#### Proof

Initially `h_r` is short.  Moving `b_(r-1)` into it makes `h_(r-1)` short.
Inductively this is exactly the destination required by the next move.
Every new real assignment is an edge of `G_bot`, so the regenerated chain is
strict.  Each step merely transports one named bottom between two fixed
suffixes, proving exact target, owner, root, and histogram preservation at
every prefix.  Summing the before/after row states gives (2.3); every
internal short interface occurs once with each sign.  QED.

For the authenticated suffix, the old and new edges are

\[
\begin{aligned}
 P\cap C&=\{\delta\!\to2117, b_{520}\!\to520,
                         b_{29}\!\to29\},\\
 (C-P)&=\{b_{520}\!\to2117, b_{29}\!\to520,
                         \delta\!\to29\}.                    \tag{2.5}
\end{aligned}
\]

Here `b_29=158` and `b_520=4174`.  Formula (2.3) becomes

\[
 S_{29}-L_{29}(158)
 +L_{520}(158)-L_{520}(4174)
 +L_{2117}(4174)-S_{2117},                                  \tag{2.6}
\]

which is the independently audited round-21 to round-23 boundary.

A dummy-free matching circuit need not have such a relay chronology.  The
compatible swap `0 <-> 495` in the frozen donor graph is the smallest exact
counterexample: it is a valid static alternating `C4`, but neither occupied
host supplies the initial aperture required by a status relay.  A
dummy-bearing aperture, an independently audited external buffer ear, or an
atomic relaxed transaction is therefore an exact extra hypothesis for
sequential use.

## 3. Compound-state columns

Let `V_L` be the literal long states `(row,flag)` and `V_S` the literal
short states `(row,address)`.  A `kS` word has `k+4` nonempty cells
`C_0,...,C_(k+3)` and supports

\[
 \ell\text{ on }C_0,C_1,C_2,qquad
 s_j\text{ on }C_j,C_{j+1},C_{j+2} (1\le j\le k),qquad
 r\text{ on }C_{k+1},C_{k+2},C_{k+3}.                        \tag{3.1}
\]

The owner-entry differences of `s_1,...,s_k,r` occur in cells
`C_0,...,C_k`.  Every short's declared inner and outer interval unions must
equal its two named targets exactly.  The endpoint long families and all
cell upper/lower boxes are literal.

These conditions have an exact bounded verifier.  For each of the 17
coordinates, enumerate its membership pattern in the `k+4` cells.  Retain a
`2^(k+4)`-state mask recording which cells have been seen nonempty.  The
terminal all-one mask exists if and only if a literal word exists.  Thus the
test costs `O(17*4^(k+4))`; in particular `2S` and `3S` require only 64 and
128 seen states respectively.

### Theorem 3.1 (exact contraction signature)

Expand a literal `kS` word as the state path

\[
          \ell\longrightarrow s_1\longrightarrow\cdots
                    \longrightarrow s_k\longrightarrow r.    \tag{3.2}
\]

Its state-incidence boundary and short-demand vector are

\[
       \partial_{\rm st}\mu=e_r-e_\ell,qquad
       d_S(\mu)=\sum_{j=1}^k e_{s_j}.                          \tag{3.3}
\]

The internal state incidences telescope.  The demand vector does not
cancel: every short role is consumed once by the absolute cover equations.
For an augmentation between two complete covers, the *signed difference* of
the short-demand vectors must be zero.

If `m_k` is the number of selected `kS` columns and `m_LL` the number of
direct long--long columns, every K17 complete cover satisfies

\[
 \sum_{k\ge1}k m_k=7395,qquad
 m_{LL}+\sum_{k\ge1}m_k=16915.                               \tag{3.4}
\]

With only `1S`, `2S`, and `3S` columns this is

\[
       m_{LL}=9520+m_2+2m_3,qquad
       m_1=7395-2m_2-3m_3.                                  \tag{3.5}
\]

Thus a `2S` or `3S` column is a rank-two or rank-three hyper-ticket.  It
does not satisfy the unary-short premise of a private-ticket transversal
matroid and must not be split into independent ticket variables without an
exact coupling row.

## 4. The authenticated common `2S` column

The same four physical rows occur in both transported `s7` owner phases:

```text
row    owner  root   chain
13416  76879  68687  66627,68679,68687
298    68815   3279  3143,3279
292     3295   3231  3215,3231
297     3263   3262  1166,3230,3262
```

The state sequence is

\[
 (13416,0)\longrightarrow(298,1)\longrightarrow(292,7)
                         \longrightarrow(297,0),               \tag{4.1}
\]

and the cells are

\[
 (66627,3143,2057,1166,2064,32).                              \tag{4.2}
\]

Direct OR replay gives

\[
\begin{array}{c|ccc}
\text{window}&\text{bottom}&\text{middle, if present}&\text{root}\\ \hline
13416&66627&68679&68687\\
298&3143&-&3279\\
292&3215&-&3231\\
297&1166&3230&3262.
\end{array}                                                   \tag{4.3}
\]

The three entering owner differences are `65536`, `64`, and `1`, contained
respectively in cells `C_0,C_1,C_2`.  Address `1` has inner/outer masks
`1/7` and is a canonical `P0-P2` address for row `298`.  Address `7` has
masks `3/7` and is a canonical `P1-P2` address for row `292`.  The exact
coordinate DP independently enforces both inner/outer covers and all six
nonempty cells.

Rows `298` and `292` occur literally in the frozen native zero list as

```text
292 7 7 6
298 6 1 3
```

and each has zero native five-cell socket triples.  The statement is about
their membership in that authenticated fixed-table list; a complete one-short
recensus of each transported owner phase has not been claimed.

The exact column signature is

\[
\begin{aligned}
 \partial_{\rm st}\mu&=e_{(297,0)}-e_{(13416,0)},\\
 d_S(\mu)&=e_{(298,1)}+e_{(292,7)},\\
 \Delta_{\rm matching}\mu&=0,\\
 \Delta_{\rm target/mode/owner}\mu&=0.                       \tag{4.4}
\end{aligned}
\]

Its endpoint flag/reset scalar is neutral (`0 -> 0`).  This does not assert
zero transition-dependent history.

Although the relative outer delta in (4.4) is zero, activation in a variable
bottom master is not support-free.  It implies

\[
 p_{13416,13416}=1,qquad p_{297,297}=1,qquad s_{292}=1,       \tag{4.5}
\]

while row `298` is an old fixed `P0-P2` short.  All mixed real/dummy pins in
(4.5) must be included in any residual Hall test.

### A common canonical `3S` column

There is also an exact common seven-cell word

\[
 (15767,1)\longrightarrow(2315,7)\longrightarrow(2189,7)
 \longrightarrow(2190,7)\longrightarrow(1518,1)                \tag{4.6}
\]

with cells

\[
 (65537,13346,8197,4259,8704,683,1024).                        \tag{4.7}
\]

It was found in the declared prefix consisting of the first `1024` frozen
zero roles and then replayed literally in both `s7` phases.  This is a
positive witness, so the restricted discovery range does not weaken its
validity; it is not a census of all open `3S` columns.

Its exact windows are

\[
\begin{array}{c|ccc}
15767&13346&78883&78887\\
2315&13351&-&13479\\
2189&12455&-&12967\\
2190&12963&-&12971\\
1518&683&8875&9899.
\end{array}                                                    \tag{4.8}
\]

The four owner-entry differences are `65536,1024,4,4096` in cells
`C_0,C_1,C_2,C_3`.  All three shorts use canonical `P1-P2` address `7`, all
three are dynamic hard slots occurring in the frozen native zero list, and
both endpoint flags are `1`.  Therefore

\[
\begin{aligned}
 \partial_{\rm st}\mu_3&=e_{(1518,1)}-e_{(15767,1)},\\
 d_S(\mu_3)&=e_{(2315,7)}+e_{(2189,7)}+e_{(2190,7)},\\
 \rho(\mu_3)&=0.                                               \tag{4.9}
\end{aligned}
\]

It is another open column, not a state circulation.  In the variable outer
master it activates `p_(15767,15767)=p_(1518,1518)=1` and
`s_2315=s_2189=s_2190=1`.

## 5. The three-socket `C60` interface

The authenticated local topology is

\[
 15C_4+2K_2\longrightarrow3C_{20}+2K_2
 \longrightarrow C_{60}+2K_2\longrightarrow P_{62}+P_2.      \tag{5.1}
\]

The last opening uses old matching `Q-={e,o1,o2}` and new matching
`Q+={n1,n2,n3}` on the same six distinct physical middle vertices.  Their
union is one alternating physical `C6`.  If `zeta=1_(Q+)-1_(Q-)`, then the
relative endpoint-state boundary and every additive endpoint-local reset
boundary are zero:

\[
                   \partial_{\rm phys}\zeta=0.                 \tag{5.2}
\]

The common absolute boundary of either matching need not be zero.  The
opened object has four path endpoints and still needs exterior routing.

### Theorem 5.1 (typed bottom lift and residual Hall)

For every opening atom `(L,U,T,H)`, choose a **real** bottom token `b_L` and
a hard slot `v` with fixed suffix `(M_v,U_v)=(H,U)` such that

\[
             L\subset H,qquad
             \chi(L;v)=L\cup(U_v-M_v)=T.                       \tag{5.3}
\]

Require the three lower tokens and three slots to be distinct, the old
three assignments to be selected or pinned, and all three crossed new
assignments to satisfy (5.3).  Dummies are excluded from these six interval
atoms.  Then the two assignment triples are the two halves of one
alternating `C6` in `G_bot`.

If the old triple is not already part of a complete matching, delete the
six incident vertices.  It extends to a perfect matching if and only if the
residual graph satisfies

\[
                         |N(X)|\ge|X|                            \tag{5.4}
\]

for every residual left set `X`.  Any such extension flips automatically to
an extension containing the new triple, so no second Hall test is required.

If a set `S_0` of `t` eligible hard slots is forced dummy matched and there
are no other pins, the exact quotient form is

\[
\begin{aligned}
 |N_F(X)|+|N_H(X)\setminus S_0|&\ge|X|,\\
 |N_F(X)|&\ge|X|-16898                                      \tag{5.5}
\end{aligned}
\]

for every real-bottom set `X`.  Here `S_0` must be disjoint from the three
long opening slots.  Formula (5.5) applies only to dynamic hard slots; it
does not represent old fixed or free short roles.  With the real pins and
`s_292=1` from (4.5), one must instead pin everything together and apply
the single residual test (5.4).

### Theorem 5.2 (exact three-port state closure)

Let the three private socket interiors carry literal compound fillers
`mu_1,mu_2,mu_3`, with pairwise disjoint short-demand supports and only their
declared endpoint ports identified.  Because (5.2) is relatively zero, the
combined state/reset boundary closes exactly when

\[
       \sum_{j=1}^3\partial_{\rm st}\mu_j=0,qquad
       \sum_{j=1}^3\rho(\mu_j)=0.                              \tag{5.6}
\]

This statement treats the `C60` as already planted and audits its final
opening.  If the preceding three `C10` switches and first fusion `C6` are
included in the same state transaction, their exact state/reset boundary
must be added to the left side of (5.6).  Equality of their four resource
decks alone does not prove address- or history-state closure.

For unit path columns, the first equality says that the tail-state multiset
equals the head-state multiset.  If the support is connected, it is one
directed state circuit.  The fillers host exactly two or three frozen zero
roles when their disjoint demand union meets that list in cardinality two or
three.  Every role still has to occur once in the global absolute cover.

If all fillers are downward/neutral and the three ports are glued cyclically
without an upward connector, (5.6) forces every flag change to be neutral:
a cyclic chain of weak inequalities can have no strict one.  A strict reset
therefore needs an explicitly replayed upward connector.

The current one-column bank cannot satisfy (5.6), since (0.1) is nonzero and
the opening column contributes zero.  In the two-column span generated by
the opening `zeta` and `mu`, the state-row functional

\[
 \pi(297,0)=1,qquad \pi(13416,0)=0,qquad \pi=0\text{ elsewhere} \tag{5.7}
\]

has `pi partial(zeta)=0` and `pi partial(mu)=1`.  This is the exact one-row
separation certificate: a packet using `mu` once cannot close using only
relative-zero module columns.

### The selected current physical hex is not a planted module

Both transported phases contain the same three dynamic-hard frozen-zero
short rows as one selected old vertical triple of the abstract fusion:

```text
row   lower  upper  tail   head/root
4354  22930  23958  23954  22934
4550  23698  24214  24210  23702
4424  23186  23446  23442  23190
```

Here `S=22674` and the four markers are
`alpha=256,gamma=1024,beta=512,delta=4`, with one consistent reverse
orientation.  The corresponding new triple is

```text
(22930,23446,23442,22934)
(23698,23958,23954,23702)
(23186,24214,24210,23190).
```

The old/new lower, upper, tail, and head multisets agree separately, and
their tail--head matchings form one physical alternating `C6`.  This is a
genuine selected fusion-hex injection, but it is not a complete `C60`
planting.  The exact state audit finds no common closed `2S` word on any pair
of these three rows and no common closed `3S` word in any of their six
orders, even with all nine short addresses.

The augmented bottom graph contains a different, automatic circuit on the
same hard-slot names:

\[
\begin{aligned}
 Q^-_\Delta&=\{d_1\!\to4354,d_2\!\to4550,d_3\!\to4424\},\\
 Q^+_\Delta&=\{d_1\!\to4550,d_2\!\to4424,d_3\!\to4354\}.       \tag{5.8}
\end{aligned}
\]

This is a dummy-label gauge `C6`.  Both halves leave the same three hosts
short and materialize the identical table.  It is not the physical fusion
hex and supplies no non-gauge co-middle actuator.  This example is the exact
reason that “one physical alternating `C6`” and “one useful `G_bot`
circuit” require the typed condition (5.3), not merely matching incidence.

For the selected physical hex, the declared completion audit examines
`6300` old three-socket completions.  None has all `60` required old atoms
in either transported table; the best phase-0, phase-1, and common counts are
respectively `9/60`, `8/60`, and `8/60`.  This is a current-table membership
obstruction in addition to the suffix-catalogue obstruction below.  Its
scope is precisely the enumerated completion family bound by the frozen
auditor.

## 6. Return-path and frozen-suffix obstructions

An exact return for (4.1) must run from `(297,0)` to `(13416,0)` in the
literal product graph while avoiding already consumed short resources and
restoring every additive ticket.  A return path is sufficient only after
every microscopic head is hard-legal and topology/history pass at every
prefix.

The finite common-phase audit checked:

* the direct canonical long--long transition; and
* every two-edge canonical long--long path through one common intermediate
  `(row,flag)`.

There are `16913*4=67652` possible middle states after excluding the two
endpoints.  The exact four-cell transition predicate was evaluated on both
transported phase tables at every edge.  The result was

```text
PASS_K17_S7_NO_COMMON_RETURN_LENGTH_LE2
start=297,0 finish=13416,0 tested_middle_states=67652
```

This is a bounded negative result only.  It excludes no length-three path,
no return using a `1S/2S/3S` macro, and no return after an alternating bottom
circuit changes the table.

Separate compound searches establish the following additional, still
finite, boundaries on the unchanged two-phase tables.

1. There is no common **closed** `2S` word whose two distinct shorts are
   drawn from all `5969` frozen native zeros, even allowing all nine short
   addresses.  The exact search performs `9,143,394,738` necessary
   pair-filter tests and reaches no six-cell-DP candidate.
2. There is no common closed canonical `3S` word whose three shorts are
   drawn from the same full zero list.  The exact search performs
   `2,567,628,296` necessary pair-filter tests and reaches no seven-cell-DP
   candidate.
3. For the promoted open `2S` boundary (0.1), there is no disjoint return
   using only two or three frozen-zero shorts in the audited compound
   language.  Its only common first-state options are `(1861,5)` and
   `(1861,6)`, its only common final-state option is `(15315,6)`, and the
   required connecting zero-short path is absent.

These are exact no-go statements for their enumerated fixed-table languages,
not for arbitrary compound renewal.  In particular they do not exclude a
cycle of two or more open macros using at least four shorts, a path mixing
direct long arcs with compound macros, a nonzero-helper short, a longer
return, or a regenerated table after an outer matching circuit.

For any declared finite lifted return graph, add an accepting sink at exact
closed returns.  If `R` is the set reachable from the head of (4.1) and the
sink is not reachable, then

\[
 z=-\mathbf1_R,qquad N^Tz\le0,qquad
 (e_{\rm sink}-e_{(297,0)})^Tz=1                              \tag{6.1}
\]

is the exact Farkas accepting cut.  If the sink is reachable and arc costs
record a declared Lyapunov payload, the usual min-cost circulation/Bellman--
Ford dual decides whether a negative closed packet exists.  Short-use masks,
outer pins, and history tickets must be coordinates of this lifted graph;
an unlifted scalar Hall projection is not equivalent.

There is an independent, earlier obstruction to using the complete
three-socket architecture inside the unchanged bottom fibre.  On the frozen
K17 consecutive `6<7<8` suffix table, the exact raw/native circuit census is

```text
type                 raw sockets   native circuits
C6                       96619             246
C8                      287269              16
saturated B5 C10             0               0
```

The construction (5.1) requires three saturated `B_5 C10` sockets.  A
bottom relay changes only bottom assignments and leaves every fixed suffix
unchanged.  Therefore no number of preliminary bottom relays can create the
missing sockets.  A suffix rethread which creates three pairwise compatible
`C10` sockets, or a different topology module not using them, is the exact
additional expansion hypothesis.  Even after such an expansion, (5.3)--
(5.6), residual Hall, and all hard-prefix predicates remain necessary.

## 7. Authentication and scope

Current carrier:

```text
checkpoint manifest
b99333b131b5ddbf0ab36909ee91dfbdb4dcaeee8686c353f186c5290126eba9
model
37a160f2b3f02839fcd9621dccb42cce43a0297016cdf050ded742baa6f84748
phase-0 transported table
ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207
phase-1 transported table
736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058
```

Frozen structural inputs:

```text
native zero-role list
ada18b7eafa26675f6ac52efb997e38b5576c1fd7a3ee98a51665dc57bb52f06
three-socket theorem
34503994be94c1c4e2ec444353fd851b56695fee65416d4d8046ce67b30a1ee8
C60 opening corollary
e83f8e02bd5e7262c8532aeea441a25ea29d31dbfb154857ea8377cabcd0bb98
three-socket topology audit
437565b36c367896f7b30afee4175ced5f95804997428c78463ca7f33007e40f
bottom interval/C10 obstruction theorem
c97b9ebcec98c481717908260ae12df5a2a5c4474e83826e6b08b3327dd18b31
bottom interval audit
c158ef6d43d706ce57de010d97b0a18201af1a4e09b46d32fe5d4edf3e8f0c61
typed C60 augmented-matching interface theorem
17b20e105a7dc77379309a62bf4224a9349c8c82702539463f729c5e72b270cd
typed C60 interface bundle manifest
2b453cf01f90b6e1966388c93fd0021fb10f7e5e64dbe83b771559b70162b019
common long-only return auditor source
dd0243493f72e5dcdd5b3e90fef5d8d4acb34eed30153fa2a42647dca34611b4
common fixed-`3S` replay auditor source
2929549a9e156cf91c0433abecf665715b29ef2c142f36bbef4220544067fde6
common fixed-`3S` replay output
2d8129bb525237131c07ea977c766d2653cb241a894e73053ffd8caa2987f20e
common `2S/3S` and selected-hex bundle manifest
cec7c7ea09ad03c591049b121368b5adc81282c1af2e163644129741d2249fb3
```

The frozen bundle named in Section 8 binds the two-phase `2S` replay, the
bounded return audit, the exact interface ledger, and these structural
inputs.  It does not authenticate a complete `2S/3S` cover, a typed K17
planting of the abstract `C60`, a longer return, topology in the ambient
carrier, residence or upper improvement, source, compiler completion, or a
word.

## 8. Frozen bundle

```text
scratch/k17_alternating_matching_compound_state_theorem_20260802/
```
