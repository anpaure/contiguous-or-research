# The `D_0V -> T_0V` donor transfer has a nonzero q2 coordinate current

**Date:** 2026-08-05  
**Method:** incidence-degree conservation; no computation or search  
**Status:** unconditional obstruction to an endpoint-transparent,
palette-preserving prefix macro whose other q2 turns are only permuted.
The donor supply is real, but a valid repair must carry an opposite
companion turn current or export the imbalance through path endpoints.

## 1. Turn marginals in an owner--upper-colour incidence factor

Let `Omega` have order `2r`.  Consider the Boolean incidence graph between
rank-`r` owners `X` and rank-`(r+1)` upper colours `Q`.  Let `F` be a
selected subgraph in which every upper colour has degree two and every
owner has prescribed degree one or two.  Put

\[
 I=\{X:d_F(X)=2\},\qquad E=\{X:d_F(X)=1\}.          \tag{1.1}
\]

At an internal owner `X in I`, write its two incident colours as

\[
                         X+a,\qquad X+b,qquad a\ne b.
\]

Its upper-q2 turn is

\[
                         \tau_F(X)=X\cup\{a,b\}.    \tag{1.2}
\]

For a coordinate `c`, define

\[
 M_c(F)=|\{X\in I:c\in\tau_F(X)\}|.                \tag{1.3}
\]

Also let `A_c(F)` be the number of selected incidences `XQ` whose added
coordinate is `c`, that is, `Q\setminus X={c}`, and let `E_c(F)` count
such incidences with `X in E`.

### Lemma 1.1 (exact coordinate-current identity)

For every coordinate `c`,

\[
 \boxed{
 M_c(F)=|\{X\in I:c\in X\}|+A_c(F)-E_c(F).}         \tag{1.4}
\]

Moreover `A_c(F)` is forced by the owner and colour degree vectors:

\[
 \boxed{
 A_c(F)=
 \sum_{Q\ni c}d_F(Q)-\sum_{X\ni c}d_F(X).}          \tag{1.5}
\]

#### Proof

If an internal owner contains `c`, then so does its turn.  If it does not
contain `c`, its turn contains `c` exactly when its unique possible
incidence to `X+c` is selected.  Counting those added-`c` incidences over
internal owners gives `A_c-E_c`, proving (1.4).

Every selected incidence into a colour `Q` containing `c` is of exactly
one of two kinds: its owner already contains `c`, or its added coordinate
is `c`.  Every selected incidence at an owner containing `c` belongs to a
colour containing `c`.  Subtracting the two incidence counts gives (1.5).
`square`

### Corollary 1.2 (endpoint-transparent q2 marginal invariant)

Let `F,F'` have the same owner degrees and the same upper-colour degrees.
If their selected endpoint incidences have the same added-coordinate
multiset—in particular, if the exchange avoids all endpoints—then

\[
                         M_c(F')=M_c(F)              \tag{1.6}
\]

for every coordinate `c`.

Equivalently, an alternating incidence-hex/C6 sequence supported on
internal owners preserves the complete coordinate-incidence vector of the
upper-q2 turn multiset.

This can also be seen locally.  Around an alternating incidence cycle, the
added-coordinate labels on the deleted incidences and on the inserted
incidences are the leaving and entering labels of one closed owner walk;
they are the same multiset.

## 2. The proposed missing target and donor

Use one-based prefix coordinates and put

\[
 T_0=110011001111,
 \qquad
 D_0=101011110101.                                  \tag{2.1}
\]

Their one-sets are

\[
 \begin{aligned}
 T_0&=\{1,2,5,6,9,10,11,12\},\\
 D_0&=\{1,3,5,6,7,8,10,12\}.
 \end{aligned}                                      \tag{2.2}
\]

Hence

\[
 T_0\setminus D_0=\{2,9,11\},
 \qquad
 D_0\setminus T_0=\{3,7,8\}.                       \tag{2.3}
\]

The exact `Gamma` inverse criterion gives four donor preimages for `D_0`.
Its height-zero upsteps are at positions `1,3,5`, its height-three upsteps
are at positions `8,10,12`, and there is no forbidden height-two or
height-three downstep between the paired positions.  This gives the first
three pairs below.  In addition, the height-one upstep at position `6` and
the height-two upstep at position `7` form a fourth admissible pair:

\[
             (1,12),\qquad(3,10),\qquad(5,8),\qquad(6,7).
                                                               \tag{2.4}
\]

For the first three pairs the two ordinal counts are respectively
`0,1,2`; for `(6,7)` they are both `3`.  Direct inspection of the eligible
height classes shows that this list is complete.  Thus `D_0` has exactly
four canonical q2 occurrences, while the already proved inverse obstruction
says `T_0` has none.

## 3. No pure donor-to-hole macro

### Theorem 3.1

There is no palette-preserving, owner-degree-preserving incidence-hex/C6
sequence which

1. is endpoint-transparent;
2. removes one q2 occurrence of `D_0` and adds one occurrence of `T_0`;
   and
3. merely permutes all other q2 turn targets.

#### Proof

Permuting the other turns contributes zero to every coordinate marginal.
The advertised donor transfer changes the q2 coordinate vector by

\[
 e_2+e_9+e_{11}-e_3-e_7-e_8,                       \tag{3.1}
\]

which is nonzero.  Corollary 1.2 says that an endpoint-transparent
palette/owner exchange has zero coordinate current.  Contradiction.
`square`

The conclusion is stronger than failure of one guessed hexagon.  It rules
out every finite composition of internal alternating incidence circuits
with the stated pure-transfer effect.

## 4. Dyck-suffix tensoring does not remove the obstruction

Let `V` be any Dyck suffix of semilength `r-6`.  Read it from height four.
It adds no eligible height-zero/one `p`, no height-two/three `q`, and no
ordinal term in the exact `Gamma` inverse test.  Therefore the four donor
preimages (2.4) persist for `D_0V`, while `T_0V` remains missing.

But the two targets have the same suffix coordinates.  Their coordinate
current is still exactly (3.1), supported on the first twelve positions.
Thus:

### Corollary 4.1

No endpoint-transparent palette-preserving macro can simultaneously make
the transfers

\[
                         D_0V\longmapsto T_0V        \tag{4.1}
\]

for all `Cat_(r-6)` Dyck suffixes while merely permuting every other q2
turn.  The aggregate prefix current is `Cat_(r-6)` times (3.1), still
nonzero.

## 5. Exact constructive escape

The donor idea is not dead; its correct form must be **current balanced**.
There are only two possibilities:

1. change companion q2 turns whose total coordinate current is the
   negative of (3.1); or
2. export (3.1) through changed endpoint incidence labels, thereby paying
   and later routing an endpoint/stem sidecar.

A full coordinate-rotation orbit of donor transfers has zero aggregate
coordinate current, because every coordinate occurs equally often in the
rotated copies of two sets of the same rank.  This identifies a plausible
global macro: repair a balanced orbit of missing suffix families rather
than one fixed prefix family.  What remains is to prove that the required
rotated donor occurrences coexist in one MSW factor and that the companion
turns, protected stems, and arbitrary-upper witnesses transport.

The theorem therefore gives an exact verdict on the proposed one-prefix
macro: the donor supply tensors, but a pure `D_0V -> T_0V` transfer does
not.
