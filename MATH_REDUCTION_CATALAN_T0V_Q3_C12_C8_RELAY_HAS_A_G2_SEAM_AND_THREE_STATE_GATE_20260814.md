# The first native `q3` relay closes at the base but exposes a `G2` suffix seam and a three-state phase gate

**Date:** 2026-08-14
**Status:** unconditional for the literal semilength-six packet, its typed
currents through `q3`, the displayed all-suffix current identity and
eight-to-one component action, and the explicit `m=9,10` counterexamples.
The finite minimality statements are only for the enumerated native-cycle
menus stated below.  No all-width `q3` repair or resident three-state
dilation is claimed.

## 0. Result

Start with the frozen mixed `C8+C6` packet of
`MATH_THEOREM_CATALAN_T0V_MIXED_C8_C6_TYPED_SAFE_RESIDENT_Q2_TENSOR_AND_Q3_GATE_20260814.md`.
Its sole base span-four casualty is

```text
                         W3 = 110111001111.
```

The canonical base load of `W3` is one.  Its unique provider is the
four-owner interval at positions `1,2,3,4` of the root

```text
110110011000:

owners   110110001001  110110000101  110010000111  110001000111
colours     110110001101  110110000111  110011000111.
```

The mixed packet removes this occurrence.  Thus there is no untouched base
provider that can merely be retagged or rephased.

For every Dyck suffix through semilength four, the complete H100 factor
replay finds the same singleton pattern: `W3[V]` has old load one, its
provider lies at positions `1,...,4` of root `110110011000V` (possibly
read in the reverse path direction), and the frozen mixed packet leaves
new load zero.  This is an exact finite trace, not an asserted all-width
singleton theorem.

In the exact target-relevant single-cycle atlas, no owner-disjoint native
`C6`, `C8`, or `C10` both recreates `W3` and preserves every old typed
support through `q2`.  At `C12` there is exactly one such circuit.  It
restores `W3` but transports the singleton debt to

```text
                         H3 = 110101101111.
```

No owner-disjoint native `C6` closes this relay.  Among all owner-disjoint
native `C8`s, exactly one closes it.  The resulting

```text
                  frozen C8 + frozen C6 + C12 + C8
```

packet has 17 changed owners, 16 touched `q1` colours, 34 toggled
incidences, and no base support casualty on any typed deck through `q3`.
This is a positive **base** repair.

It is not the desired suffix-native resident repair.  Tensoring it over
Dyck suffixes has two exact obstructions.

1. Its old/new z-free owner-adjacency union contains a literal triangle.
   Hence the common binary phase used by the frozen `q<=2` tensor is
   impossible; the local fixed-bank phase alphabet needs at least three
   states.  The stronger directed unit-`Z3` potential also fails on the
   physical complementary closure: the old components have length 13 and
   the new affected component has length 104, neither divisible by three.
2. If `c0(V),c1(V)` are the first two canonical suffix colours and
   `G2(V)=c0(V) union c1(V)`, the boundary `q3` current contains

   ```text
   +000011110111[G2(V)] - 100011010111[G2(V)].
   ```

   The map `V -> G2(V)` is not injective.  Full-factor replay first loses
   support at suffix semilength three, for `V=110100`, and loses two rows
   at suffix semilength four.

Thus the smallest presently justified suffix-state refinement is to retain
an injective mark such as `c0(V)=g(V)` (or the ordered pair
`(c0(V),c1(V))`) in addition to the collapsed `G2` target, and the smallest
possible local z-free proper-colouring alphabet has size three.  It cannot
be fed directly to the existing `p`-tag cyclic-clock theorem, because the
directed closure voltage is inconsistent.  Constructing a resource-
disjoint package with this marked state and a genuine phase-reset/terminal
collar is the sharp remaining gate.

## 1. The two added circuits

### 1.1 The `C12` relay

In cyclic order its owners are

```text
110100000111
110000001111
110000101101
110100100101
110000100111
110001000111,
```

and its colours are

```text
110100001111
110000101111
110100101101
110100100111
110001100111
110101000111.
```

As usual, colour `i` is incident with owners `i` and `i+1` cyclically in
the alternating support.  One parity consists of old canonical incidences
and the other of absent incidences.  Toggling this support together with
the frozen mixed packet gives

```text
old load(W3) = 1,   new load(W3) = 2,
old load(H3) = 1,   new load(H3) = 0.
```

It is typed-support-safe through `q2`; `H3` is its only `q3` support
casualty.

### 1.2 The `C8` closer

Its cyclic owner and colour lists are

```text
owners:
110101000011
110100100011
110100001011
110100010011

colours:
110101100011
110100101011
110100011011
110101010011.
```

It is owner-disjoint from the preceding thirteen-owner packet.  The full
17-owner packet has sixteen distinct touched colours: the only shared
colour anywhere is the already-audited relay internal to the frozen
`C8+C6`.  Hence all four circuit supports are simultaneously literal and
owner-disjoint.

With the closer installed, `H3` returns to its old load one and `W3` has
load two.  The complete base currents have

```text
deck             positive values   negative values   casualties
owner                  0                  0                0
upper q1               0                  0                0
lower q2               0                  0                0
lower q1               8                  9                0
upper q2               6                  6                0
upper q3              12                  8                0.
```

These are numbers of distinct current values, not total variation.  In
particular one lower-`q1` positive has coefficient two, while the base
`q3` current contains coefficients `-2` and `-3`.  The certificate records
all old and new multiplicities literally.

The projected fixed-complementary lift has 125 components on both rank
shores, versus `Cat_6=132` before switching.  Replays through `m=10` give

```text
m        6      7       8       9        10
components
       125    422    1416    4827     16698
formula
 Cat_m - 7 Cat_(m-6) in every displayed case.
```

This finite topology replay is recorded because it shows that the local
`q3` closure does not undo the useful component action.  In fact the
component formula is symbolic.  At semilength six the unique affected new
closure component contains exactly the eight old Dyck roots

```text
110101101000   111100100010   111100001010   111100101000
110111010000   110101110000   110101011000   110110011000.
```

It has length `8*13=104`.  Canonical insertion/deletion orders concatenate
on a Dyck suffix, and every toggled incidence lies in the first twelve
coordinates.  Appending `V` therefore repeats the same endpoint splice on
the eight roots `R_iV`, producing one cycle of length `8(2m+1)`.  Distinct
suffixes give disjoint root sets.  Hence for every `m>=6` the new histogram
has

```text
Cat_m - 8 Cat_(m-6) cycles of length 2m+1,
Cat_(m-6) cycles of length 8(2m+1),
```

and therefore exactly `Cat_m-7 Cat_(m-6)` components on both projected
rank shores.

## 2. Exact scope of the native-cycle census

All searches begin with the frozen mixed packet and require disjoint owner
sets, preservation of the created `T0`, preservation of every old support
value on all typed decks through `q2`, and a path-factor replay before the
linear `q3` deck is read.

The exact single-cycle counts are

```text
cycle  enumerated/tested owner-disjoint  raw W3 creators  typed-q2-safe W3 creators
C6                804                          7                    0
C8               2208                         31                    0
C10              1757                        235                    0
C12             11789                       1578                    1
C14             86876                      12103                    0.
```

For `C6` and `C8` the first column is the complete native alternating
atlas.  For `C10`, `C12`, and `C14`, it is the complete target-relevant atlas:
every cycle contains a changed endpoint arc belonging to a possible
four-owner path with union `W3`.  Any single cycle creating `W3` must
contain such an arc, so this restriction loses no single-cycle creator.

The unique typed-`q2`-safe `C12` creator is Section 1.1, and its unique
`q3` casualty is `H3`.  After fixing that relay, all 792 owner-disjoint
native `C6`s give zero closers; among all 2,165 owner-disjoint native
`C8`s there is exactly one closer, Section 1.2.

Two auxiliary negative searches are deliberately stated more narrowly.
There is no typed-`q2`-safe pair consisting of one of the seven individually
raw-creating `C6`s and another owner-disjoint `C6` (5,561 pairs), and no
typed-`q2`-safe pair consisting of one of the 31 individually raw-creating
`C8`s and an owner-disjoint `C6` (24,641 pairs).  The exact shared-colour
CP-SAT model also rules out every owner-disjoint `C6` bank that contains
one of the seven individually raw-creating `C6`s.  These statements do not
exclude a jointly creating bank in which no member creates `W3` alone,
nor a longer, owner-reusing, or nonnative construction.

## 3. The full suffix current identity

Let `Delta3^0` be the base upper-`q3` current of the 17-owner packet.  For
a Dyck suffix `V` of semilength `s`, write `[V]` for adjoining its owner
up-set, and let

```text
c0(V) = g(V),
c1(V) = g(h(c0(V))),
G2(V) = c0(V) union c1(V).
```

The second and third lines are used only when `s>=2`.  A literal
prefix/suffix boundary-dart ledger gives the complete current

```text
Delta3(V) = Delta3^0[V] + S1(c0(V)) + S2(G2(V)),       (3.1)
```

where `S1=0` for `s=0`, `S2=0` for `s<=1`, and otherwise

```text
S1(c) =
 -111010010111[c]
 +101011010111[c]
 +000011110111[c]
 -100011011111[c]
 -000011111111[c],                                  (3.2)

S2(G) =
 +000011110111[G]
 -100011010111[G].                                  (3.3)
```

Equation (3.1) is an equality of occurrence-current multisets; equal target
words are aggregated.  Indeed, all toggled incidences lie in the fixed
twelve-coordinate prefix.  An affected three-colour window is therefore
either wholly in that prefix, crosses the seam in exactly one suffix
colour, or crosses it in exactly two suffix colours.  The wholly-prefix
windows give `Delta3^0[V]`; the finite boundary-dart ledger gives the five
one-colour rows `(3.2)` and the two-colour pair `(3.3)`.  A window using
three suffix colours is untouched.  This proves `(3.1)` for every suffix,
not just for the replayed widths.

The same locality argument on the decks through `q2` gives the base body
current plus the already-proved seam

```text
 +000011110111[c0(V)] - 100011010111[c0(V)].        (3.4)
```

All base negative values of the 17-owner packet retain support, and the
two uniform providers from the frozen theorem back the negative row in
`(3.4)`.  Consequently the 17-owner packet still gives an all-suffix,
owner/colour/incidence-disjoint, typed-support-safe tensor through `q2`.
The failure starts at `q3`.

The map `V -> c0(V)` is injective because `g^{-1}=h'`.  Thus the rows in
`(3.2)` are suffix-separated.  By contrast, taking a union forgets the
order and the map `V -> G2(V)` is not injective.

## 4. The first `G2` support failures

At suffix semilength three the exact quotient is

```text
V        G2(V)    suffix q2 load   old/full new load of 100011010111[G2]
111000   111101          2                         8 / 6
110100   110111          1                         1 / 0
110010   111110          2                         5 / 3
101100   111101          2                         8 / 6
101010   111110          2                         5 / 3.
```

The repeated rows have current `-2`, one contribution from each suffix in
the fibre.  The singleton fibre `V=110100` has only one old full-factor
provider, namely root `111100101000110100` at position eight.  The packet
removes it, giving the first support casualty

```text
                         100011010111110111.        (4.1)
```

At suffix semilength four the exact casualties are

```text
V          G2(V)      lost target
11010010   11011110   10001101011111011110
11010100   11010111   10001101011111010111.        (4.2)
```

There are no typed casualties through `q2` in these runs.  The
semilength-three and -four replays also show why a suffix `q2` load of one
is only a warning, not a sufficient casualty criterion: for example
`V=11011000` has suffix load one at `G2=11011101`, but the complete prefixed
target has old/new load `3/2`.

Noninjectivity of `G2` alone is not a proof of support loss; the literal
loads in `(4.1)--(4.2)` are.  What noninjectivity proves is that the
injective `g(V)` argument used at `q2` cannot certify the `q3` seam.
A suffix-local repair may still send several positive occurrences to one
collapsed target, but its owner, lower, colour, and cut resources must be
keyed by an injective mark.  Either

```text
                         (G2(V),c0(V))
```

or the ordered pair `(c0(V),c1(V))` suffices; in fact `c0(V)` alone
determines `V`.  No claim is made that this informational refinement by
itself supplies the required physical circuit.

## 5. The exact phase and directed-voltage obstructions

First let `G_union` be the z-free graph on owner vertices containing every
old and new selected owner adjacency.  Already at semilength six it
contains

```text
A = 110100000111,
B = 110100001101,
C = 110100100101
```

with edges

```text
A-B  new, through colour 110100001111,
B-C  old, through colour 110100101101,
C-A  new, through colour 110100100111.             (5.1)
```

Thus `A-B-C-A` is a triangle.  Appending any suffix owner up-set tensors
this same triangle into every suffix packet.  There is no common binary
phase map on the fixed bank.  Conversely an explicit proper three-colouring
of the complete z-free base union graph exists, so this local chromatic
number is exactly three.

That proper colouring is not the hypothesis of the `p`-tag cyclic-clock
theorem.  The latter requires a common directed potential

```text
                         t(w)=t(v)+1 mod 3            (5.2)
```

on every old and new physical closure edge.  The exact projected closure
histograms are

```text
old:  132 cycles of length 13,
new:  124 cycles of length 13 and one cycle of length 104.       (5.3)
```

Summing `(5.2)` around a directed component of length `L` requires
`L=0 mod 3`.  Already an unchanged old 13-cycle gives `0=13=1 mod 3`; the
new 104-cycle gives `0=104=2 mod 3`.  Reversing a whole component changes
the sign convention but not this divisibility condition.  Therefore the
directed `Z3` voltage system is **UNSAT in each state separately**, hence
also jointly.  No SAT search over component reversals can change the
verdict.

There is a quantitative reset lower bound even if unit increments are
relaxed to arbitrary proper `Z3` edge increments.  On an oriented cycle
let `b` be the number of `-1` rather than `+1` increments.  Closure gives

```text
                         L - 2b = 0 mod 3,
                         b = -L mod 3.               (5.4)
```

Thus a 13-cycle needs at least two non-unit/reset edges under its better
orientation, and a 104-cycle needs at least one.  The complete old and new
closures therefore need at least

```text
                         132*2 = 264,
                         124*2 + 1 = 249              (5.5)
```

non-unit phase edges respectively.  Even restricting to the affected
subsystem costs at least sixteen old reset edges on its eight 13-cycles
and at least one on the new 104-cycle.  Hence a single bounded global reset
is not an escape even at `m=6`.

At general semilength `m`, the corresponding native cycle length is
`L=2m+1` and the merged length is `8L`.  Whenever `L` is nonzero modulo
three, `(5.4)` forces at least one reset on every affected old cycle and
on the merged cycle, so tensoring over suffixes costs
`Omega(Cat_(m-6))` resets.  When `L=0 mod3`, this length congruence alone
is silent; a common-voltage test is still required.  Thus the proved
Catalan-scale lower bound holds on two residue classes of `m`, not on the
third.  An all-`m` repair must either carry suffix-local reset collars or
globally refactor the closure topology.

This is the sharp distinction: three colours suffice for the undirected
z-free conflict graph, but a cyclic three-tag clock does not close the
physical wreath.  A useful repair needs an explicit phase reset or
cut-open terminal collar and must check immediate-upper currents across
its reset seams.  Neither a binary relabelling nor the existing `p=3`
tag theorem applies verbatim.

## 6. Exact next interface

A suffix-native continuation must provide, for every required `V`, a
cut-open packet with state

```text
       (local phase in a set of size at least 3,
        injective suffix mark c0(V),
        collapsed target G2(V)).                  (6.1)
```

It must satisfy all of the following simultaneously.

1. Its positive upper-`q3` current covers
   `100011010111[G2(V)]`, with fibre multiplicity accounted for.
2. Its owners, incidences, lower resources, and exposed cuts are injective
   in `c0(V)` across suffixes.
3. Its other negative `q1`, `q2`, and `q3` rows have literal surviving
   providers after all packets are coinstantiated.
4. Its three-state phase-reset collar is resident at every new reset seam;
   it may not assume a closed unit-`Z3` potential.
5. After suppressing the packet, its component action is compatible with
   the desired contracted suffix topology.

The six-root thirteen-port hypothesis from the frozen `q<=2` theorem
remains unchanged and separate **for that six-root packet**.  Write
`B_V={R0V,...,R5V}` and give it one global sign `tau_V`; its six physical
roles then have relative signs

```text
                         tau_V * (-,+,-,+,-,+).
```

For every quotient edge one must still select a terminal role and one of
the thirteen starts so that: the complete signed source block survives the
packet cuts; the endpoint port data satisfy the common-history multiway
criterion at that start; coalesced requests have one literal word and
transitively consistent histories; distinct starts at a supernode are
separated by at least `d+1`; and the quotient selection is connected.

The added `C12+C8` relay is not topology-neutral: it enlarges the affected
block from six to eight roots and destroys the binary phase.  Therefore it
cannot be installed and then silently cite the preceding six-root
hypothesis.  A successful backup must either suppress topology-neutrally
back to the six-root interface, or prove a new eight-root/reset-state
thirteen-port hypothesis.  Neither the z-free three-colouring nor the
protected suffix stems proves either alternative.

## 7. Verification and exact open scope

All enumeration, factor replay, component computation, colouring,
provider tracing, and hashing were performed on H100.  The principal
verifiers are

```text
scratch/audit_msw_t0v_mixed_q3_loss_providers_20260814.py
scratch/search_msw_t0_mixed_q3_c6_backup_20260814.py
scratch/search_msw_t0_mixed_q3_c8_backup_20260814.py
scratch/search_msw_t0_mixed_q3_long_cycle_backup_20260814.py
scratch/search_msw_t0_mixed_q3_c12_relay_c6_closure_20260814.py
scratch/audit_msw_t0v_mixed_q3_closed_tensor_20260814.py.
```

Proved here:

* the unique base provider and impossibility of an untouched base retag;
* the exact finite single-cycle census through `C14`;
* the literal `C12` relay and unique native-`C8` closer;
* base typed-support safety through `q3`;
* all-suffix typed-support safety through `q2`;
* the all-suffix `q3` current identity `(3.1)`;
* the first literal suffix casualties `(4.1)--(4.2)`; and
* the exact local three-state lower bound `(5.1)` and the stronger closed
  directed-`Z3` no-go `(5.3)`.

Not proved here:

* that the displayed `C12+C8` addition is minimum among arbitrary
  multi-cycle, longer-cycle, owner-reusing, or nonnative banks;
* an all-width backup for `(3.3)`;
* a three-state phase-reset residence-dilation theorem;
* the contracted thirteen-port hypotheses.
