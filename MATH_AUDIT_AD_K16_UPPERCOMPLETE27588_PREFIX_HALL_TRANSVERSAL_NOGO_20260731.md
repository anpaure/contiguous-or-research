# K16 upper-complete carrier: exact lower-prefix Hall no-go at the maximizing schedule

**Date:** 2026-07-31  
**Lane:** AD  
**Status:** proved fixed-schedule no-go; no global K16 lower bound

## 1. Frozen scope and verdict

The target order is

```text
scratch/k16_facet_augmented_uppercomplete_capacity27597_targets_20260731.word
SHA-256 63aababe9d5cbaeec4ce68a1ec32edc02d249caf3750bb20f6bc87c1ca1eac43.
```

It is a permutation of all `C(16,8)=12870` middle masks.  Its carrier
intervals cover every upper target, and its adjacent rank-nine unions cover
all `C(16,9)=11440` upper-q1 colours.  Its exact three-hole P/Q dynamic
programme has maximizing schedule

```text
start holes     X = {5722,10950,10951},
deadline holes  Y = {10,12,13},
selected proper-prefix area = 27588.
```

This note proves that this fixed schedule cannot have a literal lower
compiler.  The obstruction occurs before simultaneous common-core coupling:
the complete necessary target-to-prefix incidence graph has maximum matching
only `24328`, versus `26332` required lower targets.  Its exact Hall gap is
`2004`.  In fact `1478` lower targets have no individually legal prefix at
all; one of them is the forced singleton `0x8000`.

The conclusion is only for the displayed P/Q schedule.  Other schedules for
the same carrier, other carrier orders, and global K16 equality remain open.

## 2. Maximal envelopes and the complete outer prefix set

Put `W=12870`, `L=W+3=12873`, and write the prescribed middle targets as

\[
T_0,\ldots,T_{W-1}.
\]

Let `p_i` and `q_i` be the increasing complements of `X` and `Y`, paired in
order.  Thus the representative middle interval is

\[
I_i=[p_i,q_i],\qquad 0\le q_i-p_i\le3.
\]

For every physical position `j`, define its maximal middle envelope

\[
E_j=\bigcap_{i:j\in I_i}T_i.                         \tag{2.1}
\]

For the frozen schedule every `E_j` is nonempty and

\[
\bigcup_{j\in I_i}E_j=T_i\qquad(0\le i<W).           \tag{2.2}
\]

Hence any literal word realizing these middle rows has letter
`A_j subseteq E_j`.

Let `C` be the following optimistic family of lower-prefix slots.

* At a selected start `p_i`, include
  \((p_i,\ell)\) for `1<=ell<=q_i-p_i`.
* At each of the three omitted starts in `X`, include all three slots
  \((x,1),(x,2),(x,3)\).

The first family has exactly

\[
\sum_i(q_i-p_i)=27588
\]

members, and the second deliberately grants the maximum nine omitted-start
slots.  Thus

\[
|C|=27597.                                           \tag{2.3}
\]

This is an outer family: an actual equality word may have fewer usable
omitted-start prefixes, never more.  Every lower mask has a witness of at
most three letters in the equality architecture.  If its witness begins at
a selected start, monotonicity forces it to end strictly before that start's
first middle deadline and hence to lie in the first family.  If it begins at
an omitted start, it lies in the granted second family.

## 3. Exact individual-pin incidence

For a slot `c=(a,ell)` write

\[
J_c=[a,a+\ell-1],\qquad
U_c=\bigcup_{j\in J_c}E_j.                            \tag{3.1}
\]

For a middle-row bit `b in T_i`, let

\[
H_{i,b}=\{j\in I_i:b\in E_j\}                       \tag{3.2}
\]

be its nonempty maximal-envelope host set.  Define the mandatory mask

\[
M_c=\{b:\text{some }i\text{ has }b\in T_i
                 \text{ and }H_{i,b}\subseteq J_c\}. \tag{3.3}
\]

For a nonempty mask `S` of rank below eight, put an edge `S~c` exactly when

\[
S\subseteq U_c,                                      \tag{3.4}
\]

\[
M_c\subseteq S,                                      \tag{3.5}
\]

and

\[
E_j\cap S\ne\varnothing\qquad(j\in J_c).            \tag{3.6}
\]

### Lemma 3.1 (individual pin iff)

There is a nonzero word which realizes all prescribed middle rows and whose
interval `J_c` has OR exactly `S`, while all other lower pins are ignored, if
and only if `S~c`.

### Proof

Suppose first that such a word exists.  Since every letter lies in its
maximal envelope, its OR `S` is contained in `U_c`, proving (3.4).  Each
letter on `J_c` is a nonzero subset of `S`, proving (3.6).  If
`H_(i,b) subseteq J_c` and `b` were absent from `S`, no position of row `i`
could carry `b`, contradicting the middle equation.  This proves (3.5).

Conversely, cap the maximal word by setting

\[
A_j=E_j\cap S\quad(j\in J_c),\qquad A_j=E_j\quad(j\notin J_c). \tag{3.7}
\]

Condition (3.6) makes every letter nonzero.  Equations (3.1) and (3.4) make
the OR on `J_c` exactly `S`: every bit of `S` occurs in some `E_j`, and the
cap removes every bit outside `S`.  A middle-row bit could disappear only if
all of its envelope hosts lay in `J_c` and the bit were absent from `S`,
which (3.5) forbids.  Thus every middle equation survives.  QED.

This lemma is why the graph is not a donor-width proxy.  Its edges are
exactly the individually realizable physical pins of the frozen maximal
envelope.

## 4. Hall is necessary before common-core coupling

### Theorem 4.1 (lower-prefix transversal condition)

If a literal word realizes the frozen middle schedule and covers every
nonempty lower mask, then the bipartite graph of Section 3 has a matching
covering all `26332` lower masks.

### Proof

Choose one short literal witness slot for every lower target.  Section 2
places every chosen slot in `C`.  Lemma 3.1 places the corresponding edge in
the graph.  Two different target masks cannot choose the same interval,
because one fixed physical interval has only one OR.  The chosen edges are
therefore an injection from the lower targets into `C`, hence a matching.
QED.

Simultaneous common-core constraints can only rule out combinations of these
individual edges.  They cannot create a missing edge or repair a Hall cut.
Consequently an outer-graph Hall failure is already a literal compiler
no-go; no common-cap SAT model is needed.

## 5. Exact K16 certificate

Two independent implementations reconstruct the same graph and give

```text
lower targets                         26332
optimistic proper-prefix slots        27597
incidences                           293968
zero-degree targets                    1478
zero-degree ranks             1^1 6^27 7^1450
maximum matching                      24328
Hall deficiency                        2004
DM Hall shore                    4029 / 2025
```

The DM shore itself is an exact Hall witness:

\[
|Z|=4029,\qquad |N(Z)|=2025,qquad |Z|-|N(Z)|=2004. \tag{5.1}
\]

The simplest local certificate is already a zero-degree row:

```text
S = 0x8000.
```

For every eligible prefix containing the `0x8000` bit, either some capped
cell would be zero or its mandatory mask contains a different bit.  Hence no
middle-preserving individual `0x8000` pin exists.  Since a nonzero OR equal
to a singleton consists entirely of that singleton, this rules out a
literal singleton witness in the fixed schedule.

The full Hall witness is stronger: even deleting the zero-degree rows leaves
a large shared-prefix collision obstruction.

## 6. Authentication and scope boundary

Frozen primary audit:

```text
scratch/audit_r_k16_uppercomplete27588_static_hall_20260731.py
  SHA-256 76d715f8a88ad0b2b20fc6dc0e0618b5f2cc7b03a60d9e8d9c3c90d18b21c4fa

scratch/r_k16_uppercomplete27588_static_hall_20260731.audit.json
  SHA-256 16cd05c55915c97754b29c43b04abc431f16b0b5bde19b90d0064e6d86ff9c08
  payload SHA-256 8ea08897d1bf8142eb9cf380ecb91c218ca295ec260d44eef037dd5b9aae7233
```

Independent C++ reconstruction:

```text
scratch/audit_r_k16_facet_uppercomplete_max_envelope_hall_20260731.cpp
  SHA-256 861e576526f808d6b4861813b0d7decb546394e15c4106c9d87a688fe677b920
```

The independent replay returns the same `27597`, `293968`, `1478`,
`24328`, and `4029/2025` figures.

This proves only:

> No literal universal length-12873 word has the frozen carrier order and
> the maximizing P/Q schedule `X={5722,10950,10951}`,
> `Y={10,12,13}`.

It does not prove that the carrier has no other feasible three-hole schedule.
The correct next exact model is therefore schedule-plus-transversal, not a
new upper-socket search: choose a realizable three-hole P/Q staircase with
area at least `26323`, require a perfect matching in its graph (3.4)--(3.6),
and only then impose the simultaneous capped-envelope equations.
