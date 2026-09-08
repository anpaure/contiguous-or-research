# The unique two-hex MNW boundary restore leaves one unit q2 debt

**Date:** 2026-08-07  
**Method:** exact MSW touching-step phases and inverse multiplicities; no
computation or search  
**Status:** unconditional local classification in the
canonical-plus-gamma-alpha factor.  Exactly one nontrivial second hex
restores the source boundary.  Its combined q2 current deletes a unique
provider, so two hexagons do not close the relay.

## 1. State after the first leaf hex

Use the notation of the leaf endpoint-transfer theorem.  After its first
hexagon, the destination edge `(X,Q)` is selected, but at the source owner

\[
                         Y=0110001101                  \tag{1.1}

the selected boundary edge `M=Y+9` has been replaced by

\[
                         R=Y+1=1110001101.             \tag{1.2}

We seek a second incidence hexagon at `Y` which swaps `R` back to `M`
without touching `(X,Q)`.

Choose a core label `c in Y` and use active labels `c,1,9`.  The choice
`c=2` reproduces the first hexagon and simply reverses it.  The nontrivial
possibilities are

\[
                         c\in\{3,7,8,10\}.             \tag{1.3}

## 2. Exact phase classification

Put `K_c=Y-c`.  Besides `Y`, the second hex has owners

\[
                         Y_1=K_c+1,
 \qquad
                         Y_9=K_c+9.                   \tag{2.1}

For the hex to be alternating in the required orientation, the current
factor must select `Y_1+9` but not `Y_1+c`, and select `Y_9+c` but not
`Y_9+1`.

### `c=3`

The auxiliary owners are

\[
                         Y_1=1100001101,
 \qquad
                         Y_9=0100001111.              \tag{2.2}

The first is an internal canonical owner with selected additions `5,9`;
the second is a reverse endpoint with sole selected addition `3`.  Neither
is changed by the gamma-alpha pair or by the first leaf hex.  Hence the
required statuses hold and this hex is alternating.

### `c=7`

Here `Y_1=1110000101`, an alpha-relay centre.  After `alpha(1100)`, its
selected additions are `5,7`; addition `9` is unselected.  The required
phase is the opposite one.

### `c=8`

Here `Y_1=1110001001`, a mirror-gamma centre.  Its selected additions after
the first relay are `4,6`; both required additions `8,9` are unselected.

### `c=10`

Here `Y_1=1110001100` is a forward Dyck endpoint whose sole selected
addition is `10`.  The required phase needs addition `9` selected and
addition `10` unselected, again the opposite.

Thus:

### Theorem 2.1 (unique second face)

Among all nonreversing choices (1.3), exactly `c=3` gives an alternating
second hexagon.

## 3. Its q2 current

At `Y`, the second hex restores the turn

\[
1110101101\longmapsto0110101111.                     \tag{3.1}

At `Y_1=1100001101`, its untouched mate is addition five; replacing
addition nine by addition three changes

\[
1100101111\longmapsto1110101101.                     \tag{3.2}

The auxiliary owner `Y_9` is an endpoint.  Therefore the second hex has
current

\[
                  +[0110101111]-[1100101111].         \tag{3.3}

The first leaf hex had current

\[
                  +[1010101111]-[0110101111].         \tag{3.4}

The middle target cancels, and the exact two-hex current is

\[
 \boxed{
                  +[1010101111]-[1100101111].}        \tag{3.5}

## 4. The terminal negative has multiplicity one

For

\[
                         J=1100101111,                \tag{4.1}

the exact canonical q2 inverse test has the unique witness

\[
                         (p,q)=(5,9).                 \tag{4.2}

Indeed, the only candidate `q` positions are nine and ten.  The down-step
at position three starts at height two and excludes the earlier `p`
positions; among the later candidates, only position five has left ordinal
count one, equal to the right count at position nine.  No later candidate
has right count zero at position ten.

The positive target `1010101111` has canonical multiplicity two.  Hence the
two-face macro restores both boundary phases and preserves q1 exactly, but
it moves one q2 hole to `J`.

Dyck suffixing preserves this exact statement and gives the terminal debt

\[
                         1100101111v.                 \tag{4.3}

## 5. Consequence

The one-prefix prism cannot be closed by the obvious two-face endpoint
transfer.  A third signed relay must introduce `Jv` while deleting only a
redundant target, or a compound rectangle in the full interleaved annulus
must supply the same correction.

This is an incidence-level obstruction, not a topology issue: the two
hexagons are literal alternating switches and restore the source and
destination boundary edges exactly before the q2 debt is evaluated.

