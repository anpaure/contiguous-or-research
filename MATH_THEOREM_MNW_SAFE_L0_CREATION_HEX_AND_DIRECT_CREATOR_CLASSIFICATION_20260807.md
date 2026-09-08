# A support-safe hex closes the positive-H1 `L_0` relay

**Date:** 2026-08-07  
**Method:** exact touching-step phases and inverse-pair exhaustion; no
computation or search  
**Status:** unconditional literal local theorem in the state after the
gamma--alpha relay, the closed endpoint packet, positive `H0`, and the
unique `H1` phase-repair `C8`.  The face is disjoint from those supports,
creates the missing q2 target, and removes only redundant q2 occurrences.
Topology and widths at least three are separate.

## 1. Input hole

The unique `H1` phase-repair `C8` changes the selected pair at

\[
 O=1011000011
\]

from `\{2,6\}` to `\{6,7\}`.  Its negative turn is

\[
                         L_0=1111010011,             \tag{1.1}
\]

whose canonical inverse pair is uniquely `(2,6)`.  Hence `L_0` is absent
immediately after the `C8`.

## 2. A literal alternating creator

Put

\[
 Z=1010010011,\qquad K=Z-9=1010010001.              \tag{2.1}
\]

Use active labels `9,5,2`.  The lower owners are

\[
\begin{aligned}
 Z   &=K+9=1010010011,\\
 Z_5 &=K+5=1010110001,\\
 Z_2 &=K+2=1110010001,
\end{aligned}                                       \tag{2.2}
\]

and the upper colours are

\[
 K+59=1010110011,\quad
 K+25=1110110001,\quad
 K+29=1110010011.                                   \tag{2.3}
\]

The exact touching-step pairs are

\[
\begin{array}{c|c|c}
\text{owner}&\text{selected additions}&\text{cycle action}\\ \hline
Z   &\{4,5\}&5\longmapsto2,\\
Z_5 &\{2,4\}&2\longmapsto9,\\
Z_2 &\{8,9\}&9\longmapsto5.
\end{array}                                         \tag{2.4}
\]

Thus the six incidence statuses alternate.  Call the face `H_{L_0}`.
At its centre it retains addition four and changes the turn

\[
 1011110011\longmapsto1111010011=L_0.               \tag{2.5}
\]

## 3. Exact q2 current and multiplicities

The three turn changes are

\[
\begin{array}{c|c|c}
\text{owner}&\text{old turn}&\text{new turn}\\ \hline
Z   &1011110011&1111010011,\\
Z_5 &1111110001&1011110011,\\
Z_2 &1110010111&1110110101.
\end{array}                                         \tag{3.1}
\]

The intermediate term cancels, so

\[
 \boxed{
 \partial_2H_{L_0}
   =[1111010011]+[1110110101]
    -[1111110001]-[1110010111].}                    \tag{3.2}
\]

The two negative targets have the exact inverse-pair lists

\[
\begin{array}{c|c|c}
\text{target}&\text{inverse pairs}&\text{load}\\ \hline
1111110001&(1,10),(2,4)&2,\\
1110010111&(2,3),(8,9)&2.
\end{array}                                         \tag{3.3}
\]

The face removes respectively `(2,4)` and `(8,9)`, leaving `(1,10)` and
`(2,3)`.  Neither negative target occurs in the signed currents of the
gamma--alpha pair, the closed endpoint packet, positive `H0`, or the
repair `C8`.  Hence both still have load two just before `H_{L_0}`.
After (3.2), `L_0` is restored and every previously represented q2 target
remains represented.

## 4. Exact direct-creator classification

For a canonical centre `L_0-\{p,q\}`, a one-face creator requires exactly
one of additions `p,q` to be selected.  The complete touching-step list is

\[
\begin{array}{c|c|c}
\{p,q\}&\text{selected pair at the centre}&
 \text{alternating core labels}\\ \hline
\{1,6\}&\{6,7\}&\varnothing\\
\{1,9\}&\{8,9\}&\varnothing\\
\{1,10\}&\{1,8\}&\varnothing\\
\{2,4\}&\{4,5\}&6,9\\
\{2,9\}&\{2,8\}&\varnothing\\
\{3,6\}&\{6,7\}&2\\
\{3,9\}&\{8,9\}&\varnothing\\
\{4,6\}&\{6,7\}&\varnothing\\
\{4,9\}&\{8,9\}&\varnothing\\
\{6,9\}&\{8,9\}&\varnothing.
\end{array}                                         \tag{4.1}
\]

All other pairs have zero or two desired selected additions.  The
`\{3,6\}`, core-two face uses the original unique provider owner `O` as
an auxiliary owner; canonically its `L_0` gain cancels its `L_0` loss, and
after the repair `C8` it is no longer alternating.  The `\{2,4\}`, core-six
face has current

\[
 [L_0]+[1110101011]-[1111100011]-[1110011011],      \tag{4.2}
\]

and `1111100011` has the unique inverse pair `(2,4)`, so it is only a
one-hole relay.  The core-nine face is exactly (2.1)--(3.2) and is the
unique support-safe direct creator in this state.

In particular, the previously tempting centre `0111010010`, with pair
`\{1,10\}`, has no alternating completion.  At each possible core, one of
the two auxiliary phase tests fails; it must not be cited as a literal
creator.

## 5. Support separation and suffixing

The lower-owner set in (2.2) is disjoint from:

* the three mirror-gamma centres
  `1010001101,1011001001,1110001001`;
* the three `alpha(1100)` owners
  `1110000101,1110000110,1110100100`;
* the owners of `H_leaf`, `H_*`, positive `H0`, and the eight vertices of
  the `H1` repair `C8`.

Its six colours are disjoint from the selected incidences changed by those
moves.  Therefore (2.4) is still the canonical phase when the face is
used.

Appending a Dyck suffix preserves every touching-step test and every
inverse multiplicity in (3.3).  Distinct suffixes have disjoint supports.
Thus the entire suffix cylinder of `L_0` holes is closed simultaneously.

## 6. Remaining scope

This theorem closes the literal q1/q2 obstruction at positive `H1`.  It
does not assert the component permutation of the combined packet, its
membership in one MNW spanning hypertree, or preservation of q3 and wider
decks.  Positive `H2` and `H3` must be replayed in the resulting phase.
