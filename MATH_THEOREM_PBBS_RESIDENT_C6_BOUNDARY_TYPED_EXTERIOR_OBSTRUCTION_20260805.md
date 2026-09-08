# Exact boundary transport and the two-sided exterior obstruction for a resident PBBS `C6`

**Date:** 2026-08-05  
**Method:** exact port-block interval calculus; no computation or search  
**Status:** unconditional local theorem.  A resident three-port fusion is
upper-monotone for a complete context transported with one side of the
seam, but it is not transparent to two independently fixed exterior sides.
The smallest orientation-cancelling double has no topology gain.

**Correction notice.**  This file supersedes the retracted draft with SHA
`b8d786557610064e2794bba839b9b03b7906afa3b4f084b9a8adb9def77cabce`.
That draft incorrectly treated a change of penetration as a target loss.
The opposite-extreme witness lies at the same head-transported seam and
does preserve every one-sided exterior OR.  The genuine obstruction below
uses two independently fixed sides.

## 1. Port paths and seam transport

Use the resident `q=3` notation with core `K`, fresh rail bank
`Y={y_1,...,y_d}`, active labels `a_0,a_1,a_2,c`, and deadline `d>=1`.
Put

\[
 C_i=K\cup Y\cup\{c,a_i,a_{i+1}\},
 \qquad
 D_i=K\cup Y\cup\{c,a_{i-1},a_i,a_{i+1}\}.
 \tag{1.1}
\]

Write the directed port path

\[
 V_i=(B_i=P_{i,0},P_{i,1},\ldots,P_{i,d},
             Q_{i,0},\ldots,Q_{i,d}=A_i).          \tag{1.2}
\]

In `H_2`, its closure seam is

\[
                         \beta_i:A_i\longrightarrow B_i. \tag{1.3}
\]

In `H_3`, the right/head endpoint `B_i` is reached from `A_(i+1)`:

\[
                         \beta_i^+:A_{i+1}\longrightarrow B_i. \tag{1.4}
\]

Thus `beta_i -> beta_i^+` is the natural boundary map when the complete
context attached to the head `B_i` moves with that head.

For `r,s>=1`, let `X_i(r,s)` be the last `r` owners of `V_i` followed by
the first `s` owners of `V_i`, across (1.3).  Let `X_i^+(r,s)` be the last
`r` owners of `V_(i+1)` followed by the first `s` owners of `V_i`, across
(1.4).

## 2. The exact one-sided positive theorem

### Theorem 2.1 (head-transported exterior monotonicity)

For every old crossing segment `X_i(r,s)` there is a segment at the
transported boundary `beta_i^+` with the same union.

More precisely:

1. if `r+s<=d+2`, then

   \[
                  \bigcup X_i(r,s)=\bigcup X_i^+(r,s); \tag{2.1}
   \]

2. if `r+s>=d+2`, then

   \[
                  \bigcup X_i(r,s)=C_i,             \tag{2.2}
   \]

   and the fixed opposite-extreme segment

   \[
     J_i=(A_{i+1},B_i=P_{i,0},P_{i,1},\ldots,P_{i,d},Q_{i,0})
        =X_i^+(1,d+2)                               \tag{2.3}
   \]

   also has union `C_i`.

Consequently, if an arbitrary complete exterior path `E_i` is transported
from `beta_i` to `beta_i^+`, every old interval which traverses `E_i` and
meets both adjacent port pieces has a new interval traversing the identical
occurrence of `E_i` with exactly the same OR.  The penetration lengths may
change, but no target value is lost.

#### Proof

For total width at most `d+2`, the rail profile depends only on `(r,s)`.
At the old seam the active union is `\{c,a_i,a_(i+1)\}`.  At the transported
new seam, the incoming owner belongs to port `i+1` and the outgoing owner
to port `i`, giving the same active union.  This is the port-shift identity
in the proof of the resident first-current theorem, and gives (2.1).

Every interval of width at least `d+2` on the old resident port is
saturated and has union `C_i`.  In (2.3), the incoming owner contributes
`c,a_(i+1)`, while the first `d+2` owners of `V_i` contribute all of
`K union Y` and `a_i,a_(i+1),c`.  Hence its union is `C_i`, proving (2.2).

Adjoining the same exterior OR to equal packet unions preserves equality.
The old and new segments meet the same transported boundary occurrence,
so the assertion is occurrence-level, not merely an untyped internal-deck
statement. `square`

The exceptional width-`d+3` calculation illustrates why penetration must
not be frozen.  The old segment

\[
 (P_{i,d},Q_{i,0},\ldots,A_i,B_i)=X_i(d+2,1)       \tag{2.4}
\]

has union `C_i`; the same penetration in the new phase has union `D_i`,
but (2.3) at the **same transported seam** restores `C_i` with penetration
`(1,d+2)`.

## 3. Two independently fixed sides do fail

Theorem 2.1 moves the boundary with the head.  It cannot simultaneously
keep the tail identity `A_i` fixed.  The following counterexample makes
that incompatibility literal while keeping the two exterior marker owners
Johnson-legal.

Choose fresh labels `p,q`, used nowhere else.  Insert

\[
 L_i=(K-\{x_d\})\cup\{c,a_i,p\}                  \tag{3.1}
\]

between `Q_(i,d-1)` and `A_i`, and insert

\[
 R_i=(K-\{x_1\})\cup\{a_i,a_{i+1},q\}            \tag{3.2}
\]

between `B_i` and `P_(i,1)`.  All four adjacent pairs are Johnson edges:
`L_i` is obtained from `Q_(i,d-1)` by `y_d -> p` and from `A_i` by
`x_d -> p`; `R_i` is obtained from `B_i` by `x_1 -> q` and from
`P_(i,1)` by `y_1 -> q`.

### Theorem 3.1 (two-marker exterior counterexample)

In the old port cycle, the four-owner interval

\[
                         L_i,A_i,B_i,R_i             \tag{3.3}
\]

has union

\[
 T_i=K\cup\{c,a_i,a_{i+1},p,q\}.                  \tag{3.4}
\]

After the fusion `H_2 -> H_3`, no interval in the displayed augmented
packet has union `T_i`.

Thus a single resident packet is not transparent to two independent
exterior sides, even though each side is represented by a rank-`r`
Johnson-legal owner.  The lost target has rank `r+3`.

#### Proof

The old direct edge `A_i -> B_i` makes (3.3) consecutive, and its union is
(3.4).  Since `p` occurs only in `L_i` and `q` only in `R_i`, every interval
with value `T_i` must contain both marker owners.

There are two directed arcs between the marker occurrences after fusion.
The arc internal to `V_i` is

\[
 R_i,P_{i,1},\ldots,P_{i,d},Q_{i,0},\ldots,Q_{i,d-1},L_i.
 \tag{3.5}
\]

It contains `y_1` (and also `y_d`; these coincide when `d=1`), whereas
`T_i` contains no member of `Y`.  Hence its union is not `T_i`.

The other arc begins

\[
 L_i,A_i,B_{i-1},\ldots
 \tag{3.6}
\]

and traverses the other two complete port paths before reaching
`B_i,R_i`.  It contains `a_(i-1)` and members of `Y`, neither of which is
in `T_i`.  Hence its union is also not `T_i`.

Any larger interval containing both marker owners contains one of these
two arcs and cannot remove its extra coordinate.  Therefore no new
interval has union (3.4). `square`

This is an upper/exterior theorem only.  The two marker owners certify that
even owner-legal boundary collars do not give arbitrary-context
transparency; no residence claim for the augmented collars is needed or
made.

## 4. Exact boundary criterion

For a replacement of directed fragments, record a boundary tuple

\[
              (\lambda,\rho,U),                   \tag{4.1}
\]

where `lambda` and `rho` are the named incoming and outgoing endpoint
occurrences touched by the segment and `U` is its packet union.  Penetration
length is deliberately omitted: Theorem 2.1 shows that it may change
without harming OR transport.

### Theorem 4.1 (private-context necessity on the resident seam)

A theorem which is to hold for all independently labelled two-sided
exteriors at a resident seam must preserve every tuple (4.1), up to its
explicitly declared endpoint/context bijection.

#### Proof

For the resident seam, (3.1)--(3.2) are owner-legal collars carrying two
fresh coordinate markers.  Every witness containing both markers must join
the two named endpoint occurrences.  An absent tuple then gives a target
casualty exactly as in Theorem 3.1. `square`

Internal cyclic support inclusion omits `lambda,rho` and therefore cannot
imply this condition.

## 5. The smallest double and its topology tradeoff

Consider two clean rethread sites on the same three components.  After
cutting both triples, the components are six arbitrary directed exterior
paths.  Let the two cyclic reconnections have orientations `sigma` and
`tau`, where each is one of the two nontrivial three-cycles.

### Theorem 5.1 (global orientation cancellation has no component gain)

1. If `sigma=tau`, the aligned double ear fuses the three old components
   into one, but Theorem 3.1 applies at either changed site and arbitrary
   two-sided exterior transparency fails.
2. If `tau=sigma^{-1}`, the **global monodromy** of the two boundary
   permutations cancels, but the six exterior paths close into three
   components rather than one.  Each local endpoint pairing is still
   changed, so independent two-sided contexts still fail Theorem 4.1.

Thus even the smallest two-packet compound which cancels the global
orientation has zero topology gain **and** does not, by itself, cancel the
local typed signatures.  A disjoint forward/reverse pair cannot help,
because independent private markers localize the casualty to one copy.

#### Proof

The component statements are the cut-path permutation calculation for the
aligned double ear: equal orientations advance the component index by a
generator of `Z_3`, while opposite orientations return each path pair to
its original index.  The upper statement follows from Theorem 3.1 at any
site whose endpoint pairing changes.  With independent markers, a target
lost at one site cannot be supplied by the other site. `square`

A correlated reflected double can evade the private-marker argument only
by cross-identifying and transporting the complete exterior contexts.  It
is the smallest algebraic candidate for a genuine boundary repair, but its
outer interface and topology must then be proved jointly.  That is a
protected-host hypothesis, not a context-free local identity.

### Theorem 5.2 (formal reflected-double cancellation)

Take two set-identical but occurrence-distinguished formal copies of the
resident bank and perform

\[
        H_0^-\sqcup H_2^+
          \longrightarrow
        H_1^-\sqcup H_3^+.                         \tag{5.1}
\]

Cross-identify their complete exterior contexts so that swap of the two
copies followed by reversal is an occurrence bijection.  Then (5.1)
preserves the complete occurrence-labelled interval-OR deck, including
every interval meeting either exterior context, at every width.

Its component count is

\[
                         1+3\longrightarrow3+1.    \tag{5.2}
\]

Hence this smallest formally transparent correlated double is exactly
topology-neutral.

#### Proof

The resident identities are

\[
                 H_0=\operatorname{rev}(H_3),
 \qquad          H_1=\operatorname{rev}(H_2).      \tag{5.3}
\]

Map the old `H_0^-` copy, together with its complete context, by reversal
to the new `H_3^+` copy.  Map the old `H_2^+` copy similarly to the new
`H_1^-` copy.  Reversal sends every directed interval occurrence to a
directed interval occurrence with the identical set union; the declared
cross-identification does the same for intervals entering the contexts.
The two maps are disjoint and exhaustive, proving the occurrence
bijection.  The component counts are those of the four resident states.
`square`

Theorem 5.2 is sharp in the following sense.  Removing the correlated
context identification returns the private-marker obstruction, while
retaining it supplies no decrease in the number of components.  A useful
global proof must therefore spend additional protected structure: it
cannot obtain both arbitrary-exterior transparency and Hamiltonization
from this two-copy algebra alone.

There is also a physical resource qualification.  Set-identical copies
repeat every middle owner and therefore cannot coexist in a simple central
owner factor.  Relabelling the second copy makes the owner resources
disjoint, but then (5.3) preserves interval values only up to that coordinate
relabeling, not as literal targets.  Thus Theorem 5.2 is an exact algebraic
cancellation certificate, not yet a plantable owner-simple double packet.

## 6. Consequence for the PBBS route

Full arbitrary-exterior transparency is therefore the wrong remaining
local target.  The proof-safe alternatives are:

1. rethread only at sites whose named upper witnesses are protected
   elsewhere;
2. preserve a fixed edge section containing one named witness for every
   upper target; or
3. build a genuinely correlated host which supplies the endpoint/context
   bijection excluded by Theorem 3.1.

The newly isolated all-unit soliton quiet path is disjoint from the fixed
gap section.  None of the present counterexample uses that component.
Hence any protected-section Hamiltonization should reserve the all-unit
path unchanged rather than spend it on a futile arbitrary-exterior double.

No `B(k)+O(1)` conclusion is claimed here.
