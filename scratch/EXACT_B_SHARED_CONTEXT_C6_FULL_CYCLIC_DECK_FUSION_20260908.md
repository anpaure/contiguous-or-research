# Shared-context C6 fusion preserves every old cyclic interval width

Date: 2026-09-08. Status: proved restricted zero-length-cost fusion lemma.
No canonical PBBS planting, global regeneration, or safe linear opening is
asserted. This generalizes the whole-component resident hybrid calculation
to arbitrary common literal contexts; it does not remove that calculation's
arbitrary-exterior boundary.

## 1. Literal construction

Let a_0,a_1,a_2,c be distinct coordinates and read indices modulo three.
Put

\[
L_i=\{c,a_i\},\qquad R_i=\{a_{i-1},a_i\}.
\]

Let C and D be any two fixed finite words of nonempty set letters. Either
word may be empty. They can use arbitrary coordinates, including the four
displayed ones. The three copies below have the same literal values but
distinct occurrence identities. Put N=|C|+|D|+2.

Start with the three complete cyclic source words

\[
W_i=(L_i,C,R_{i+1},D),\qquad i\in\mathbb Z_3.
\tag{1}
\]

Cut each cycle immediately before its R screen and reconnect so that L_i,C
is followed by the complete path R_i,D,L_(i-1),C. This gives one cyclic word
of length 3N, which can be written

\[
V=(L_0,C,R_0,D,L_2,C,R_2,D,L_1,C,R_1,D).
\tag{2}
\]

No source occurrence is added or removed. The old-to-new port successor is
i -> i-1, so all three old components are fused into one.

There is a substantial restriction for an exact flat-owner application:
if all width-(d+1) owner values across the three old cycles must be distinct
rank-r sets, then necessarily |C|<=d and |D|<=d. Section 4.1 proves this.
Thus allowing long common contexts in the set-word theorem does not supply
long owner-once components for the exact construction.

## 2. All old interval rows transport exactly

For a cyclic word W and an integer w no greater than its period, let
M_w(W) be the multiset of OR labels of its intervals of width w, one
occurrence per cyclic start.

### Theorem 2.1

For every 1<=w<=N,

\[
\boxed{
M_w(V)=M_w(W_0)\uplus M_w(W_1)\uplus M_w(W_2).
}
\tag{3}
\]

This is exact occurrence-multiset equality at every old cyclic width,
including widths much greater than the source depth used by a compiler.

#### Proof

In both the old cycle bank and V, the screen gaps alternate between
|C|+1 and |D|+1. Equal screen types are distance N apart. Thus an interval
of width at most N contains at most two screen occurrences.

Classify intervals by their screen occurrences and their exact endpoints
inside the common contexts.

* An interval with no screen lies inside a C or D copy. Match these copies
  bijectively, retaining its offsets.
* An interval with one screen has the form suffix(D),L_i,prefix(C) or
  suffix(C),R_i,prefix(D), with either fringe possibly empty. Both banks
  have exactly one screen of each displayed type with precisely these
  common contexts. Match the same screen label and the same offsets.
* A two-screen interval in the R-to-L orientation has the form

      suffix(C), R_(i+1), D, L_i, prefix(C).

  That complete oriented arc occurs literally in V. Match it with identical
  offsets. The width restriction ensures that the two C fringes are
  consistent; their allowed lengths are identical in the two banks.
* A two-screen interval in the L-to-R orientation has old form

      suffix(D), L_i, C, R_(i+1), prefix(D).

  Match it to the interval with the same fringes and common C in V whose
  screens are L_(i+1),R_(i+1). Its OR is equal because

  \[
  L_i\cup R_{i+1}
   =\{c,a_i,a_{i+1}\}
   =L_{i+1}\cup R_{i+1}.
  \]

Each correspondence is bijective on its interval type and preserves width
and OR label. The types are disjoint and exhaust all intervals of width at
most N, proving (3). QED.

The argument permits empty contexts: the screen-based classification still
applies, with no intervals of a vanished context type.

## 3. Complete cyclic support changes by at most the full union

Write B for the union of all letters of C and D, and put

\[
\Omega=B\cup\{c,a_0,a_1,a_2\}.
\]

Let Deck(W) be the set of OR values of all nonempty cyclic intervals of
width at most one period. Then

\[
\boxed{
Deck(V)=Deck(W_0)\cup Deck(W_1)\cup Deck(W_2)\cup\{\Omega\}.
}
\tag{4}
\]

The inclusion from right to left follows from (3) and the full-period
interval of V. For the other inclusion, only intervals of width greater
than N need consideration. The C/D background and screen positions repeat
with spacing N, so such an interval contains every background position
type and therefore has background union B. It also contains at least two
consecutive screens.

The union of two consecutive screens contains c and two of the a labels.
Any larger consecutive screen block has either those same three labels or
all four labels. Hence the complete interval OR is either Omega or
B union {c,a_i,a_(i+1)} for some i. The latter is the full-period union of
old cycle W_i and is already in its deck. This proves (4).

## 4. Application and exact boundary

If the old sources have rank-r owner windows at some width d+1<=N, (3)
preserves their full owner multiplicity. It also preserves every shorter
source row and every old upper source row through width N. In particular,
an occurrence-labelled compiler using any old cyclic cells of width at
most N transports through the bijection with no extra letters.

For the resident clean-C6 hybrid, take C=(C_1,...,C_d) and
D=(C'_1,...,C'_d). The result reproduces its internal upper-support
inclusion and strengthens the explanation: the primed replacement algebra
is needed to make the owners resident and rank-correct, but the full cyclic
OR-deck preservation itself needs only the two shared literal contexts.
Arbitrarily long shared return contexts are allowed.

The shared-context condition applies to the **complete three cycles**.
An arbitrary body attached to one port can change its C or D context, and
then the interval correspondences in Section 2 need not preserve values.
This is exactly the mechanism exposed by the earlier private-prefix upper
counterexample. The lemma cannot be serially applied to an enlarged output
cycle without finding a new complete shared-context decomposition.

Likewise, the cyclic support theorem does not guarantee that appending only
d letters after a final linear cut preserves every long upper witness. A
safe opening remains a separate requirement.

Thus this is a concrete sufficient fusion rule, not an assertion that a
canonical PBBS factor contains enough such triples or that their outputs
regenerate. No all-dimensional equality claim follows.

### 4.1 The owner-uniqueness restriction rules out long whole components

Suppose d+1<=N, every width-(d+1) owner in the three old cycles has rank r,
and these owner labels are globally distinct. Then

\[
\boxed{|C|\le d,\qquad |D|\le d,\qquad N\le2d+2.}
\tag{5}
\]

If |C|>=d+1, take any consecutive d+1 letters entirely inside C. The same
literal word occurs in all three old components, so its rank-r union is
repeated three times in the owner row, contrary to distinctness. The same
argument applies to D. This proves (5). It is necessary, not sufficient for
owner uniqueness.

In particular, at k=17 and d=3 this template can only have old component
length N<=8. It therefore cannot fuse the intact canonical PBBS bad cycles
of length 51, nor the rigid mountain cycle of length 17, by treating those
cycles as the three complete old components in (1). Both lengths exceed
eight. More generally, the established PBBS coordinate-homomesy/divisibility
theorem makes each canonical step-two component length at least k in odd
dimension; whenever k>2d+2, no intact canonical component can fit (1) with
a globally nonrepeating middle owner row.

The resident hybrid construction avoids this contradiction because its
displayed short port cycles are prospective modules, not a claim that an
arbitrary long canonical PBBS component already equals that module. A
global use still has to replace or protect the exterior bodies, which is
the already-identified upper-deck problem. The bound (5) prevents treating
arbitrarily long shared contexts as a solution to that exact application.

## 5. Earlier sources and novelty

The source construction and special resident case are in

    MATH_THEOREM_PBBS_RESIDENT_C6_HYBRID_SOURCE_LOWER_TRANSPORT_AND_UPPER_MONOTONICITY_20260805.md

The arbitrary-exterior obstruction is in

    MATH_THEOREM_PBBS_CLEAN_C6_COMMON_HISTORY_ALL_LOWER_DEPTH_LIFT_AND_SHARP_UPPER_BOUNDARY_20260805.md

The canonical component-length input and the newly classified bad sector
are respectively in

    PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md
    scratch/PBBS_EXACT_THREE_RUN_COMPONENT_SECTOR_20260908.md

The new statement here isolates a stronger shared-context conclusion:
arbitrary common literal C,D, exact per-width occurrence-multiset transport
for all old widths, and the complete support identity (4). It is a
restricted extension of the known resident internal theorem, not a new
unrestricted PBBS fusion theorem. The proof is purely combinatorial; no
program was executed for it.
