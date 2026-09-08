# Canonical MSW common-history rethreading has an absolute alternating upper portal hole

**Date:** 2026-08-13  
**Status:** unconditional all-parameter obstruction for `m>=8` and every
source depth `4<=d<m+1`.  It concerns rethreadings which keep the canonical
MSW owner occurrences and alter successors only at literal common-history
ports.  It does not exclude an incidence trade which first changes those
owner occurrences, such as a two-hex upper relay.

## 0. Outcome

Put

\[
 n=2m+1,\qquad R=m+1,
\]

and label the finite coordinates by `0,1,...,2m-1`, with the usual extra
MSW coordinate `2m`.  For `m>=8`, define

\[
 U_m=110011001111(10)^{m-6}.                         \tag{0.1}
\]

Thus `U_m` is a rank-`(R+1)` subset of the finite coordinates.  It is one
of the canonical upper-`q2` holes `T_0V` from Theorem 4.1 of
`MATH_OBSTRUCTION_CANONICAL_MSW_Q2_SURJECTIVITY_INFINITE_FAMILY_20260805.md`,
with the Dyck suffix `V=(10)^(m-6)`.

The new point is stronger than canonical absence:

> **Absolute portal theorem.**  Let `4<=d<R`.  For no two distinct labels
> `x,y in U_m` do the canonical occurrences of the two owners
> `U_m-{x}` and `U_m-{y}` admit a literal common depth-`d` history with the
> first owner on the left side of the cut and the second owner on the right.

Consequently no collection of common-history successor splices--even using
arbitrary root pairs, arbitrary orientations, arbitrarily many separated
ports per root, and an arbitrary final Euler tour--can create `U_m` as an
upper value.  Indeed, two distinct rank-`R` subsets of the rank-`(R+1)` set
`U_m` are necessarily

\[
 U_m-\{x\},\qquad U_m-\{y\},                         \tag{0.2}
\]

and their union is `U_m`.  Every new adjacency in a common-history
rethreading is a compatible left/right pair, which the theorem excludes.

This formally closes the route in which the canonical MSW factor is made
upper-complete by common-history fusion alone.  A route mixing
common-history fusion with owner-changing upper actuators remains open.

## 1. The explicit owner intervals

Write

\[
 C=\{0,1,4,5,8,9,10,11\},\qquad
 E=\{12,14,\ldots,2m-2\}.                            \tag{1.1}
\]

Then `U_m=C union E`, and `|E|=m-6`.  Write `E^up` and `E^down` for the
increasing and decreasing lists, and similarly write `E_(<e)^down` and
`E_(>e)^down`.

For every `x in U_m`, the unique canonical occurrence of `U_m-{x}` is a
length-`R` interval in its tight MSW row.  In one of the two row
orientations, the ordered interval is the following word `a_x`:

\[
\begin{array}{c|l}
x&a_x\\ \hline
0 &(10,E^\uparrow,1,5,4,9,8,11)\\
1 &(10,8,9,4,5,11,E^\downarrow,0)\\
4 &(10,8,9,5,11,E^\downarrow,0,1)\\
5 &(4,10,8,9,11,E^\downarrow,0,1)\\
8 &(5,10,9,11,E^\downarrow,0,1,4)\\
9 &(5,8,10,11,E^\downarrow,0,1,4)\\
10&(8,9,11,E^\downarrow,0,1,4,5)\\
11&(5,8,9,E^\downarrow,10,0,1,4)\\
e\in E&(5,8,9,E_{>e}^\downarrow,10,
          E_{<e}^\downarrow,11,0,1,4).
\end{array}                                             \tag{1.2}
\]

Every displayed word has length `R` and set `U_m-{x}`.

### Lemma 1.1 (canonical provenance)

The words in (1.2) are the oriented canonical tight-row intervals of the
owners `U_m-{x}`.

#### Proof

Here are explicit Dyck roots for the eight fixed cases, followed by the
common suffix `(10)^(m-6)`:

\[
\begin{array}{c|c}
x&\text{twelve-letter prefix}\\ \hline
0&101100110010\\
1&111100110000\\
4&110110110000\\
5&110101110000\\
8&110110011000\\
9&110110010100\\
10&110111010000\\
11&110110010010.
\end{array}                                             \tag{1.3}
\]

For `e=12+2i`, where `0<=i<=m-7`, use

\[
 110110010011(10)^i00(10)^{m-7-i}.                    \tag{1.4}
\]

Substitution in the standard tight-row recurrence

\[
 \rho(1u0v)=\bigl(c,c-\rho(\mu u),1,c+\rho(v)\bigr)   \tag{1.5}
\]

gives precisely the cyclic intervals (1.2), allowing reversal of the
unoriented row.  Concretely, appending one terminal `10` appends the next
even label to the monotone `E` rail; in (1.4), moving the unique `00` one
block to the right moves that even label across the central label `10`.
The eight fixed prefixes give the eight first lines of (1.2), and this
one-step recursion gives the last line for every `i`.  This proves the
claim.  \(\square\)

## 2. Depth-four left and right port states

Let `a=(a_0,...,a_(R-1))` be one of the words (1.2), or its reversal.
At depth four, put `s=R-4`.  If this owner lies immediately to the left
of a proposed seam, its four maximal letters and forced pairs are

\[
\begin{aligned}
 P^L_j(a)&=\{a_{j+1},\ldots,a_{j+R-4}\},\\
 F^L_j(a)&=\{a_{j+1},a_{j+R-4}\},
                         &&0\le j<4.                 \tag{2.1}
\end{aligned}
\]

If it lies immediately to the right, they are

\[
\begin{aligned}
 P^R_j(a)&=\{a_j,\ldots,a_{j+R-5}\},\\
 F^R_j(a)&=\{a_j,a_{j+R-5}\},
                         &&0\le j<4.                 \tag{2.2}
\end{aligned}
\]

These are just the tight-row specialization of the exact maximal-envelope
and forced-pair formulas.  Therefore a left occurrence `a_x` and a right
occurrence `a_y` are depth-four common-history compatible only if

\[
 F^L_j(a_x)\cup F^R_j(a_y)
 \subseteq P^L_j(a_x)\cap P^R_j(a_y)
 \quad(0\le j<4).                                    \tag{2.3}
\]

The formulas also show why this test has a uniform all-`m` boundary: each
`P` omits only four positions from its owner interval, while every `F`
uses only its first or last five positions.

### Lemma 2.1 (complete depth-four exclusion)

For every `m>=8` and every ordered pair of distinct labels `x,y in U_m`,
(2.3) fails for all four choices of orientations of `a_x,a_y`.

#### Proof

First project (2.3) onto the fixed core `C` in (1.1).  Direct substitution
of the first and last five entries in (1.2) gives the following exhaustive
table.  A plus sign means the displayed orientation in (1.2), and a minus
sign means its reversal:

\[
\begin{array}{c|c}
(\operatorname{or}(a_x),\operatorname{or}(a_y))
 &\text{ordered pairs surviving the core projection}\\ \hline
(+,+)&(x,y)=(e,10),\quad e\in E-\{2m-4,2m-2\},\\
(+,-)&\varnothing,\\
(-,+)&\varnothing,\\
(-,-)&(x,y)=(10,e),\quad e\in E-\{2m-4,2m-2\}.
\end{array}                                             \tag{2.4}
\]

For clarity, (2.4) is not an asymptotic or computational classification.
It is the fixed boundary check obtained from (1.2): use (2.1)--(2.2),
discard every pair for which one of `0,1,4,5,8,9,10,11` belongs to a
forced pair on one side and to one of the four omitted boundary positions
on the other, and the two displayed families are exactly what remains.
The two largest even labels are excluded already by the positions of
`10` and `11` at the moving break in the last line of (1.2).

It remains to eliminate the two families in (2.4).  Put

\[
                         e_*=2m-2.                   \tag{2.5}
\]

In the `(+,+)` survivor `(x,y)=(e,10)`, the label `e_*` lies in
`F^R_3(a_10)` but not in `P^L_3(a_e)`.  In the `(-,-)` survivor
`(x,y)=(10,e)`, it lies in `F^L_0(reverse(a_10))` but not in
`P^R_0(reverse(a_e))`.  Thus (2.3) fails in the final tail coordinate in
both cases.  When `m=8`, the survivor set in (2.4) is already empty.
This proves the lemma.  \(\square\)

## 3. Descent from an arbitrary depth to depth four

Let `D` be consecutive union on a cyclic literal source word.  Its powers
compose:

\[
                         D^aD^b=D^{a+b}.              \tag{3.1}
\]

### Lemma 3.1 (history erosion)

If two owner circuits admit a common literal length-`d` history at a cut,
where `d>=4`, then the same two oriented owner occurrences admit a common
literal length-four history at that cut.

#### Proof

Let the two depth-`d` antecedents share source letters
`H_1,...,H_d` at the port.  Apply `D^(d-4)` to both antecedents.  On the
shared block this produces the same four letters

\[
 H'_i=H_i\cup H_{i+1}\cup\cdots\cup H_{i+d-4}
 \quad(1\le i\le4).                                  \tag{3.2}
\]

By (3.1), applying `D^4` to either eroded antecedent gives the original
owner circuit.  Hence (3.2) is a common depth-four history at the same
oriented owner boundary.  \(\square\)

### Theorem 3.2 (absolute common-history portal hole)

For every `m>=8` and `4<=d<R`, no pair of canonical occurrences
`U_m-{x}`, `U_m-{y}` with `x!=y` admits a common literal depth-`d` port.

#### Proof

Such a port would descend by Lemma 3.1 to a depth-four port, contradicting
Lemma 2.1.  \(\square\)

## 4. Global rethreading consequence

Consider any successor rethreading of the complete canonical MSW owner
occurrences in which every changed successor is made at a literal common
depth-`d` source state.  This includes edge-dependent port states,
multi-port rows, separated spanning-tree splices, and arbitrary Euler tours
of the resulting labelled de Bruijn multigraph.

### Corollary 4.1

For `m>=8` and `4<=d<R`, the target `U_m` does not occur in the upper
owner-union deck after any such rethreading.

#### Proof

The target is absent on every original canonical component by the
infinite-family obstruction cited after (0.1).  If it appeared after
rethreading, take a witnessing consecutive owner interval.  Every owner in
that interval is a rank-`R` subset of `U_m`; otherwise the union would
contain a coordinate outside `U_m`.  Since the union has rank `R+1`, not
all owners are equal.  At the first change between distinct consecutive
owners, the two owners are `U_m-{x}` and `U_m-{y}` for distinct `x,y`, and
their union is `U_m`.

If that adjacency was old, it contradicts canonical absence.  If it was
new, its outgoing and incoming occurrence halfedges were paired at one
common depth-`d` history, contradicting Theorem 3.2.  Thus no witness can
exist.  \(\square\)

The conclusion is absolute within the common-history-only model: adding
more ports or allowing an edge-dependent state at each port cannot help,
because the obstruction is checked on every possible pair of endpoint
owners.  It does **not** say that `U_m` is an intrinsic hole of every
integral factor.  An owner-changing alternating circuit may create a new
rank-`R` occurrence or adjacency outside the canonical list used in
Lemma 2.1.

## 5. Finite replay and scope

The formula verifier is

`scratch/verify_msw_alternating_TV_depth4_portal_obstruction_20260813.py`.

It instantiates (1.2), checks all ordered pairs and orientations in (2.3),
verifies the exact core-survivor classification (2.4), and checks the final
witness (2.5).  As a separate provenance check, it applies the exact
canonical `g/h` construction to only the explicitly listed roots
(1.3)--(1.4) and verifies that every `a_x` is the asserted oriented cyclic
interval.  It never enumerates the Catalan family of roots.  The H100
replay passed for every `8<=m<=60`.

The JSON transcript is

`scratch/msw_alternating_TV_depth4_formula_8_60.json`.

The replay is an audit of the displayed all-`m` formulas, not the basis of
the proof.

The precise remaining escape routes are:

1. first apply a conformal owner/incidence trade which changes the
   canonical occurrences involved in (1.2);
2. install an independent literal source occurrence of `U_m` in a
   protected upper relay; or
3. abandon literal common-history successor pairing at the relevant seam
   and pay a separately controlled source correction.

Thus canonical common-history fusion remains a complete solution of the
short-deck topology problem, but it is not by itself an upper-completion
theorem.
