# Coatom depth-jump collars are explicit nested chains; protected host extension is a state-filtered port-completion gate

Date: 2026-08-01  
Lane: L, additive-constant regenerative planting  
Status: exact local monotone-collar construction and exact fixed-forest
completion criterion.  The global accepting completion is not proved, and
no unconditional additive-constant conclusion is claimed.

## 0. Outcome

The boundary staircase of the zero-defect endpoint-planted coatom packet is
not itself an existential obstruction.  Put

\[
                         h=D+2
\]

for the child positive-run threshold after a depth jump.  The child packet
has common boundary coordinates

\[
 B=\{g_0,g_1,\ldots,g_D,z\}
\]

with clipped profiles

\[
 \beta(g_0)=(h,h),\qquad
 \beta(g_i)=(i,h-i)\ (1\le i\le D),\qquad
 \beta(z)=(h-1,1).                                      \tag{0.1}
\]

One private bank `U={u_0,...,u_D}` of exactly `h-1` labels supports two
nested Johnson collars, one on each side.  They make both boundary runs of
every coordinate in `B` have length at least `h`.  Every other old boundary
coordinate is retained through all `h-1` collar owners and is likewise
saturated.  The only unsaturated boundary state left by the superfragment
belongs to `U`, and it is an explicit monotone prefix/suffix staircase.

Consequently, for a bounded bank of owner-disjoint packets, pairwise-private
`U` banks make the complete collared packet paths owner-disjoint and
residence-safe internally.  What remains is global: extend this protected
path forest to one safe spanning child chronology.  For a fixed orientation
and residence-state face, the owner-topology part is exactly a physically
simple port matching whose contracted quotient is one path.  Immediate
palette and complete interval-OR-deck acceptance remain additional rows.
No existing same-parity theorem in the repository proves that this joint
completion always exists.

## 1. The exact left and right collars

Let `P` be either phase of the endpoint-planted child packet.  Its ordered
endpoints `E_-` and `E_+` have rank `R`, both contain `B`, and differ in the
active endpoint label (`infinity` versus `e`).  Let

\[
 U=\{u_0,u_1,\ldots,u_D\}
\]

be disjoint from every coordinate occurring in `P`.

For `1<=s<=D+1`, define the left collar, written from the exterior toward
the packet, by

\[
\begin{split}
 L_s={}&E_- -\{g_0\}-\{g_i:s<i\le D\}
                 -\bigl(\{z\}\text{ if }s\le D\bigr)\\
      &+\{u_0\}+\{u_i:s<i\le D\}
                 +\bigl(\{u_1\}\text{ if }s\le D\bigr).       \tag{1.1}
\end{split}
\]

The two displayed `u` sets are disjoint because `s>=1`.  Thus

\[
 L_s\longrightarrow L_{s+1}
\]

replaces `u_(s+1)` by `g_(s+1)` for `s<D`, the last internal step replaces
`u_1` by `z`, and `L_(D+1)->E_-` replaces `u_0` by `g_0`.

Define the right collar, written from the packet toward the exterior, by

\[
 R_s=E_+-\{g_0\}-\{g_i:1\le i<s\}
             +\{u_0\}+\{u_i:1\le i<s\}.                       \tag{1.2}
\]

Here `E_+->R_1` replaces `g_0` by `u_0`, and
`R_s->R_(s+1)` replaces `g_s` by `u_s`.

### Theorem 1.1 (nested monotone collar)

The concatenation

\[
                 L_1\cdots L_{D+1}\;P\;R_1\cdots R_{D+1}     \tag{1.3}
\]

is a simple rank-`R` Johnson path whenever `P` is simple.  It has no closed
positive run shorter than `h`.  Every old packet-boundary run is either
closed with length at least `h` or reaches an outer boundary already clipped
at `h`.  The only unsaturated outer boundary runs are the private-label runs

\[
\begin{array}{c|cc}
 &\text{left prefix}&\text{right suffix}\\ \hline
 u_0&h-1&h-1\\
 u_1&h-2&h-2\\
 u_i\ (2\le i\le D)&i-1&h-1-i.
\end{array}                                                    \tag{1.4}
\]

Zero entries in (1.4) mean absence at that boundary.

#### Proof

Every consecutive pair in (1.1)--(1.2), including the two packet joins,
differs by one deletion and one insertion.  All owners therefore have rank
`R` and every displayed step is a Johnson edge.

The private label `u_0` occurs in every collar owner and nowhere in `P`.
Thus no collar owner is a packet owner.  The left and right collars cannot
meet each other: every left owner contains the active endpoint label
`infinity` and omits `e`, while every right owner contains `e` and omits
`infinity`.  Within either collar, the nested set of restored `g` labels
strictly changes at every step.  This proves simplicity.

Coordinate `g_i` occurs in exactly `h-i` left-collar owners and exactly `i`
right-collar owners.  Combining these with (0.1) gives the two packet-
boundary run lengths

\[
                         (h-i)+i=h
\]

on both sides.  Coordinate `z` occurs once on the left and in all `h-1`
right-collar owners, again giving `h` on both sides.  Coordinate `g_0` is
absent from the collars, but its two packet runs are already clipped at
`h`.  Every other coordinate in `E_-` or `E_+` is retained through all
`h-1` owners of the corresponding collar, so even a one-cell packet
boundary run reaches `h`.  Some of these legal runs close inside a collar
and some reach its exterior; in the latter case their clipped outer state is
already `h`.

All packet-internal closed runs are legal by the zero-defect tensor theorem.
Each `u_i` run touches an outer boundary of (1.3), and its lengths are read
directly from (1.1)--(1.2), giving (1.4).  No other new run occurs.  \(\square\)

The theorem does not pretend that the private `U` state has disappeared.
It replaces a candidate-dependent old-filler staircase by a deterministic
monotone boundary state on fresh labels, which is the correct interface to
the complementary chronology.

## 2. A bounded private bank

Take `H` endpoint-planted packets whose packet owner sets are pairwise
disjoint.  For packet `i`, choose a bank `U_i` of `h-1` coordinates such
that

1. the `U_i` are pairwise disjoint; and
2. every `U_i` is disjoint from the coordinate support of every packet.

### Corollary 2.1 (private collared path forest)

The `H` collared superfragments from Theorem 1.1 form a pairwise
owner-disjoint path forest, in either packet phase.  Toggling any subset of
the packets preserves this forest's owner set, ports, immediate palettes,
prefix/suffix/internal OR decks and residence boundary state.

#### Proof

Every collar owner for component `i` contains `u_0^i`.  That label occurs
in no packet and in no other component's collar, so collar owners cannot
collide across components or with packets.  Packet owners are disjoint by
hypothesis.  The two packet phases have equal owner sets and endpoints and
the exact U1--U4 signatures; their collars are literal common words.
Composition gives the assertion.  \(\square\)

This uses `H(h-1)` private coordinate labels, not `2H(h-1)`: the same bank
serves the two shores of one packet.  In a central `2R`-coordinate host the
label condition is an explicit planting hypothesis.  For fixed `H` and
`h=o(R)` it is asymptotically compatible with the linear endpoint-label
menu, but coordinate counting alone does not place the superfragments in a
Pascal child.

## 3. Exact owner-topology completion

Let `F` be any protected linear forest on a subset of the rank-`R` owner
layer.  In the present application its nontrivial components are the
collared packet paths.  Treat every unused owner as a singleton component
with two formal ports.  A port edge is an unused Johnson edge between the
underlying endpoint owners; it is **physically simple** if the same
underlying Johnson edge is not selected twice.

Fix orientations of all nontrivial components and a residence-state face.
Retain only connector edges certified compatible with that face.  If the
compatibility of a seam depends on a live clipped state, replace a port by
its state copy and impose the usual one-copy-per-component consistency.

### Theorem 3.1 (state-filtered port criterion)

For fixed distinct global ports `s,t`, the protected forest extends without
deleting a protected edge to one spanning Johnson path from `s` to `t` if
and only if its state-expanded port graph has a physically simple matching
which

1. leaves exactly `s,t` unmatched;
2. matches every other port once; and
3. becomes one connected path after every component of `F` is contracted.

For a cyclic carrier, match every port and require the contracted quotient
to be connected and two-regular.

#### Proof

Any extending Hamilton path uses one connector at every non-global port.
Those connectors are a physically simple port matching, and contraction of
the retained paths gives one quotient path.  Conversely, expand every
vertex of a connected quotient path through its oriented protected
component.  Port matching gives degree two at every internal owner and
degree one at `s,t`; connectedness and the partition of the owner layer give
one Hamilton path.  The state-copy filters give exactly the declared seam
compatibility.  The cyclic proof is identical.  \(\square\)

This is the path analogue of the endpoint-cycle criterion and is sharper
than ordinary Hall: a perfect port matching may consist of several quotient
cycles.  On a prepared acyclic/private connector face, the existing
graphic--gammoid theorem or its Hall-one specialization can certify the
connected row polynomially.  No such prepared face has yet been constructed
for the prospective coatom bank.

## 4. From owner completion to physical `PHE`

Theorem 3.1 closes only owner topology and the declared residence face.  A
safe child carrier also needs the residual immediate palettes and the full
interval-OR support.  For ordered fragments `A,B`, the exact deck identity
is

\[
 \operatorname{Deck}(AB)=\operatorname{Deck}(A)\cup
 \operatorname{Deck}(B)\cup
 \{S\cup P:S\in\operatorname{Suf}(A),
              P\in\operatorname{Pre}(B)\}.                    \tag{4.1}
\]

Therefore the physical prospective-host statement for a prescribed flag
word is equivalent to finding one state-expanded port completion from
Theorem 3.1 whose selected connector colours satisfy the residual immediate
palette row and whose ordered fragment product under (4.1) covers every
required upper target.  The packet toggles then preserve those rows
serially.

The distinction is exact:

* pairwise owner-disjoint planted packets plus Theorem 1.1 produce the
  protected path forest;
* they do not imply a connected port matching;
* a connected port matching does not imply the residual palette row; and
* topology plus palettes do not imply the global deck condition (4.1).

The bare Pascal attachment Hall theorem assigns components to distinct
native anchors, but explicitly excludes residence, protected upper
witnesses and the completed child chronology.  The local cone/insertion
recurrence regenerates the packet formula, not this complement.  The serial
safe-move theorem assumes the starting safe carrier.  Thus none of the
current same-parity results proves the joint accepting completion above.

The weakest physical theorem needed for one bounded terminal route is not
an all-packets extension theorem.  It is:

> for the one selected private packet bank representing the prescribed flag
> word, the state-expanded port system has one connected accepting solution
> satisfying the residual immediate palettes and (4.1).

Compiler U5 remains subsequent and nonlinear.  The saturated flag lattice
removes no part of this physical completion quantifier.

## 5. Lightweight audit

The dependency-free script

```text
python3 scratch/audit_o1_coatom_nested_collar_20260801.py
```

reconstructs both corrected endpoint-planted packet phases after a depth
jump, attaches (1.1)--(1.2), and checks for `1<=D<=20`:

* ranks, Johnson adjacency, simplicity and equal owner sets;
* pairwise disjointness from the private collar bank;
* exact clipped profiles (0.1) and (1.4);
* no closed run shorter than `h`;
* equality of both immediate-palette counters;
* equality of ordered prefix/suffix OR signatures and internal interval-OR
  support.

The finite replay validates the formulas; it does not construct the global
port completion, palette completion, upper deck or compiler.
