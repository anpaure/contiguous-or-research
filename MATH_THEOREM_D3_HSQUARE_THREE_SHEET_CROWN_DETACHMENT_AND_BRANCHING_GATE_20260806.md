# The `D_3` H-square has an exact three-sheet owner colouring but no simple rail lift

**Date:** 2026-08-06  
**Method:** pure mathematics; crown-graph factorization and complete
rail-potential rigidity  
**Status:** unconditional sharp reduction.  Three sheets are exactly enough
to detach the multiplicity-three owner ledger **after splitting rows into
owner occurrences**.  No whole-row three-sheet packing exists, and no
capacity-one one-in/one-out rail transport can realize the required split.
Thus a physical detachment must contain a genuinely branched or stateful
profile adapter.  The native owner columns have arity three, but the note
does not exclude a composite built from auxiliary binary branches and does
not construct the final branched word.

## 1. The reduced H-square rows

Use the reduced four-for-four identity from
`MATH_THEOREM_D3_CONJUGATE_CURRENT_SQUARE_OWNER_MULTIPLICITY_OBSTRUCTION_20260806.md`.
Put

\[
\begin{aligned}
 E_0&=\{3,5\},&E_1&=\{3,4\},\\
 E_2&=\{2,4\},&E_3&=\{2,5\}.
\end{aligned}                                           \tag{1.1}
\]

The four owners containing the full common block `X` are `X+E_j`.
Relabel each residual row by the unique owner it omits.  Then the three
full-`X` owners in the negative row `R_i^-` occur in the order

\[
                         E_{i+1},E_{i+2},E_{i+3},       \tag{1.2}
\]

while those in the positive row `R_i^+` occur in the reverse order

\[
                         E_{i-1},E_{i-2},E_{i-3}.       \tag{1.3}
\]

All indices in this note are modulo four.  Equations (1.2)--(1.3) are the
literal active-pair tables

\[
\begin{array}{c|c|c}
i& R_i^-&R_i^+\\ \hline
0&E_1,E_2,E_3&E_3,E_2,E_1\\
1&E_2,E_3,E_0&E_0,E_3,E_2\\
2&E_3,E_0,E_1&E_1,E_0,E_3\\
3&E_0,E_1,E_2&E_2,E_1,E_0.
\end{array}                                             \tag{1.4}
\]

Thus the row--owner incidence graph on either shore is

\[
                              K_{4,4}-I,                \tag{1.5}
\]

with `R_i` nonincident only with `E_i`.  This is the exact source of the
owner multiplicity three.

## 2. Exact three-sheet occurrence detachment

Colour an incidence `R_i E_j`, with \(i\ne j\), by

\[
                 \kappa(i,j)=j-i\pmod4\in\{1,2,3\}.    \tag{2.1}
\]

### Theorem 2.1 (crown detachment)

The colouring (2.1) is a proper three-edge-colouring of `K_(4,4)-I`.
Every row uses each sheet once and every repeated owner uses each sheet
once.  It works on both shores of the H-square; along a negative row the
sheet order is `1,2,3`, and along a positive row it is `3,2,1`.

Consequently, at the occurrence-ledger level, replacing `X+E_j` by the
addressed owner `(X+E_j,kappa(i,j))` makes all twelve owners distinct on
each shore and gives exactly the same detached owner set on the two
shores.

#### Proof

For fixed `i`, the allowed values of `j-i` are precisely `1,2,3`; hence
the three incidences at row `R_i` have different colours.  For fixed `j`,
the incident rows are `i=j-1,j-2,j-3`, again giving the three colours.
This proves properness and both one-copy assertions.  The order statements
follow immediately from (1.2)--(1.3). \(\square\)

Three is minimal at this abstract level, since every vertex in (1.5) has
degree three.

## 3. Whole rows require four sheets

### Proposition 3.1 (no whole-row three-sheet packing)

If a sheet carries whole residual rows with one fixed owner profile per
row, no two of the four rows on one shore can occupy the same sheet.
Therefore a whole-row detachment needs at least four sheets.

#### Proof

Rows `R_i` and `R_j`, with \(i\ne j\), are both incident with the two owner
types outside `{E_i,E_j}`.  With one common sheet/profile, those two
central owners collide.  Thus all four rows require different sheets.
\(\square\)

This lower bound is stronger than the maximum owner multiplicity: although
each owner occurs only three times, the row-intersection graph is `K_4`.
The three-sheet optimum of Theorem 2.1 is available only after every row is
split among its three owner occurrences.

## 4. Rail-potential rigidity forces branching

Let a sheet/profile be represented by ordered banks `(X_s,Y_s)`.  At an
active label `z`, a capacity-one complete-current seam from profile `s` to
profile `t` requires literal equality

\[
                         F_{X_s,Y_s}(z)=F_{X_t,Y_t}(z). \tag{4.1}
\]

For semilength at least four, the complete rail-potential rigidity theorem
recovers both ordered banks from either side of (4.1).  Hence

\[
                         (X_s,Y_s)=(X_t,Y_t).          \tag{4.2}
\]

### Theorem 4.1 (no simple three-sheet rail cover)

The occurrence detachment of Theorem 2.1 cannot be lifted by a network in
which every active-label current has one incoming and one outgoing rail
potential.  Any physical three-sheet lift must use a branched current
identity, an extra absorbing row, or a nonzero intermediate current.

#### Proof

Along every row, Theorem 2.1 assigns three different sheets to the three
consecutive full-`X` owner occurrences.  Distinct sheets must have distinct
literal profiles somewhere, or the addressed owners remain equal and the
detachment is fictitious.  At the first profile change, a one-in/one-out
current seam would satisfy (4.1), and rigidity would force (4.2), a
contradiction. \(\square\)

This is exactly why taking three private copies of the four-edge current
rectangle cannot work: simple current matching forces the private profiles
back together before the owner collision is removed.

## 5. The minimal constructive interface

Theorem 2.1 identifies the correct incidence skeleton for a branched lift:
four owner columns, each incident with three row fragments, together with
the three perfect sheet matchings

\[
                       M_c=\{R_iE_{i+c}:i\in\mathbb Z_4\},
                       \qquad c=1,2,3.                 \tag{5.1}
\]

At each owner column a direct local adapter must accept three incoming
profiles and return three outgoing profiles while preserving their
aggregate complete current.  A capacity-one seam is impossible by
Theorem 4.1.  The column itself is ternary; the theorem does not exclude a
larger realization which factors that node through auxiliary binary
branches.

The masked-core triangle theorem is a literal example of such an arity-
three, addresswise zero-current profile change.  It therefore has the right
local algebra.  What is not yet proved is a simultaneous embedding of four
masked triangles whose twelve fragments:

1. realize the incidence colouring (2.1) on both H-square shores;
2. reassemble into simple owner/root paths rather than a multifactor;
3. preserve the noncrossing portions of the D3 rail current; and
4. retain the endpoint and terminal common-cap interfaces.

Thus the exact successor is no longer an unspecified three-sheet cover.  It
is a **four-column ternary branch gluing lemma** on the crown factorization
(5.1).  Proving that lemma would detach the H-square at the minimum possible
owner multiplicity; a one-in/one-out construction is now ruled out.

## 6. Battery-equipped alternative

The later dual four-ray theorem supplies a second, logically different
escape from Theorem 4.1.  If every profile-changing fragment seam is
coinstantiated with its shielded lower-and-upper bi-battery, that battery
absorbs the seam's complete rail current locally.  The crown fragments then
need not cancel their profile currents against one another, so the
one-in/one-out rigidity obstruction no longer applies.

This does not solve owner detachment: the colouring (2.1) and a literal
split/reassembly of the twelve fragments are still required.  Moreover the
battery theorem is conditional on a common host which makes every
cross-native/battery interval invariant and separates physical capacities.
It yields the alternative exact target

> **Battery-equipped crown detachment.**  Realize the three-sheet incidence
> colouring (2.1) as simple source fragments, and coinstantiate every
> profile-changing seam with a protected bi-battery inside one resident
> owner/compiler host.

Thus there are now two proof-safe construction routes: four correlated
ternary zero-current branches, or individually battery-neutralized crown
seams.  Neither physical host is yet proved.
