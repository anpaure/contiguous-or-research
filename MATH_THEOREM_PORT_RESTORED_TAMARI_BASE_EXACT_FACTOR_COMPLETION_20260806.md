# The port-restored Tamari packet has an exact noncanonical base factor

## Status

The four-row Tamari note proves a local support-matched trade and records a
canonical Dyck-port obstruction.  The latter does **not** obstruct arbitrary
exact-factor completion.  The original nonlocal Haar certificate supplies
a common ten-wreath complement, and the port-restored packet has the same
central support as the Haar positive phase.

Consequently, at semilength four, both sides of the port-restored trade lie
in exact fourteen-wreath factors.  The unsolved host problem begins only
when this noncanonical base factor is lifted to all dimensions.

## 1. Imported exact completion

`NONLOCAL_HAAR_M4.md` gives four negative wreath orders `N`, four positive
wreath orders `P`, and ten common orders `C` such that

\[
                         C\mathbin{\dot\cup}N,
 \qquad                  C\mathbin{\dot\cup}P          \tag{1.1}
\]

are exact factors of all `binom(9,4)=126` middle vertices.

Section 9 of
`MATH_ATTACK_E_FOUR_ROW_TAMARI_ASSOCIATOR_20260726.md` gives the coordinate
relabeling

\[
 1\mapsto8,\ 2\mapsto6,\ 3\mapsto4,\ 4\mapsto7,
 \ 5\mapsto5,\ 6\mapsto3,\ 7\mapsto2,\ 8\mapsto1,    \tag{1.2}
\]

with the omitted coordinate `9` fixed, together with harmless row
reversals, which sends the Haar four-for-four packet to

\[
                         {\cal P}^-\longleftrightarrow {\cal P}^+.
                                                               \tag{1.3}
\]

Apply the same relabeling and row reversals to the ten common orders, and
call the resulting family `C'`.

### Lemma 1.1

Both

\[
                         C'\dot\cup {\cal P}^-,
 \qquad                  C'\dot\cup {\cal P}^+       \tag{1.4}
\]

are exact shortest-wreath factors on nine coordinates.

#### Proof

Coordinate relabeling and reversal are automorphisms of the middle-levels
incidence graph and preserve every wreath support.  Apply them to the two
exact factors (1.1). \(\square\)

## 2. Port restoration does not change support

Let `X(Q)` be the rank-four state support of a four-row path packet and let
`Y(Q)` be its aggregate adjacent-union support.  The base associator note
proves

\[
 X({\cal P}^*)=X({\cal P}^+),
 \qquad
 Y({\cal P}^*)=Y({\cal P}^+),                         \tag{2.1}
\]

with every state and union occurring once.

In the odd-graph lift, vertices avoiding the omitted coordinate are the
`X` states.  Vertices containing it are obtained by complementing the
`Y` unions and adjoining the omitted coordinate.  Hence (2.1) implies

\[
              V({\cal P}^*)=V({\cal P}^+)            \tag{2.2}
\]

as literal middle-vertex sets.

### Theorem 2.1 (exact noncanonical host at `r=4`)

Both

\[
                         C'\dot\cup {\cal P}^-,
 \qquad                  C'\dot\cup {\cal P}^*       \tag{2.3}
\]

are exact fourteen-wreath factors.  Thus

\[
                         {\cal P}^-\longleftrightarrow {\cal P}^* \tag{2.4}
\]

is an actual fixed-endpoint move between exact noncanonical factors, not
merely a signed or partial-factor relation.

#### Proof

The first factor is Lemma 1.1.  In the second factor, replace the four
positive wreath cycles by the port-restored cycles.  Equation (2.2) says
that the four cycles occupy exactly the same middle vertices.  They are
pairwise disjoint by the base packet theorem, so they remain disjoint from
`C'` and still cover the entire middle layer once. \(\square\)

## 3. Exact scope

Proposition 7.3 of the base associator note remains correct: neither packet
can occur in the **canonical Dyck-port-transversal** factor because three
Dyck states are internal.  Theorem 2.1 shows that this is a canonical-host
obstruction, not a universal completion obstruction.

The all-dimensional tensor theorem extends the four-row partial trade but
does not extend the ten-row complement `C'`.  The next host statement is
therefore precise:

> **Noncanonical Tamari host suspension.**  Extend the exact factors (2.3)
> from semilength four to every sufficiently large semilength while
> retaining the tensored four-row packet and the protected all-width tail
> rails.

At the base dimension, host extension and dynamic legality are now closed
exactly.
