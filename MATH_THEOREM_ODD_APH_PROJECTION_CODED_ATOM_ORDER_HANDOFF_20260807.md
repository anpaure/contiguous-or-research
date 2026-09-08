# Odd APH: projection-coded pilot order preserves the atom branch through retirement

**Date:** 2026-08-07  
**Scope:** repair of the failed register row in
`MATH_THEOREM_ODD_APH_ODD_PILOT_TRAIN_AND_RETIREMENT_20260806.md`  
**Method:** keep the protected atom register literal, store the collar order
in the two already reserved odd code blocks, and transfer records only after
their old sources are literal; no computation or search  
**Status:** **candidate pending independent occurrence audit; do not yet cite
as APH.**  The scalar resource ledger and task substitutions are inherited
from the clean-selection, farthest-first, and variable-mass `G_1` theorems.
This note replaces the noninjective rewrite
`Q_q -> widehat Q_(q,r)` and supplies the corresponding variable-pilot
crossing and phase schedule.

## 1. The failed row and the repair principle

The clean setup proves source injectivity using

\[
            (D,\ Q_q,\ \hbox{literal source collar}),
        \qquad q\in\{0,1,3\}.                         \tag{1.1}
\]

The previous pilot candidate overwrote `Q_q` before proving another copy of
`q`.  Its proposed endpoint was not injective in `q`, even after the final
collar record was adjoined.  The repair is therefore deliberately
asymmetric:

1. `Q_q` is never changed during setup, any task visit, collar regeneration,
   the cart return, or reverse motif teardown;
2. the already reserved mass-four pilot/delimiter pair stores the collar
   order `r`; and
3. only after the exact raw motif is literal again is `Q_q` rewritten to a
   collar-order state.

Thus `q` is copied from `Q_q` back to its raw source before it is erased,
and `r` is copied from the odd pair to the final collar before that pair is
erased.

## 2. One mass-four pair stores the order in both projections

Continue to write

\[
 A=00,\quad B=20,\quad C=22,\quad
 H=02,\quad M=11.                                     \tag{2.1}
\]

Assign the ordered source collar, within each fixed-sum fibre, the classes

\[
\begin{array}{c|c}
\hbox{source collar}&r\\ \hline
A|A&0\\
A|B,\ B|A&0,1\\
A|C,\ B|B,\ C|A&0,1,2\\
B|C,\ C|B&0,1\\
C|C&0.
\end{array}                                             \tag{2.2}
\]

Use the following odd pair at the declared code berth:

\[
\begin{array}{c|c|c|c|c|c}
r&P_r&D_r&C_r=P_r|D_r&\bar D_r&S_r\\ \hline
0&01&21&0121&12&H\\
1&10&12&1012&21&M\\
2&21&10&2110&01&B.
\end{array}                                             \tag{2.3}
\]

Here `bar D_r` is the selected-support `M` branch value and `S_r` is the
temporary train-head value used only while the train crosses `D_r` itself.

### Lemma 2.1 (two projection decoders)

Every row of (2.3) has total mass four.  Each `P_r` and each `D_r` has odd
mass, the three `P` projections are distinct, the three `D` projections are
distinct, and `P_r != D_r` in every row.  The three `bar D_r` values are
also distinct and have the same respective masses as `D_r`.

Consequently:

* whenever `P_r` is literal, it alone recovers `r`;
* whenever `D_r` is literal, it alone recovers `r`;
* a literal `bar D_r` recovers both `r` and the selected-`M` branch; and
* at a macro checkpoint the moving odd block `P_r` is distinguishable from
  the stationary odd block `D_r` and from every even ordinary block.

#### Proof

The `P` masses are `1,1,3`, the `D` masses are `3,3,1`, and each row sums
to four.  The projection lists are

\[
        (01,10,21),\qquad (21,12,10),\qquad(12,21,01),
                                                               \tag{2.4}
\]

which are injective.  All remaining claims are literal inspection of
(2.3). \(\square\)

### 2.1 Explicit code writing from the clean spare pair

The clean selection theorem supplies one disjoint raw spare pair

\[
                          BB,\qquad AC,\qquad CA                 \tag{2.5}
\]

of mass four.  Use the following arms to the mass-four hub `1111`:

\[
\begin{array}{c|l}
BB&2020\to2011\to1111,\\
AC&0022\to0112\to1012\to1102\to1111,\\
CA&2200\to2110\to2020\to2011\to1111,
\end{array}                                             \tag{2.6}
\]

and the following arms from the hub:

\[
\begin{array}{c|l}
C_0&1111\to0211\to0121,\\
C_1&1111\to1102\to1012,\\
C_2&1111\to2011\to2020\to2110.
\end{array}                                             \tag{2.7}
\]

Every arrow is one adjacent unit transfer and no displayed state is
`H|H=0202`.  Concatenate the appropriate two arms and erase the resulting
loops; the endpoint cannot equal the raw source because its two aligned
blocks have odd mass.  This gives a nonempty simple path from every source
in (2.5) to every `C_r`.

During this path the stationary temporary cart, `Q_q`, the literal source
collar, the declared code-berth side, and the clean theorem's gap trails are
unchanged.  They are exactly the source decoder already proved for the
clean spare-pair route.  Changing the endpoint among (2.3) changes neither
its support nor its mass.  Split `C_r` into the moving `P_r` and stationary
`D_r`, and attach `P_r` to the cart tail by the same declared bounded berth
permutation.  No collar or task coordinate is used.

The resource lifecycle is therefore

\[
 \text{raw spare pair}\longrightarrow C_r
 \longrightarrow (\text{moving }P_r,\text{ origin }D_r)
 \longrightarrow C_r\longrightarrow\text{the same raw pair}.   \tag{2.8}
\]

It has zero net mass and restores every source coordinate.

## 3. Variable-pilot block crossings

Write a right-going train as `U|V|P_r`.  Every allowed train contains at
least one head in `U|V`.  To cross one aligned block `Y`, use

\[
 U|V|P_r|Y
   \leadsto U|V|Y|P_r
   \leadsto Y|U|V|P_r.                                \tag{3.1}
\]

The first arrow uses the following literal four-coordinate paths.

For `P_0=01`:

\[
\begin{array}{c|l}
A&0100\to0010\to0001\\
B&0120\to1020\to1110\to2010\to2001\\
M&0111\to1011\to1101\\
C&0122\to1022\to1112\to2012\to2021\to2111\to2201\\
D_0&0121\to1021\to1111\to2011\to2101.
\end{array}                                             \tag{3.2}
\]

For `P_1=10`:

\[
\begin{array}{c|l}
A&1000\to0100\to0010\\
B&1020\to1011\to1002\to0102\to0111\to0201
       \to1101\to2001\to2010\\
M&1011\to1002\to0102\to0111\to0201\to1101\to1110\\
C&1022\to1112\to2012\to2102\to2111\to2201\to2210\\
D_1&1012\to1102\to1111\to1201\to1210.
\end{array}                                             \tag{3.3}
\]

For `P_2=21`:

\[
\begin{array}{c|l}
A&2100\to2010\to1110\to1101\to1011\to0111
       \to0102\to0012\to0021\\
B&2120\to2111\to2102\to2012\to2021\\
M&2111\to1211\to1202\to1112\to1121\\
C&2122\to2212\to2221\\
D_2&2110\to2101\to2011\to2002\to1102\to1111\to1021.
\end{array}                                             \tag{3.4}
\]

Every displayed arrow is one adjacent unit transfer.  In every strict
state its right aligned block is different from the relevant `P_r`; that
tail occurs only at the endpoint.  Thus the first phase of (3.1) cannot
meet the second phase, in which `P_r` is held literally at the train tail.

For the second arrow, hold `P_r` fixed and choose one simple path in the
six-coordinate fixed-mass layer

\[
                         U|V|Y\leadsto Y|U|V.           \tag{3.5}
\]

This layer is nonextreme because `U|V` contains a head, or its declared
temporary mass-two replacement `M` or `B`; each such block has an interior
capacity-two coordinate pattern.  Equation (3.5) is one six-coordinate
rotation, not two successive swaps.  A left-going crossing uses (3.5) and
then the reverse of (3.2), (3.3), or (3.4).

### 3.1 Equal-mass and delimiter guards

The only ordinary equal-mass ambiguity is `B/M`.

* A raw residual corridor uses `B` and keeps `D_r` fixed.
* Before a selected-support `M` enters its tail-clean path, change
  `D_r -> bar D_r` while `P_r` and that `M` are literal.  Hold `bar D_r`
  through both phases of (3.1), then restore `D_r` while the same `M` is
  literal.
* For the one already recorded dirty `G_1` ticket, use the proved
  nonextreme collar toggle in the same way, now holding it through both
  phases rather than only through (3.5).

The `B` and `M` rows of (3.2)--(3.4) may meet in their four-coordinate
projection, but their full states therefore cannot meet.

There is one additional first-visit guard.  In the extreme-collar phase
(4.3), `bar D_1=21` equals the base delimiter `D_0` used during cart
prepositioning.  Before such a first-out selected-`M` crossing, also change
one declared train-head slot `H -> M`, hold that value through both local
phases, and restore it with the crossed `M` literal.  Thus even when the
delimiter projection returns to `21`, the first-out route cannot meet the
prepositioning route.  This extra head tag is unnecessary for every
nonextreme collar because `Phi(K) != K` already supplies the phase record.

When the crossed block is `D_r` itself, both odd code blocks enter the
active window.  Before that crossing, while both are literal, change one
declared train-head slot from `H` to `S_r` in (2.3), along the simple
mass-two path `H -> M -> B` as far as necessary.  Hold `S_r` through the
tail-clean path and (3.5), and restore `H` after `D_r|P_r` is literal.
The declared origin address and `S_r` then recover `r` at every strict
state in which neither odd block is literal.

### Lemma 3.1 (local crossing decoder)

Fix the source, task visit, direction, and crossed physical boundary.
Every macro and strict state in (3.1)--(3.5) recovers `q,r`, the train type,
`Y`, the local phase, and the microstep.

#### Proof

The unchanged `Q_q` gives `q`.  Outside the delimiter crossing, the
stationary `D_r` or `bar D_r` gives the effective code row; during that
crossing `S_r` gives it.  Normally this is `r` itself.  In the first-out
extreme-collar phase, the literal extreme collar and phase record translate
effective row one back to logical order `r=0`.  In the tail-clean phase,
`U,V` stay fixed and the tail is not `P_r`.
The local total mass distinguishes `A,B/M,C` and the delimiter row, while
the delimiter or collar branch tag distinguishes `B/M`.  Each selected row
in (3.2)--(3.4) is simple.

In the rotation phase the literal tail `P_r` gives both the phase and `r`.
The sole exception is the first-out extreme-collar phase of (4.3): there
the effective crossing row is `P_1,D_1`, while the literal extreme collar
and the declared first-out phase recover the logical order `r=0`.
The task record fixes `U,V`; subtracting their known mass from the
six-coordinate mass determines `Y` except for `B/M`, already tagged.
Simplicity of (3.5) then gives its microstep.  At the delimiter boundary the
declared origin location fixes the active window even while both odd blocks
are internal.  Hence equality of two full strict states forces equality of
all decoded data. \(\square\)

At macro checkpoints the physical position of the unique moving value
`P_r` changes by one aligned block at every crossing.  Since `P_r != D_r`,
even their mutual crossing is visible.  Thus distinct crossing counts in
one monotone sweep cannot give the same graph vertex.

## 4. The mandatory first-visit phase record

Keeping `Q_q` unchanged removes the old automatic setup/task phase change.
It must be replaced before the first outward task sweep, because that sweep
may geometrically reverse part of cart prepositioning.

### 4.1 Nonextreme source collars

For source-collar masses two, four, or six, use the following same-mass
phase endpoints:

\[
\begin{array}{c|c|l}
K&\Phi(K)&\hbox{literal path}\\ \hline
A|B&A|M&0020\to0011\\
B|A&M|A&2000\to1100\\
A|C&H|H&0022\to0112\to0202\\
B|B&H|M&2020\to2011\to1111\to0211\\
C|A&M|H&2200\to2110\to1210\to1120\to1111\to1102\\
B|C&M|C&2022\to1122\\
C|B&C|M&2220\to2211.
\end{array}                                             \tag{4.1}
\]

The endpoints are nonraw, pairwise source indexed, and different from
their sources.  Write `Phi(K)` at the collar while `Q_q,P_r,D_r` are
literal.  Hold it throughout the first outward sweep.  After the first
task target is deposited, restore `Phi(K) -> K` while that new literal
ticket is fixed; then perform the ordinary return and collar update.

For a zero-task row the initial collar has mass four.  The assignment (2.2)
and (4.1) gives directly

\[
 \Phi(A|C)=R_0=H|H,\qquad
 \Phi(B|B)=R_1=H|M,\qquad
 \Phi(C|A)=R_2=M|H.                                  \tag{4.2}
\]

Hold this value on the complete cart return to the motif and retain it as
the final order record; no restoration to `K` is made.

### 4.2 Extreme source collars

At mass zero or eight the collar layer is a singleton, and (2.2) has only
`r=0`.  Before the first outward sweep use the two internal fixed-mass
edges

\[
                  (P_0,D_0)=(01,21)
          \longrightarrow(10,21)\longrightarrow(10,12).          \tag{4.3}
\]

Hold the endpoint pair through the outward sweep, using the `P_1,D_1`
crossing rows (3.3).  The literal extreme collar identifies this as the
first-out phase of logical order `r=0`.  Restore (4.3) in reverse only
after the first target ticket is literal.  An extreme initial collar cannot
be a zero-task row, because with no nonzero task its mass could not finish
at four.

### Lemma 4.1 (visit separation)

No state of cart prepositioning, the first outward sweep, a later task
visit, or final teardown is repeated in another one of those phases.

#### Proof

Prepositioning holds raw `K` and the base pair.  The first outward sweep
holds `Phi(K) != K`, or the distinct endpoint pair (4.3).  Once its target
is deposited, that literal ticket separates the return from
prepositioning.

For later visits, the deterministic completed-ticket set and current collar
state form a phase record.  A return from task `i` and the next outward
sweep have the same completed-ticket set, but the intervening nonzero task
changes collar mass by two.  Different task indices otherwise have
different completed-ticket sets.  On final teardown every task ticket is
literal and the collar has been normalized to `R_r`.  In the zero-task row,
(4.2) separates the return and teardown from setup. \(\square\)

## 5. Tasks and guarded collar regeneration

Tensor the proved residual and `G_1` substitutions with the unchanged
pilot `P_r`.  At a residual task use

\[
 X|H_1|H_2|P_r\leadsto M|H_2|X|P_r,                  \tag{5.1}
\]

and at the zipper task use

\[
 X|H_1|H_2|P_r\leadsto X'|Z_d|H_2|P_r.              \tag{5.2}
\]

The old bounded operations act outside `P_r`, so their mass and strict
state decoders are unchanged.  Return the resulting train by Section 3.

At the collar, keep the returned outside head fixed and keep the stationary
origin delimiter `D_r` literal.  Choose one simple path on all eight
coordinates

\[
       X|P_r|K_i\leadsto H|P_r|K_{i+1},               \tag{5.3}
\]

or the identical formula with `X=Z_d`.  Its mass identity is the old one
with `mass(P_r)` added to both sides.  The pilot is allowed to change at
strict states of this path; otherwise it would separate `X` from the collar
and prevent the required mass transfer.  The fixed `D_r` independently
retains `r`, and `Q_q` retains `q`.  The returned head, named task ticket,
and completed-ticket set select the ordered endpoints; simplicity selects
the microstep.  The eight-coordinate layer is nonextreme because its
endpoint contains both a head and an odd pilot, so the prefix-discrepancy
argument supplies the required simple path.  The endpoint is

\[
                         H|H|P_r|K_{i+1},             \tag{5.4}
\]

so the odd pilot separates the temporary cart from a possible collar value
`R_0=H|H`.

The pilot pair has total mass four for every `r`, but neither block pays a
task increment.  Hence the farthest-first capacity order, the exceptional
preliminary residual before `G_1`, and the final collar mass four are
unchanged.

## 6. Copy-before-erase retirement

After the last task, normalize the final mass-four collar while
`Q_q,P_r,D_r` and the completed task tape are literal:

\[
             K_f\leadsto R_r,\qquad
 R_0=H|H,\quad R_1=H|M,\quad R_2=M|H.                 \tag{6.1}
\]

Choose one simple path in the mass-four collar layer.  The odd projections
give `r`, so intersecting collar paths for different order classes are
separated in the full state.

Return `H|H|P_r` through the completed tape and selected motif.  Keep
`Q_q,R_r` fixed.  Reunite `P_r|D_r=C_r`, reverse its simple code path to
the exact raw spare pair, reverse every selected-support `M -> B`, restore
all gap trails, return the temporary cart to its exact source support, and
reverse its bootstrap.  During every strict teardown state:

* `Q_q` still gives the atom branch;
* `R_r` gives the collar order and task/teardown phase; and
* the currently literal code, cart, or restored raw prefix gives the local
  reverse microstep.

Do **not** change `Q_q` merely because the code pair has become raw.  First
finish the entire motif teardown.  At the resulting checkpoint, the exact
raw selected motif and the deterministic selector recover `q` without the
register, while `R_r` still recovers `r`.

Now put

\[
                     T_0=Q_0,\qquad T_1=Q_1,
                     \qquad T_2=Q_2.                  \tag{6.2}
\]

Traverse a simple route in the protected register graph

\[
 Q_0\leftrightarrow Q_1,\qquad
 Q_0\leftrightarrow111\leftrightarrow Q_2,\qquad
 Q_2\leftrightarrow Q_3                               \tag{6.3}
\]

from the current `Q_q` to `T_r`, while the raw motif and `R_r` are both
literal.  This is the safe late handoff: the raw motif is now the old copy
of `q`, and `R_r` is the old copy of `r`.  Finally hold `T_r` and use a
simple mass-four collar path

\[
\begin{array}{c|l}
R_0&0202,\\
R_1&0211\to0202,\\
R_2&1102\to0202.
\end{array}                                             \tag{6.4}
\]

At (6.4), `T_r` independently selects the endpoint branch.  The temporary
cart and both odd code blocks are already raw, so the resulting fixed-berth
`H|H` is the permanent pre-head required downstream.

### Lemma 6.1 (no erased datum)

At every checkpoint and strict state from code writing through (6.4), the
pair `(q,r)` has two independent literal decoders, one for each coordinate.

#### Proof

The complete record schedule is:

\[
\begin{array}{c|c|c}
\hbox{phase}&q\hbox{ record}&r\hbox{ record}\\ \hline
\hbox{code write and cart preposition}&Q_q&K\\
\hbox{task macro state}&Q_q&P_r\hbox{ and }D_r\\
\hbox{pilot-active local path}&Q_q&D_r\hbox{ or }\bar D_r\\
\hbox{six-coordinate rotation}&Q_q&P_r\\
\hbox{guarded collar regeneration}&Q_q&D_r\\
\hbox{delimiter crossing}&Q_q&S_r\\
\hbox{reverse work teardown}&Q_q&R_r\\
\hbox{late register handoff}&\hbox{raw motif}&R_r\\
\hbox{final collar path}&\hbox{raw motif}&T_r.
\end{array}                                             \tag{6.5}
\]

The first-visit phase record of Section 4 and completed tickets supplement
this table with global time.  Every record is changed only while its old
value and the datum it represents are literal elsewhere.  Hence neither
`q` nor `r` is absent at any join. \(\square\)

## 7. Candidate theorem, resource audit, and exact scope

### Theorem 7.1 (projection-coded atom/order handoff; candidate)

Conditional on the already proved clean zero-charge motif selection and
the scalar/task carrier theorems, the schedule in Sections 2--6:

1. uses the same disjoint mass-four spare pair and no new support;
2. keeps the three-valued atom branch in `Q_q` through every task and every
   strict reverse-setup state;
3. stores the collar order in each projection of the odd pair;
4. separates cart prepositioning from the first task, including the
   zero-task and extreme-collar rows;
5. restores every task corridor and the exact raw selected motif; and
6. transfers the collar order to the protected register before writing the
   permanent fixed-berth `H|H`.

Every nonzero code, train, task, phase-collar, and retirement edge lies in
the reserved work suffix after `p_1`; the register edges are the already
protected root/boundary edges (6.3).  Thus the audited fixed-row directed
lift applies edge by edge without changing the selected first row.

The length threshold is unchanged from clean selection:

\[
                         m-3\ge64,
                 \qquad k=2m-1\ge133.                 \tag{7.1}
\]

No claim is made below this threshold.

The additional persistent atom-tag cost is **zero**: the old atom register
is retained rather than overwritten, and the already reserved pair takes
over the order datum.  If one insists on overwriting `Q_q` before the raw
motif returns, any replacement atom tag must have at least three literal
states, because the branches `q=0,1,3` can occur with the same later collar
order.  A binary tag is therefore information-theoretically insufficient.

This theorem is not frozen as proved here.  An independent audit must still
match translated full states across all code-writing paths, all three
variable-pilot path tables, the both-code-active delimiter crossing, the
first-visit phase paths, guarded collar regeneration, and the reverse
private-gap teardown.  Failure of any one of those rows leaves the
proof-safe frontier at `ACT4`; it does not justify reverting to the
noninjective `widehat Q_(q,r)` table.
