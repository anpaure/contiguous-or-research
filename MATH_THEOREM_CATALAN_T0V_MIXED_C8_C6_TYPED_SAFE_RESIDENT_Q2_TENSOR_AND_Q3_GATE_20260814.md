# A mixed `C8+C6` gives a typed-safe Catalan `T0V` tensor and a resident `q<=2` phase lift

**Date:** 2026-08-14  
**Status:** unconditional for the literal canonical MSW incidence factor,
its owner/lower/upper typed decks through `q2`, the fixed complementary
lifted topology, and the internal phase-clock collar through three owner
blocks.  The later six-root contracted common-history fusion is stated as
an exact hypothesis, not claimed.  A unique span-four (`q3`) loss remains.

## 0. Result

Put

```text
T0 = 110011001111.
```

There is one literal owner-disjoint mixed packet in the canonical
semilength-six MSW incidence factor consisting of one alternating `C8` and
one alternating `C6`.  It has seven changed owners, six touched `q1`
colours, fourteen toggled incidences, and one colour shared as a relay
between the two circuits.  Its exact typed occurrence currents are

```text
owner       0
upper q1    0
lower q2    0
lower q1    four positive - four negative
upper q2    three positive - three negative.
```

Every negative lower-`q1` and upper-`q2` value has old canonical load two,
so the packet loses no old support and creates `T0`.

For every `m>=6` and every Dyck suffix `V` of semilength `m-6`, append the
up-set `U(V)` to every owner and colour in the packet.  The resulting
packets are literal, pairwise resource-disjoint, and simultaneous.  For
nonempty `V` the formerly terminal `C6` owner has one untouched suffix-side
colour, producing one additional seam current

```text
 + 000011110111[g(V)] - 100011010111[g(V)],
```

where `g(V)` is the first canonical MSW colour of `V`.  The negative seam
value always has at least two old providers.  Hence the complete tensor is
typed-support-safe through `q2` for every `m`.

For each `V`, the packet merges six native lifted MSW wreath cycles into
one.  Applying every suffix packet changes the component count from

```text
Cat_m  to  Cat_m - 5 Cat_(m-6).
```

The union of the old and new owner-adjacency banks is bipartite.  In the
actual fixed-complementary-closure orientation, the six native roots have
the fixed sign vector

```text
(-,+,-,+,-,+)
```

up to simultaneous reversal.  The binary phase clock gives arbitrary
owner residence depth `h` and transports every internal interval meeting at
most three base owner blocks.  Thus the packet has an all-`h` internal
resident lift through immediate upper `q2`.

This is sharp for the displayed phase lift.  Exactly one old span-four
base value has no new mate:

```text
110111001111.
```

At clock depth `h` it produces exactly `2h+1` lost lifted fibres.  This is a
`q3` gate, not a defect in the proved `q<=2` tensor.

## 1. The two literal alternating circuits

### 1.1 The `C8`

In cyclic order put

```text
O0 = 110011000101    Q0 = 110011000111
O1 = 110010000111    Q1 = 110010010111
O2 = 100010010111    Q2 = 100011010111
O3 = 100011010101    Q3 = 110011010101.
```

The old selected incidences are

```text
O0-Q3, O1-Q0, O2-Q1, O3-Q2,
```

and the new incidences are

```text
O0-Q0, O1-Q1, O2-Q2, O3-Q3.
```

Thus

```text
O0-Q0-O1-Q1-O2-Q2-O3-Q3-O0
```

is an alternating incidence `C8` with the displayed new edges on one
parity and the displayed old edges on the other.

### 1.2 The `C6`

Put

```text
K = 000011010110,       active coordinates = (1,7,12).
```

With the usual incidence-hex notation,

```text
A  = 100011010110       X = 100011110110
B  = 000011110110       Y = 000011110111
C  = 000011010111       Z = 100011010111.
```

The old selected incidences are

```text
A-X, B-Y, C-Z,
```

and the new incidences are

```text
B-X, C-Y, A-Z.
```

Consequently `A-X-B-Y-C-Z-A` is alternating.  The owner sets of the `C8`
and `C6` are disjoint, while

```text
                         Z = Q2
```

is their unique shared `q1` colour.  The two switches are therefore a
simultaneous owner-disjoint packet, with a genuine two-circuit colour
relay rather than a resource collision.

## 2. Exact base typed currents

The lower-`q1` current is

```text
positive                                        old load
000011100110                                        0
100010010110                                        0
100011010001                                        2
110001000101                                        1

negative                                        old load
000011110100                                        2
100011000110                                        2
110011000001                                        2
100000010111                                        2.
```

The upper-`q2` current is

```text
positive                                        old load
110110010111                                        2
101011010111                                        0
110011001111 = T0                                  0

negative                                        old load
110111000111                                        2
111010010111                                        2
000011111111                                        2.
```

Owners and upper-`q1` colours are preserved occurrence-for-occurrence by
alternation.  A direct intersection ledger at each changed owner gives
zero lower-`q2` current.  The displayed lower-`q1` rows are obtained by
intersecting the two selected owner endpoints of each changed colour; the
upper-`q2` rows are obtained by uniting the two selected colours at each
internal changed owner.  The independent full-factor replay gives exactly
the stated loads.  In particular, no negative row is a support casualty.

## 3. Literal suffix tensor and the seam current

Let `V` be a Dyck word of semilength `s=m-6`.  For every twelve-coordinate
mask `M`, write

```text
                         M[V] = M union U(V).
```

The canonical insertion and deletion orders concatenate on Dyck words.
Every selected prefix incidence in Section 1 therefore remains selected in
the canonical semilength-`m` factor after adjoining `V`; every unselected
prefix incidence remains unselected.  The two circuits remain alternating.

If `V!=V'`, suffix projection distinguishes `U(V)` from `U(V')`.  Hence
different packets have disjoint owner, colour, incidence, lower-`q1`,
lower-`q2`, and body upper-`q2` resources.  Within one packet there are
exactly seven owners, six colours and fourteen incidences.

Every current row in Section 2 tensors by `[V]`.  Each old negative base
provider also tensors literally, so all four lower and all three body-upper
negative values retain at least one provider.

There is one boundary correction when `s>0`.  The owner

```text
                         C[V] = 000011010111[V]
```

is a reverse endpoint at `s=0`, but is internal when the suffix path is
nonempty.  Let `g(V)` be the first canonical suffix colour.  Its untouched
suffix-side incidence contributes the exact additional current

```text
 + 000011110111[g(V)] - 100011010111[g(V)].       (3.1)
```

Here `[g(V)]` means that the rank-`s+1` suffix colour, rather than the
rank-`s` owner, is appended.

### Lemma 3.1 (two uniform providers of the seam debt)

For every nonempty Dyck `V`, the canonical upper-`q2` load of

```text
                         100011010111[g(V)]        (3.2)
```

is at least two.

#### Proof

Let `k(V)` be the down-step flipped up by `g`, and let `ell(V)` be the
up-step flipped down by `h` in the first canonical exchange

```text
                         V -> g(V) -> h(g(V)).
```

Apply the exact `Gamma` inverse criterion to the endpoint-four path in
`(3.2)`.  Since `V` is Dyck, `k(V)` is its first down-step from height one,
the first return of its first primitive component.  After that flip, every
later step of `g(V)` is two levels above the corresponding step of `V`.
If there are `r` up-steps from height one before `k(V)`, then `g(V)` has
exactly `r+1` such up-steps.  The `h` ordinal selects the last touching
up-step before `k(V)`; hence `ell(V)<k(V)` and exactly one height-one
up-step, namely `k(V)`, lies to its right.

Substitution of these facts and the fixed prefix heights into the four
conditions of the exact inverse criterion gives the two inverse pairs

```text
                         (1, 12+k(V)),
                         (11,12+ell(V)).            (3.3)
```

The two suffix coordinates differ because they are the two exchanged
coordinates of a Johnson edge.  Thus `(3.3)` gives two distinct canonical
turn occurrences of `(3.2)`.  One is the occurrence changed at `C[V]`; at
least the other survives.  This proves the lemma. `square`

The map `V -> g(V)` is injective because `g^{-1}=h'`.  Seam resources are
therefore pairwise distinct across suffixes.  Their twelve-coordinate
prefixes are different from every body-current prefix in Section 2, so no
body/seam collision is possible.  Combining the tensor providers and
Lemma 3.1 proves typed support safety for all `m`.

The exact upper-`q2` current per packet is therefore three positive and
three negative rows when `V` is empty, and four positive and four negative
rows when `V` is nonempty.

## 4. Exact component action

The six native root prefixes touched by one packet are

```text
R0 = 110101101000
R1 = 110110011000
R2 = 110111010000
R3 = 111100100010
R4 = 111100001010
R5 = 111100101000.
```

For suffix `V`, these are the six roots `Ri V`.  The fourteen-edge toggle
cuts their six distinct native lifted wreath cycles and reconnects all six
into one.  The endpoint replay gives one affected lifted component and no
split component.  Thus the component decrement is five.

The roots used for different suffixes are distinct, so component actions
are disjoint and add.  This proves

```text
                     components = Cat_m - 5 Cat_(m-6).        (4.1)
```

The same count is obtained independently on both projected rank shores of
the fixed odd complementary lift.

All toggled prefix colours lie among the first six canonical exchanges.
Consequently, if `h<=m-6`, the reverse depth-`h` suffix stem of every
affected native path is untouched.  These are literal protected path
terminals; they are not, by themselves, a proof of the later thirteen-port
source hypothesis.

## 5. Binary phase, residence, and the exact `q3` gate

Let the roots be ordered as `(R0,...,R5)`.  The union of all old and new
owner adjacencies is bipartite.  Choose a common phase map

```text
                         epsilon : owners -> {0,1}.
```

Alternating the rethreaded z-free paths with the fixed complementary
closure gives one affected lifted component.  Its physical traversal
orients the six old root rows with signs

```text
                         (-,+,-,+,-,+),             (5.1)
```

or the simultaneous reverse.  This is not an independently selected sign
pattern: the endpoint-closure replay derives it from the literal packet.

For clock depth `h>=2`, replace each owner of phase zero by

```text
D0,D1,...,Dh
```

and each owner of phase one by

```text
Dh,D(h+1),...,D(2h)=D0,
```

where `Dt` is the cyclic interval of `h` clock coordinates beginning at
`t` in `Z_(2h)`.  Join consecutive blocks at their common antipodal
anchor.  The phase-clock theorem gives positive and zero clock runs of
length at least `h` on every lifted trace.

The finite oriented certificate under `(5.1)` has:

```text
two-owner signatures:                 loss 0
stratified signatures of span <= 3:   loss 0
first stratified loss:                span 4 only.
```

For one or two met blocks, equality of the base owner union and ordered
phase word lets one reuse the same endpoint offsets.  For three met blocks,
the middle clock block is complete, so its clock union is all of `Z_(2h)`;
the immediate-upper support theorem of Sections 2--3 supplies a new
three-owner interval with the same base union.  Reusing endpoint offsets
gives the same lifted width and literal clock union.  Therefore every old
internal lifted interval meeting at most three base owners has a new mate
for every `h`.  This is the claimed resident `q<=2` lift.

The sole first loss is the old four-owner interval

```text
110110001001
110110000101
110010000111
110001000111
```

whose union is

```text
                         W3 = 110111001111.          (5.2)
```

No new base owner interval of any span has union `W3`.  A lifted interval
through these four blocks contains two complete middle clock blocks.  Its
clock union is therefore full, while its width depends only on the
difference of the two endpoint offsets.  That difference ranges from
`-h` to `h`, giving exactly

```text
                         2h+1                       (5.3)
```

lost lifted fibres.  The H100 replay gives losses `5,7,9,...,17` for
`h=2,...,8`, exactly as `(5.3)` predicts.

No claim is made here for intervals crossing the z-present return, the
final lifted closure, or the span-four value `(5.2)`.

## 6. Why the `C8` is a genuine minimum alphabet escape

There are 826 unoriented initially alternating native incidence `C6`
supports in the semilength-six canonical factor.  An exact CP-SAT model
selects an arbitrary owner-disjoint subset, allows shared `q1` colours, and
models the final two selected endpoints of every colour literally.  It
requires creation of `T0`, preservation of every old upper-`q2` value, and
preservation of every old lower-`q1` value.  The model is infeasible.

Thus no owner-disjoint simultaneous bank made only of initially
alternating native `C6`s solves the typed `T0` task, regardless of the
number of `C6` phases.  At least one longer circuit, an owner-reusing
sequential construction, or a nonnative context extension is necessary.

For the first longer alphabet, there are fourteen target-directed native
`C8` creators.  None is simultaneously upper-`q2`-safe and lower-`q1`-safe.
Among all 11,418 owner-disjoint pairs consisting of a target-directed `C8`
and an arbitrary native `C6`, exactly one pair is safe on every typed deck;
it is the packet of Section 1.  This is a finite exact minimality statement
inside the stated native owner-disjoint atlas, not a classification of
owner-reusing or nonnative circuits.

## 7. Exact six-root contracted thirteen-port hypothesis

The native thirteen-port theorem cannot simply be cited after `(4.1)`.
It is a theorem about one intact canonical tight row per native Dyck root.
One packet replaces six such rows by one component made of their path
segments and forces the relative sign vector `(5.1)`.

The precise sufficient interface for a later quotient fusion is as follows.
Contract each six-root block `B_V={R0V,...,R5V}`.  Give it one global sign
bit `tau_V`; terminal role `i` then has physical sign

```text
                         tau_V * (-,+,-,+,-,+)_i.   (7.1)
```

For every chosen quotient edge, select one terminal role at each endpoint
and one of the thirteen starts `a_t=t(d+1)`.  Require:

1. the complete length-`d` source block at that signed role survives as one
   literal contiguous occurrence after the packet cuts;
2. the two endpoint port data satisfy the common-history multiway
   union/intersection criterion at the same assigned start;
3. incidences coalesced at one supernode/start request one common literal
   word, and the generated history classes are transitively consistent;
4. distinct starts used at one supernode have cyclic distance at least
   `d+1`; and
5. the selected quotient graph is connected.

Under these five conditions, the coalesced multi-incidence Euler theorem
serializes the contracted components while preserving the strict-lower
deck in its stated range.

What is **not** proved is that the native thirteen candidates always contain
such a signed surviving role.  The native proof spends its entire
`13>12` pigeonhole margin on the parent edge's own bad set and assumes
intact canonical rows.  It neither absorbs a packet cut nor resolves the
mixed signs `(7.1)`.  This is the exact remaining common-history gate; the
protected reverse stems in Section 4 are candidate terminals, not a proof
of clauses 1--2.

## 8. H100 verification and scope

All enumeration, CP-SAT solving, full-factor reconstruction, component
replay, phase search, clock replay, and hashing were run on H100.  The main
verifiers are

```text
scratch/search_msw_t0_c8_typed_safe_20260814.py
scratch/solve_msw_t0_typed_safe_c6_bank_shared_colours_20260814.py
scratch/audit_msw_t0v_mixed_c8_c6_tensor_20260814.py
scratch/audit_msw_t0v_mixed_seam_providers_20260814.py
scratch/audit_msw_t0_mixed_c8_c6_phase_clock_20260814.py.
```

Complete-factor tensor replays at `m=6,7,8,9` give zero typed support
casualties and component counts exactly `(4.1)`.  The undilated factor has
minimum owner or immediate-upper run one, so dilation is genuinely needed.

Proved:

* a literal Catalan-indexed owner/colour/incidence-disjoint actuator bank;
* exact owner, lower-`q1`, upper-`q1`, lower-`q2`, and upper-`q2` currents;
* uniform body and seam backup providers;
* exact six-to-one component action for every suffix;
* a common binary phase and arbitrary internal residence depth;
* internal lifted support through three owner blocks (`q<=2`); and
* the first exact span-four loss and its `2h+1` clock multiplicity.

Not proved:

* a backup for the span-four value `110111001111[V]`;
* intervals crossing a module/exterior or fixed lifted-closure seam;
* clauses 1--2 of the contracted thirteen-port hypothesis;
* a final terminal opening cap; or
* complete proper-upper support beyond `q2`.
