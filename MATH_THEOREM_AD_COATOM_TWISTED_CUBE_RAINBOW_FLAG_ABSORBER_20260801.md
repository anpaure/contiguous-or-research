# A four-packet twisted coatom cube cancels every lower flag without palette collisions

> **Correction, 2026-08-01.**  The signed/source-signature cancellation
> identity is exact, but its literal Klein four-block realization is not a
> simple-owner or strict-lower-rainbow physical packet.  The replay
> `scratch/audit_c8_fourblock_physical_owner_palette_nogo_20260801.py`
> gives owner multiplicity `2^2 4^(8d+22)` and lower-q1 multiplicity
> `2^4 4^(8d+20)`.  Adding uniform block-private tags separates resources
> but destroys the connected `K_(2,2)` cancellation equalities.  Thus the
> physical prepared-slot conclusions below require a nonliteral quotient
> weave and are not established by the literal four-block word.

Date: 2026-08-01  
Status: exact conditional serial absorber theorem.  Four explicitly
owner- and immediate-palette-disjoint planted packets preserve U1--U4 at
every intermediate step and restore the full lower-intersection counter at
every depth.  Global prepared-slot reachability and the nonlinear
address-labelled compiler U5 remain open.  Therefore this theorem does
**not** by itself prove `nu(k) <= B(k)+O(1)`.

## 0. Outcome

The saturated flag/Pluecker theorem proves that the canonical mixed-screen
packet has no local lattice obstruction.  A direct three-packet flag
triangle already telescopes, but it repeats one lower-q1 socket colour at
each of its three flag vertices.  It therefore cannot be planted unchanged
inside a strict lower-rainbow bank.

The following **twisted cube** removes that physical obstruction.  It uses
four canonical packets, two forward neutral filler flags and two reversed
ones.  The four packets have:

1. pairwise-disjoint literal owner sets;
2. pairwise-disjoint complete adjacent-intersection palettes;
3. pairwise-disjoint adjacent-union supports;
4. U1--U4 phase exactness separately; and
5. exact coefficientwise cancellation

   \[
       \sum_{i=0}^3
       \bigl({\cal L}_q(Y_i)-{\cal L}_q(X_i)\bigr)=0
                         \qquad(1\le q\le d).          \tag{0.1}
   \]

Thus four prepared slots can be toggled serially in any order.  Every
intermediate carrier remains U1--U4-valid, and the terminal lower target
counter through depth `d` equals the initial counter exactly.  The move has
only eight fixed exterior endpoints and no terminal lower-trace residue.

This is a uniform four-packet rainbow-compatible identity for every
`d>=2`.  It is not dimensionwise minimal: three filler-axis packets already
suffice at `d=2,3`.  For `d>=4`, a separate theorem rules out three packets
inside the normalized common-base square face.  The arbitrary-core
three-packet classification remains open, so no full canonical or global
minimality claim is made.

## 1. The one-packet action

For active roles `(e,a,b,c,delta,infinity)`, use the authoritative old/new
twelve-owner ECO paths

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab,           (1.1)
```

where, for example, `Ibc={infinity,b,c}`, `Cd={e,c,delta}`
and `bc={e,b,c}`.  Tensor a path by the ordered filler set

\[
                (f_0,g_1,\ldots,g_d,f_{d+1})          \tag{1.2}
\]

and a core `K`, using upper screens at transitions `{1,3,5,7}` and lower
screens elsewhere.  Denote the resulting old/new words by
`X(a,b|c;pi),Y(a,b|c;pi)`, where `pi=(g_1,...,g_d)`.

For a word `W`, let

\[
 {cal L}_q(W)=
   \sum_s {\bf e}_{W_s\cap W_{s+1}\cap\cdots\cap W_{s+q}}.
                                                               \tag{1.3}
\]

If `t=d+1-q`, define the prefix and suffix flag sets

\[
 P_t(\pi)=\{g_1,\ldots,g_t\},\qquad
 S_t(\pi)=\{g_{d-t+1},\ldots,g_d\}.                  \tag{1.4}
\]

The exact new-minus-old counter identity is

\[
\begin{aligned}
 \Delta_q(a,b\mid c;\pi)
 &= {\bf e}_{K\infty caP_t}-{\bf e}_{K\infty cbP_t}
   +{\bf e}_{K\infty cbS_t}-{\bf e}_{K\infty caS_t},\qquad
                                           2\le q\le d,         \tag{1.5}\\
 \Delta_1&=0.                                                   \tag{1.6}
\end{aligned}
\]

Here juxtaposition means disjoint union.  Formula (1.5) is the flag form
proved in `MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`;
it is also obtained directly from the two one-sided windows at the four
upper screens.  It is an equality of occurrence counters, not only support.

Every such packet has length `12d+35`, rank

\[
                              r=|K|+d+4,               \tag{1.7}
\]

and is exactly owner-, immediate-palette-, compressed-OR-deck-, residence-
and simple-topology-preserving.

## 2. The four twisted cube faces

Fix six distinct cube labels

\[
                  a_0,a_1,b_0,b_1,c_0,c_1             \tag{2.1}
\]

and an ordered neutral filler list

\[
                  M=(m_1,\ldots,m_{d-2});              \tag{2.2}
\]

for `d=2`, `M` is empty.  Let `M^rev` be the reverse order.  Use common
`K,infinity,delta`, but give packet `i` private labels

\[
                         e_i,\ell_i,r_i.               \tag{2.3}
\]

The four packet specifications are

```text
 i   ordered active pair   third role   internal filler flag

 0       a0 -> a1             c0        b0, M,      b1
 1       a1 -> a0             b0        c0, M,      c1
 2       a0 -> a1             b1        c0, rev(M), c1
 3       a1 -> a0             c1        b0, rev(M), b1.         (2.4)
```

The full filler order in row `i` is obtained by adjoining `ell_i` first and
`r_i` last.  All labels displayed in (2.1)--(2.3), the core, and the neutral
fillers are mutually disjoint.

## 3. Exact all-depth cubical cancellation

For `t=d+1-q`, put

\[
 A_t=\{m_1,\ldots,m_{t-1}\},\qquad
 B_t=\{m_{d-t},\ldots,m_{d-2}\}.                     \tag{3.1}
\]

Empty ranges are empty.  Reversing `M` interchanges `A_t,B_t`.  Write

\[
 E_{ijk}(R)={\bf e}_{K\cup\{\mathord\infty,a_i,b_j,c_k\}\cup R}.
                                                               \tag{3.2}
\]

### Theorem 3.1 (twisted-cube identity)

For every `2<=q<=d`, the four rows in (2.4) have deltas

\[
\begin{aligned}
 \Delta_q^0={}& E_{000}(A_t)-E_{100}(A_t)
                 +E_{110}(B_t)-E_{010}(B_t),\\
 \Delta_q^1={}& E_{100}(A_t)-E_{000}(A_t)
                 +E_{001}(B_t)-E_{101}(B_t),\\
 \Delta_q^2={}& E_{010}(B_t)-E_{110}(B_t)
                 +E_{111}(A_t)-E_{011}(A_t),\\
 \Delta_q^3={}& E_{101}(B_t)-E_{001}(B_t)
                 +E_{011}(A_t)-E_{111}(A_t).          \tag{3.3}
\end{aligned}
\]

Consequently

\[
                         \Delta_q^0+\Delta_q^1
                         +\Delta_q^2+\Delta_q^3=0      \tag{3.4}
\]

for every `1<=q<=d`.

#### Proof

Apply (1.5) to the first two forward flags.  In the last two flags, the
prefix neutral set is `B_t` and the suffix neutral set is `A_t`.  This gives
the four displayed rows.  Their eight pairs cancel vertically:

```text
 row0 prefix  <-> row1 prefix,
 row0 suffix  <-> row2 prefix,
 row1 suffix  <-> row3 prefix,
 row2 suffix  <-> row3 suffix.                         (3.5)
```

At depth one every row is zero by (1.6).  \(\square\)

This is an abelian four-face cubical identity, not a noncommutative group
commutator.  The four disjoint toggles commute; their nontrivial content is
that the signed lower-counter image of their product is zero while the
terminal literal word changes in four slots.

For `d>=4`, the reverse-neutral twist is essential to this displayed
uniform identity.  With all four neutral orders forward, (3.4) holds at the
two extreme depths but generally fails at the intermediate flag layers.

## 4. Mutual physical and palette compatibility

### Theorem 4.1

The four old owner sets in (2.4) are pairwise disjoint.  The same holds for
the new owner sets.  Moreover their complete lower-q1 palettes are pairwise
disjoint, and their adjacent-union supports are pairwise disjoint.

#### Proof

An owner inside a coatom block contains at least one private extreme filler
`ell_i,r_i`, and a lower-screen owner contains both.  Three of the four
upper screens contain private `e_i`.  The only upper owner without a private
label is the central one.  For rows `0,1,2,3`, its cube-label part is

```text
 a0 a1 b0 b1 c0,   a0 a1 b0 c0 c1,
 a0 a1 b1 c0 c1,   a0 a1 b0 b1 c1,                  (4.1)
```

respectively.  These are the four distinct five-subsets obtained by
omitting `c1,b1,b0,c0`.  Hence the owner banks are disjoint.

For adjacent intersections, every block-internal or lower-screen incident
colour contains a private extreme filler.  At an upper screen, all but two
boundary colours contain private `e_i`.  The two exceptional socket colours
in each row have the following cube-label parts, once for each
`alpha in {a0,a1}`:

```text
 row0: alpha b0 b1 c0     (missing c1),
 row1: alpha b0 c0 c1     (missing b1),
 row2: alpha b1 c0 c1     (missing b0),
 row3: alpha b0 b1 c1     (missing c0).               (4.2)
```

They are eight distinct sets.  Thus the complete lower-q1 palettes are
mutually disjoint.

Finally, an adjacent union inside a block or at a lower screen contains the
full private filler pair.  At an upper-screen boundary it contains at least
the left or the right private extreme.  Hence adjacent-union supports from
different rows are disjoint.  \(\square\)

Within each row, old and new owner sets and immediate palettes agree by the
authoritative mixed-screen theorem.  The union of the four rows is therefore
a literal simple, lower-rainbow-compatible U1 bank, rather than merely a
formal signed cancellation.

The exact combined ledger is

\[
\begin{array}{c|c}
\text{resource}&\text{number of distinct values}\ \hline
\text{owners}&4(12d+35)=48d+140\\
\text{adjacent intersections}&4(12d+34)=48d+136\\
\text{adjacent-union support}&4\cdot20=80.
\end{array}                                                     \tag{4.3}
\]

The complete construction uses

\[
 |K|+2+6+(d-2)+4\cdot3=r+14                       \tag{4.4}
\]

coordinates.  It fits in a `2r`-coordinate middle-layer ground whenever

\[
                         r\ge\max\{d+4,14\}.           \tag{4.5}
\]

## 5. Serial replacement theorem

### Theorem 5.1 (prepared-slot rainbow absorber)

Let a simple U1--U4-valid carrier contain four disjoint intervals equal to
the old packet words (2.4), with no exterior immediate-palette collision.
Replace them, in any order, by their new phases.  Then every intermediate
word is U1--U4-valid, has the same owner set as the initial carrier, and has
the same exterior attachment and clipped residence state.  The terminal
word also satisfies

\[
                   {\cal L}_q(W_{final})
                    ={\cal L}_q(W_{initial})
                    \qquad(1\le q\le d).              \tag{5.1}
\]

#### Proof

Each local replacement has common endpoints, owner set, immediate palettes,
prefix/suffix OR signatures, internal OR support deck and clipped residence
state.  The owner and palette disjointness from Theorem 4.1 makes the four
local moves mutually compatible.  The initial global validity assumption
excludes exterior collisions, so validity persists in any serial order.

A depth-`q` window crossing one of the four slot boundaries is unchanged,
because the first and last `d+2` literal block owners agree in the two
phases while `q+1<=d+1`.  All changed windows are therefore internal to one
slot.  Their summed counter delta is (3.4), proving (5.1).  \(\square\)

The construction is replacement-only: its four `Theta(d)` words occupy
prepared slots and do not add `Theta(d)` letters.  Its exterior boundary is
the constant set of eight common slot endpoints.

## 6. Why the shorter triangle is insufficient

With one common internal flag and third role `c`, the algebraic triangle

\[
                   (x,y\mid c),(y,z\mid c),(z,x\mid c)\tag{6.1}
\]

does telescope at every depth.  However its packet pairs repeat exactly the
three lower-q1 socket colours

\[
 K\mathord\infty cxF,\qquad
 K\mathord\infty cyF,\qquad
 K\mathord\infty czF.                                \tag{6.2}
\]

More generally, every nonempty closed walk in the fixed-flag pair-potential
graph revisits its flag vertices, and the corresponding q1 sockets repeat.
Thus fixed-flag telescoping alone is incompatible with a strict rainbow
bank.  The construction (2.4) avoids repeated vertices by exchanging which
cube axis is the active pair and which is the filler pair, with the neutral
reversal synchronizing all intermediate depths.

There is also a sharp two-packet obstruction **inside the nonzero canonical
mixed-coatom catalogue**.  At depth two, the union of the four masks in one
packet's signed support is exactly its central upper owner.  Two canonical
packet actions whose depth-two deltas cancel therefore share that owner,
even if their cores or filler presentations differ.  Hence such a
two-packet owner-disjoint cancellation is impossible.  These facts explain
why the twisted cube, not the shorter triangle or a canonical inverse pair,
is the useful physical identity.

They do not prove that some entirely different three-packet family is
impossible.  Indeed, in the bounded base depths there is a shorter exact
construction.  Keep one active pair `(a,b|c)` and take internal filler flags

```text
d=2: (x,y),       (y,z),       (z,x),
d=3: (x,m,y),     (y,m,z),     (z,m,x).               (6.3)
```

Their flag potentials telescope at every available nontrivial depth.  The
three full filler sets are distinct, so after private `e,ell,r` labels their
owners and q1 palettes are mutually disjoint.  At `d>=4`, the naive common-
middle extension of (6.3) fails at an intermediate prefix/suffix layer.

Inside the normalized common-base face,
`MATH_THEOREM_AD_NORMALIZED_COMMON_BASE_THREE_PACKET_RAINBOW_NO_GO_20260801.md`
handles the rectangle and diagonal Pluecker triangles.  Socket disjointness
eliminates the diagonal case and leaves at most one axis-transposed
rectangle.  The remaining all-depth equations force a middle filler word
of length `d-2` to equal its reversal, impossible for distinct labels when
`d>=4`.

This does **not** classify arbitrary-core Johnson-square triples: a shared
adjacent Johnson edge has several possible distinguished common labels at
higher rank.  Thus a different three-packet identity remains open even
inside the full canonical catalogue, as well as after enlarging the packet
family.

## 7. Compiler interface and exact remaining gate

The cancellation pairing (3.5) is independent of depth.  It transports the
two nested lower-chain occurrences between the same four packet pairs for
all `q=2,...,d`.  Thus an address-transparent placement needs only four
synchronized occurrence transports, not `Theta(d)` independent repairs.

If a permutation of compiler cells, fixing the exterior bank, maps the
**full labelled compiler feasibility structure** to its new counterpart,
then every old compiler matching transports verbatim.  Here the structure
includes target labels, cell capacities and deletion labels, interval-
survival/nonzeroness predicates, and all unchanged exterior assignments,
in addition to the paired occurrence edges (3.5).  This full-structure
isomorphism is an exact sufficient U5 criterion; an isomorphism of the bare
occurrence-cell graph need not be.

It is not automatic.  Equality (5.1) forgets word positions, deletion
labels, and interval-survival/nonzeroness constraints.  The exact remaining
gates are therefore:

1. planting the four old packet slots, with their private labels, in one
   safe carrier; and
2. proving the nonlinear compiler incidence transport or terminal Hall
   matching for the four paired chains.

The theorem closes local lattice cancellation, mutual owner
disjointness/compatibility, and mutual immediate-palette conflicts.  It does
not close arbitrary-carrier planting, U5, regeneration, or the full
additive-constant conjecture.

## 8. Independent replay

The dependency-free audit constructs the four literal packets for every
`2<=d<=12`.  It checks individual U1--U4, pairwise owner disjointness,
pairwise lower- and upper-q1 resource disjointness, and coefficientwise
counter cancellation at every depth.  It separately replays the three-
packet base exceptions (6.3):

```text
scratch/audit_ad_coatom_twisted_cube_rainbow_absorber_20260801.py
scratch/ad_coatom_twisted_cube_rainbow_absorber_20260801.audit.json
```

It reports

```text
PASS_AD_COATOM_TWISTED_CUBE_RAINBOW_ABSORBER
```

with canonical payload SHA-256

```text
07906857998c93f9947d56da5fbd1a7bcce07a629c060556d88efed3f7f04e3f
```

The normalized common-base obstruction has its own three-square audit:

```text
MATH_THEOREM_AD_NORMALIZED_COMMON_BASE_THREE_PACKET_RAINBOW_NO_GO_20260801.md
scratch/audit_ad_normalized_common_base_three_packet_rainbow_no_go_20260801.py
scratch/ad_normalized_common_base_three_packet_rainbow_no_go_20260801.audit.json
```

It reports `PASS_AD_NORMALIZED_COMMON_BASE_THREE_PACKET_RAINBOW_NO_GO`, explicitly marks
the arbitrary-core classification `UNPROVED`, and has payload SHA-256

```text
1b635e2fd0a7f245b4bbbdb0a0730493782641a998bd0a27e67c8b8901a2b9db
```
