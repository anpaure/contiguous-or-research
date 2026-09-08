# MNW mirror wrappers move genuine canonical q2 holes

**Date:** 2026-08-07  
**Method:** exact MSW path recursion, shore reversal, and the canonical q2
inverse test; no computation or search  
**Status:** unconditional local theorem.  The suffix-only no-support result
does **not** extend to the full MNW language.  The mirror wrappers of the
patterns beta and gamma each introduce one target absent from the canonical
q2 support.  Their signed currents also delete old targets, so they are hole
transporters rather than complete coverage-preserving repairs.

## 1. Shore reversal converts coturns into q2 turns

On one canonical MSW incidence path, let an internal upper vertex `U` have
lower neighbours `X^-` and `X^+`.  Define its coturn

\[
                         \Lambda(U)=X^-\cap X^+ .       \tag{1.1}
\]

For a base flipping tuple `phi`, let `partial^vee_2 phi` be the signed
change in these coturn values at all changed upper vertices.

For a bitstring `A` put

\[
                  F(A):=1\,\operatorname{revcomp}(A)\,1. \tag{1.2}
\]

The MNW mirror closure sends a tuple `phi` on `D_m` to

\[
                         1\,\operatorname{revcomp}(\phi)\,0
                                                               \tag{1.3}
\]

on `D_(m+1)`.  The published path recursion inserts, between the two new
endpoint edges, the old path under the map `F`.  This map swaps the two
incidence shores: an old lower vertex becomes a new upper vertex and an old
upper vertex becomes a new lower vertex.

### Lemma 1.1 (wrapper current identity)

For every base tuple `phi`,

\[
 \boxed{
 \partial_2\bigl(1\operatorname{revcomp}(\phi)0\bigr)
       =F_*\bigl(\partial^\vee_2\phi\bigr).}           \tag{1.4}
\]

#### Proof

At an old upper centre `U`, the two adjacent lower vertices `X^-,X^+`
become two new upper facets `F(X^-),F(X^+)` adjacent to the new lower centre
`F(U)`.  Their union is

\[
 F(X^-)\cup F(X^+)
 =1\operatorname{revcomp}(X^-\cap X^+)1
 =F(\Lambda(U)).
\]

The same identity holds before and after the flip and preserves the signed
multiplicity.  Summing over the changed centres proves (1.4). \(\square\)

This is the reason that appending a Dyck suffix and mirror-wrapping have
different q2 behaviour.  Suffixing preserves the ordinary union turns;
mirror-wrapping exposes the coturns.

## 2. Exact coturn currents of the four base patterns

Reading the other canonical lower neighbour at each upper endpoint of a
removed flipping-cycle edge gives

\[
\begin{array}{c|l}
\text{pattern}&\partial^\vee_2\\ \hline
\alpha(\varnothing)
 &[000110]+[100001]-[000101]-[100010],\\
\beta
 &[001001]+[010010]-[010001]-[001010],\\
\gamma
 &[10010100]+[10001001]-[10001100]-[10010001],\\
\delta
 &[000011]+[011000]-[010001]-[001010].
\end{array}                                                   \tag{2.1}
\]

For example, the three beta upper centres are `111001`, `011011`, and
`111010`.  Their unchanged lower neighbours are respectively `101001`,
`010011`, and `101010`.  The three coturn changes are

\[
\begin{aligned}
101000&\longmapsto001001,\\
010001&\longmapsto010010,\\
001010&\longmapsto101000.
\end{aligned}
\]

The value `101000` cancels, yielding the beta row of (2.1).  The other
rows follow from the same literal three- or four-edge ledger.

Applying (1.4) gives the wrapper q2 currents

\[
\begin{array}{c|l}
\text{wrapper}&\partial_2\\ \hline
1\operatorname{revcomp}(\alpha)0
 &[11001111]+[10111101]-[10101111]-[11011101],\\
1\operatorname{revcomp}(\beta)0
 &[10110111]+[11011011]-[10111011]-[11010111],\\
1\operatorname{revcomp}(\gamma)0
 &[1110101101]+[1011011101]-[1110011101]-[1011101101],\\
1\operatorname{revcomp}(\delta)0
 &[10011111]+[11110011]-[10111011]-[11010111].
\end{array}                                                   \tag{2.2}
\]

## 3. Exactly two wrapper types have a novel positive term

The positive coturns in the alpha and delta rows, and `010010` in the beta
row, are already canonical coturns.  Literal witnesses are

\[
\begin{array}{c|c}
\text{coturn}&\text{canonical upper centre and its lower neighbours}\\ \hline
000110&101110:\ 100110,001110,\\
100001&101101:\ 101001,100101,\\
010010&011110:\ 011010,010110,\\
000011&101011:\ 100011,001011,\\
011000&011101:\ 011100,011001.
\end{array}                                                   \tag{3.1}
\]

By the wrapper identity, their `F`-images are already canonical q2 turns
in the next dimension.

The remaining beta gain is

\[
                         H_\beta=10110111.             \tag{3.2}
\]

It is absent from the canonical semilength-four q2 image.  In its height
walk, the last down-step from height two is position five.  Every admissible
`p` before it is separated from either possible `q` by that forbidden
down-step.  The only later admissible `p` is position six.  It has two
height-zero up-steps to its left, whereas the two possible `q` positions
have respectively one and zero height-three up-steps to their right.  The
ordinal equality in the exact inverse test therefore never holds.

The other beta gain `11011011` is canonical: positions four and five form
an inverse witness, with ordinal counts one and one.

For gamma, the two gains are

\[
 H_\gamma=1110101101,
 \qquad G_\gamma=1011011101.                          \tag{3.3}
\]

For `H_gamma`, the only candidate `p` positions are one and two.  The only
candidate `q` not separated from them by a down-step starting at height two
or three is position three.  Its right ordinal count is two, whereas the
left counts are zero and one.  Thus `H_gamma` is canonically absent.

For `G_gamma`, positions six and seven form a valid inverse pair: both
ordinal counts are two and the positions are consecutive.  Hence
`G_gamma` is canonically present.

We have proved:

### Theorem 3.1 (mirror-wrapper hole mobility)

The mirror-wrapped beta tuple introduces the canonically missing q2 target
`H_beta`, and the mirror-wrapped gamma tuple introduces the canonically
missing q2 target `H_gamma`.  The mirror-wrapped alpha and delta tuples
introduce no target outside canonical q2 support.

In particular, the suffix-only single-tuple no-support theorem cannot be
extended to arbitrary MNW contexts.

## 4. Dyck-suffix repair cylinders

Let `v` be any Dyck word.  Appending `v` to every root and every flipping
cycle vertex appends it to every term of (2.2).  Each prefix in (2.2) ends
at height four.  Read from height four, a Dyck suffix contributes no
eligible inverse-test position at starting height zero, one, two, or three.
Therefore canonical presence or absence of every displayed prefix is
unchanged after suffixing.

Consequently

\[
 \boxed{H_\beta v=10110111v,
        \qquad H_\gamma v=1110101101v}                \tag{4.1}
\]

are missing canonical targets introduced respectively by

\[
 (1\operatorname{revcomp}(\beta)0)v,
 \qquad (1\operatorname{revcomp}(\gamma)0)v.          \tag{4.2}
\]

For fixed total semilength, distinct suffixes give disjoint tuple supports
and distinct missing targets.  Thus the full MNW language contains two
explicit Catalan cylinders of genuine q2 support mobility.

## 5. Why this is not yet a q2-complete Hamiltonization

The beta and gamma currents in (2.2) also have two negative terms.  In the
beta case both negative targets have canonical multiplicity one (their
unique inverse witnesses are `(3,5)` for `10111011` and `(6,7)` for
`11010111`).  A lone beta wrapper therefore fills `H_beta` but opens two
other holes.  It is a hole transporter, not a coverage-preserving repair.

To turn the mobility theorem into an upper-q2-complete rethreading one
still needs either

1. a signed relay whose negative terms terminate at redundant providers;
2. compound centres where two incident tuple changes interact; or
3. a correlated spanning hypertree whose total current has no unit-load
   negative term.

The local support obstruction is nevertheless removed: missing q2 targets
are reachable by isolated tuples already present in the MNW language.
