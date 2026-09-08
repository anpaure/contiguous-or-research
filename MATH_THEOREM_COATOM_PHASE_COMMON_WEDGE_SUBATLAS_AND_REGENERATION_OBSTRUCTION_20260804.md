# Coatom phase-common wedge subatlas and the sharp regeneration obstruction

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional extraction from the canonical mixed-coatom tensor.
It proves a quadratic prospective family of phase-common one-coordinate
turn wedges inside one fixed block.  It also proves that this family is not
a quadratic menu over a fixed incumbent and does not regenerate at the same
slot.  Product typing, common-socket privacy and global host planting remain
open.

## 0. Canonical planted atlas

Use the fixed-active common-boundary atlas with owner rank `r`, residence
depth `d>=2`, a rank-`r-2` frame `H`, fixed labels `e,h`, fixed ordered bank
`S`, and

\[
 R=H\setminus(\{e,h\}\cup S),
 \qquad q=|R|=r-d-2.
\tag{0.1}
\]

For every ordered pair of distinct labels `(u,v) in R^2`, put

\[
 F_{uv}=(g,S,u,v,h),
 \qquad
 K_{uv}=H\setminus(\{e,h,u,v\}\cup S).
\tag{0.2}
\]

Let `X(u,v)` and `Y(u,v)` be the old and new mixed-coatom words.  Their
twelve active block labels are, respectively,

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.
```

The active labels at block positions `1,4,5,12` are identical in `P` and
`Q`.  Fix one of those positions and call its common active set `V_*`.
The first position `Iab` is a canonical choice.

## 1. A quadratic family of literal phase-common turns

Inside the coatom block `B(V_*)`, the consecutive filler omissions `u,v`
give two consecutive rank-`r` owners.  Define

\[
 Z_*=(H\setminus\{e\})\cup\{g\}\cup V_*,
\tag{1.1}
\]

\[
 U_u=Z_*\setminus\{u\},
 \qquad
 U_v=Z_*\setminus\{v\},
 \qquad
 L_{uv}=Z_*\setminus\{u,v\}.
\tag{1.2}
\]

These identities follow from

\[
                         K_{uv}\cup F_{uv}
 =(H\setminus\{e\})\cup\{g\}.
\tag{1.3}
\]

### Theorem 1.1 (phase-common fixed-block wedge atlas)

For every ordered `u!=v`, both `X(u,v)` and `Y(u,v)` contain, at the same
two internal addresses of the fixed block, the literal Johnson turn

\[
 U_u\;--\;L_{uv}\;--\;U_v
\tag{1.4}
\]

with q1 union value `Z_*`.  The old and new phases agree pointwise on this
entire coatom block.

Consequently:

1. there are exactly `q(q-1)` directed phase-common turn certificates;
2. reversing `(u,v)` reverses the two owner roles but gives the same full
   wedge;
3. there are exactly `C(q,2)` distinct unoriented wedges and lower sources;
4. every wedge has terminal `Z_*`; and
5. the unordered wedge recovers `{u,v}` from `Z_*\L_(uv)`.

In particular, since `q=r-O(sqrt(r))` in the central regime, this is a
fixed-positive-density prospective wedge family.

#### Proof

The filler order in (0.2) places `u` and `v` consecutively.  In a coatom
block, the two corresponding owners are obtained by omitting `u` and then
`v` from the complete union `K_(uv) union F_(uv) union V_*`.  Equation
(1.3) identifies that complete union with `Z_*`, proving (1.2)--(1.4).

The selected active block is identical at the same block position in `P`
and `Q`; the filler order inside the block is unchanged by the active
rethread.  Hence the two owner occurrences and their intersection/union
cell are pointwise phase-common.

Swapping `(u,v)` swaps the two consecutive coatom addresses.  The lower
intersection and upper union depend only on the unordered pair.  Distinct
unordered pairs give distinct lower sets because their deleted pair is
`Z_*\L_(uv)`.  This proves every count.  \(\square\)

### Corollary 1.2 (what is already typed)

At the native one-coordinate owner/q1 level, the two containments

\[
 L_{uv}\subset U_u\subset Z_*,
 \qquad
 L_{uv}\subset U_v\subset Z_*
\]

are literal in both tensor phases.  Thus any terminal type depending only
on this native rank chain and the common block address is phase-stable on
the entire atlas.

This does not imply acceptance of a folded two-coordinate terminal type,
an external flag, or a private continuation beyond `Z_*`.

### Corollary 1.3 (native factor-completion and orientation stability)

Fix one candidate and protect its two incidences

\[
 L_{uv}--U_u,\qquad L_{uv}--U_v.
\tag{1.5}
\]

In every degree-compatible two-factor completion containing (1.5), those
two incidences exhaust the degree of `L_(uv)`.  Hence they are consecutive
at that lower occurrence and its literal q1 turn is necessarily

\[
                         U_u\cup U_v=Z_*.
\tag{1.6}
\]

Thus every candidate is individually stable under arbitrary completion of
the unprotected factor edges.  Both traversal orientations are available:
the directed options `(u,v)` and `(v,u)` use the same wedge and exchange its
two owner roles.  Consequently the atlas contains `q(q-1)` prospectively
oriented, completion-stable certificates for the native q1 terminal type.

This conclusion is occurrence-local.  It neither creates a second capacity
at `Z_*` nor certifies any external product type attached to either side.

## 2. Exact socket structure

The family in Theorem 1.1 is the complete graph on the `q` owner values

\[
                         \{Z_*\setminus\{u\}:u\in R\}.
\tag{2.1}
\]

Its edges are the full wedges, its edge intersection is the lower source,
and every edge union is the one common terminal `Z_*`.

Therefore one task may choose any one of `C(q,2)` wedges without an internal
socket conflict.  But two simultaneously required tasks which identify
their `Z_*` occurrences with one common unit capacity cannot both use this
subatlas.  Task-private physical slots, distinct terminal values, or an
explicit capacity split are necessary.

The obstruction is value-sensitive.  If equal values at distinct planted
block addresses remain distinct physical capacities, two task-private
slots do not collide merely because their Boolean terminal values agree.
If the common cap quotients by terminal value, they do.

## 3. Why this does not yet give the folded product ticket

The two canonical branches of one wedge share the same q1 occurrence
`Z_*`.  Two simultaneous occurrence-coordinate demands therefore meet a
unit cut at that terminal.  The full mixed-coatom packet preserves U1--U4,
but this one phase-common turn supplies only a native one-coordinate socket.

The folded-C8 terminal pair consists of two incomparable literal ray
targets.  A nested native Hasse chain cannot replace that pair while
preserving both target identities.  Hence Theorem 1.1 does not establish a
positive-density **product-typed** baseline.  One still needs one of:

1. two physically separate terminal occurrences with the correct two
   literal types;
2. the proved polarized stateful socket interface; or
3. a complete canonical tail which retains the two ray identities upstream
   and uses `Z_*` only as an allocated terminal socket.

The known opposed three-packet triangle has an additional exact warning:
its lower-q1 socket palette repeats three colours, each twice.  The local
phase-common block extraction does not remove that internal conflict.

## 4. Fixed-incumbent and same-slot regeneration no-go

### Theorem 4.1 (fibre one remains sharp)

For a fixed literal old word, at most one ordered pair `(u,v)` from the
atlas is available.  After applying that packet, the new word `Y(u,v)` is
not an old word `X(u',v')` of any different atlas option.  Thus the same
slot exposes no forward quadratic menu; its canonical available move is the
inverse toggle back to `X(u,v)`.

#### Proof

The fixed-incumbent theorem reconstructs the ordered filler pair from the
literal coatom addresses, proving the first statement.

For the second, a literal word reconstructs not only the filler pair but
also the ordered active-block sequence.  Every `X(u',v')` has active
sequence `P`, whereas `Y(u,v)` has the distinct sequence `Q`.  Hence no
equality is possible.  The authenticated tensor move is an involution, so
the same parameter pair supplies the inverse transition.  \(\square\)

### Consequence

The `q(q-1)` count is a prospective joint host/packet choice.  It can seed a
positive-density typed baseline only if the old slots are planted jointly
with the candidate parameters.  It cannot be used as a post-hoc repair menu
around one fixed chronology, and it cannot by itself satisfy regenerative
positive density at the same physical slot.

Regeneration therefore requires fresh task-private planted slots, transport
to a new common-boundary frame, or a separate serial mechanism whose new
phase is an old phase of the next packet.  The current tensor theorem proves
none of these.

## 5. Full-packet versus local-wedge planting

Theorem 1.1 extracts one local turn, but the U1--U4 guarantees belong to the
entire `12d+35`-owner mixed-coatom packet.  Protecting only the two wedge
incidences materializes the local turn and does not preserve the packet's
global owner current, residence, screens, or full interval-OR language.

A bounded bank of whole packets has `O(d)` protected support per packet and
fits the small protected-factor edge budget for a fixed number of tasks
when `d=O(sqrt(r))` and `r` is large.  A bank of `Theta(d)` whole packets
has `Theta(d^2)=Theta(r)` support with a template-dependent constant and is
not covered automatically by the `m-2` protected-edge theorem.

Thus the local quadratic wedge family closes neither full-packet planting
nor extensive regeneration.

## 6. Exact verdict on the positive-density premise

The existing atlas proves unconditionally:

\[
 \boxed{
 \text{quadratically many prospective, native one-coordinate,
 phase-common local wedge certificates}.}
\]

It does **not** yet prove:

\[
 \boxed{
 \text{a positive-density completion-stable product-typed and
 regenerating wedge baseline in one common cap state}.}
\]

The sharp missing rows are now explicit:

1. plant the candidate-dependent old packet jointly with the host;
2. make common anchors and the common `Z_*` socket task-private or
   capacity-faithfully shared;
3. resolve the folded two-coordinate terminal type and the opposed-triangle
   repeated q1 colours;
4. protect the whole-packet support in the global factor/topology; and
5. export a genuinely new quadratic atlas rather than the inverse move.

## 7. Dependencies

- `MATH_THEOREM_AD_COATOM_TENSOR_PLANTED_BOUNDARY_ATLAS_AND_FIXED_WORD_GATE_20260801.md`
- `MATH_THEOREM_H2_COATOM_TENSOR_FIXED_ACTIVE_MENU_AND_HOST_QUANTIFIER_20260801.md`
- `MATH_THEOREM_ALIGNED_BIRAIL_TELESCOPING_AND_PROSPECTIVE_FIXED_BANK_20260801.md`
- `MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`
- `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`
