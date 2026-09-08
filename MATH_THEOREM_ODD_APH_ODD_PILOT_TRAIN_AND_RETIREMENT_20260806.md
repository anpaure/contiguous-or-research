# Odd APH: an odd pilot gives a simple train and retires the temporary cart

**Date:** 2026-08-06  
**Scope:** the work-level interface left after the clean zero-charge motif,
farthest-first residual carrier, and variable-mass `G_1` substitution  
**Method:** one moving odd-mass pilot, one restored odd-mass origin delimiter,
literal two-state branch tags, and copy-before-erase; no computation or
search  
**Status:** candidate replacement, pending the independent work-level audit.
It starts from the piloted normal form in
`MATH_THEOREM_ODD_APH_CLEAN_ZERO_CHARGE_ORIGIN_CODE_SELECTION_20260806.md`
and does not cite the false two-block crossing lemma in
`MATH_THEOREM_ODD_APH_RECORDED_MOTIF_CROSSING_AND_RETIREMENT_20260806.md`.

## 1. The two odd blocks

Put

\[
 A=00,\quad B=20,\quad C=22,\quad
 H=02,\quad M=11,
 \qquad P=01,\quad \bar P=10,\quad
 D=21,\quad \bar D=12.                               \tag{1.1}
\]

The ordinary, midpoint, and head blocks have even masses

\[
 0,2,4,2,2,                                             \tag{1.2}
\]

whereas `P,bar P` have mass one and `D` has mass three.  Moreover

\[
              \operatorname{mass}(P|D)=4,
 \qquad P\leftrightarrow\bar P,
 \qquad D\leftrightarrow\bar D,
 \qquad H\leftrightarrow M                           \tag{1.3}
\]

are literal fixed-mass code moves.  The clean motif theorem produces:

1. an origin delimiter `D` at a declared address in a source-injective
   interval of length at most thirteen, restored to that address after every
   completed out-and-back visit;
2. a protected final atom state `Q_q`, `q in {0,1,3}`, while the ordered
   source collar is still literal;
3. a mobile train whose pilot is `P`; and
4. only even-mass ordinary or midpoint blocks between successive visits to
   the selected motif, apart from the one named zipper block at its fixed
   decoded address.

The zipper block is a task endpoint, never a crossed background block.  In
particular the aligned block `01` occurs exactly once on every corridor to
which the pilot-position argument below is applied: it is the train tail.
The aligned block `21` occurs exactly once in the selected motif normal
form: it is the declared origin delimiter.  During the one step in which a
train crosses `D`, its current position and the inverse completed
permutation recover that declared address.  The protected register is on a
different root/boundary coordinate support and is not parsed on this work
block lattice.

### 1.1 Exact source of the mass-four pilot pair

No collar or task mass is used to create `P|D`.  In the `BBBB` selection
branch, the first `BB` is the cart atom and the disjoint second `BB` is
routed to `P|D`.  In the four-extreme branch, one unlike extreme pair is the
cart atom and the two unused extremes are a disjoint `A,C` pair of mass
four; that pair is routed to `P|D`.  Thus the cart source and pilot source
are disjoint in both branches.  The entire selected support is deleted
before the residual bank is chosen, so no residual task uses either source
occurrence.  The collar and the named zipper block lie outside this support.

The lifecycle is therefore

\[
 \text{raw spare pair}\longrightarrow P|D
 \longrightarrow (H|H|P)\;\hbox{ plus origin }D
 \longrightarrow P|D\longrightarrow\text{the same raw spare pair}. \tag{1.5}
\]

At no checkpoint is the pair also counted as a collar, task, or cart-mass
resource.

### 1.2 Exact source and phase-changing lifecycle of the `Q` register

The register is the protected root/boundary register of
`MATH_THEOREM_ODD_APH_EARLY_FOUR_STATE_ATOM_RECORD_20260806.md`, with

\[
 Q_0=021,\quad Q_1=012,\quad Q_2=201,\quad Q_3=210.                 \tag{1.6}
\]

Its literal connecting paths are

\[
 Q_0\leftrightarrow Q_1,\qquad
 Q_0\leftrightarrow111\leftrightarrow Q_2,\qquad
 Q_2\leftrightarrow Q_3.                                          \tag{1.7}
\]

It is disjoint from `p_1`, the work suffix, the selected motif, and the
collar.  The clean theorem has already completed the private `Q_2` phase, so
the departure sweep uses one final atom state

\[
              Q_q,\qquad q\in\{0,1,3\}.              \tag{1.8}
\]

Keep `Q_q` and the source collar literal while `H|H|P` moves from the motif
to the collar.  At the collar, the complete piloted-departure normal form
is an injective copy of the atom datum.  Now encode the collar order `r` by
the following endpoint, deliberately excluding the old state `Q_q`:

\[
\begin{array}{c|ccc}
q\backslash r&0&1&2\\ \hline
0&Q_1&Q_2&Q_3\\
1&Q_0&Q_2&Q_3\\
3&Q_0&Q_1&Q_2.
\end{array}                                           \tag{1.9}
\]

Call it `widehat Q_(q,r)`.  Given the source-injective origin normal form,
`q` is known, so each row of (1.9) recovers `r`.  Traverse a simple route in
(1.7) from `Q_q` to `widehat Q_(q,r)` while the cart and source collar are
literal.  The route is nonempty in every row.  Hence it simultaneously
copies the atom datum out of the register, copies the collar order into it,
and writes a mandatory setup/task phase change.  Hold `widehat Q_(q,r)`
literally through every task, collar normalization, and motif teardown; it
labels the final route (5.2).

### Lemma 1.1 (setup and reverse-setup decoder)

The complete route from the raw selected motif to the collar checkpoint
`H|H|P` plus `D,widehat Q_(q,r)`, and its late reverse work route, are
pairwise source disjoint.

#### Proof

The cart atom and spare pair are disjoint by Section 1.1.  Until `P|D` is
literal, the early atom state in (1.6), the source collar, and the stationary
`H|H` cart label every bounded gathering and fixed-mass code path.  At the
`P|D` endpoint, the declared berth side, the `M` gap trails, the cart
address, and the interval geometry recover the four raw extreme addresses
and every intervening `B`; in the neutral branch the literal order
`H|H|P|D` recovers `BBBB`.  Thus this work normal form is injective before
the register changes.

Move `P` to the train tail by a fixed bounded sequence while `H|H,D,Q_q`
and the source collar are literal.  Each strict local path is simple, and
its literal sentinels and declared subphase recover its endpoints.  Move the
piloted cart to the collar with `Q_q` fixed.  There traverse the nonempty
route (1.9); afterward `widehat Q_(q,r)` retains both the task phase and the
collar order, while the work normal form retains the motif source.

For teardown, reverse only the work operations in the opposite order; the
register remains at `widehat Q_(q,r)`.  Keep `R_r,widehat Q_(q,r)` literal
until `P|D`, the cart, every gap trail, and finally every raw source block
have reappeared.  The origin normal form recovers `q`, so (1.9) still
recovers `r` and the atom branch.  Hence each datum has an old or new literal
copy at every checkpoint, and equality of two full states forces the same
source and microstep. \(\square\)

At every completed crossing checkpoint the pilot is `P`.  The alternate
value `bar P` is not needed in the crossing path; it remains available as a
literal forbidden-state check.

The three train types are

\[
       H|H|P,\qquad H|X|P,\qquad Z|H|P,              \tag{1.4}
\]

where `X in {A,C}` and, on a nonzero zipper task, `Z in {A,C}`.  The
`Z=H` row is the zero-change `G_1` task and is omitted.  Thus every train has
exactly one odd pilot and at least one literal head, and the double-head cart
is not confused with a nontrivial return train.

## 2. One piloted block crossing

Write a right-going train as `U|V|P` and let
`Y in {A,B,C,M,D}` be the next crossed block.  No completed pre-head task
leaves an `H` in the background.  Use only two local phases:

\[
 U|V|P|Y
   \leadsto U|V|Y|P
   \leadsto Y|U|V|P.                                  \tag{2.1}
\]

The first arrow uses the following literal tail-clean paths on `P|Y`:

\[
\begin{array}{c|l}
Y& P|Y\leadsto Y|P\\ \hline
A&0100\to0010\to0001\\
B&0120\to1020\to1110\to2010\to2001\\
M&0111\to1011\to1101\\
C&0122\to1022\to1112\to2012\to2021\to2111\to2201\\
D&0121\to1021\to1111\to2011\to2101.
\end{array}                                           \tag{2.2}
\]

Every arrow in (2.2) is one adjacent unit transfer.  The `B` and `M` rows
are vertex disjoint despite their equal mass.  More importantly, no strict
state in any row has its right two-coordinate block equal to `P=01`; that
literal tail appears only at the endpoint, and no strict state contains an
aligned `H=02`.  Thus the unchanged `U,V` contain every literal head during
the first phase and locate the active boundary.

For the second arrow of (2.1), keep that endpoint pilot `P` fixed and choose
one simple path in the six-coordinate fixed-mass layer

\[
                         U|V|Y\leadsto Y|U|V.          \tag{2.3}
\]

This layer is nonextreme because every train in (1.4) contributes a literal
`H` to its endpoint.  Equation (2.3) is one simple path, not two successive
block swaps.  This removes the exact repeated state
`H|M|H|P` which occurs if the rotation is incorrectly decomposed into an
`H|B` swap followed by a second `H|B` swap.

The sole equal-mass pair `B/M` receives a literal external branch bit before
(2.3) is selected.

* In an ordinary residual corridor every crossed mass-two block is raw `B`;
  the farthest-first invariant excludes old `M` tickets.
* In the selected support every source `B` was normalized to `M`.  After the
  tail-clean row (2.2), while that `M` is literal, change the separate origin
  delimiter `D=21` to `bar D=12`.  Hold `bar D` through (2.3), then restore
  `D` while the crossed `M` is again literal.  For a raw `B`, keep `D`
  unchanged.  The protected `Q` state and the still-literal `M` make both
  delimiter moves copy-before-erase.  Normalize `D` before the train crosses
  the delimiter itself.
* In the sole dirty `G_1` corridor, retain the literal mass-two/mass-six
  collar toggle from Section 3 of the variable-mass `G_1` theorem: write its
  `M` state while the unique recorded ticket is active, hold it through
  (2.3), and restore it afterward.  The same rule handles a completed
  residual ticket on the final cart return.  There the final collar has mass
  four and `widehat Q_(q,r)` retains its order.  Such a ticket is never
  crossed while the collar is extreme: farthest-first residual sweeps
  exclude old tickets, and each exceptional `G_1` row first moves collar
  mass from zero or eight to two or six.

Thus the full state contains `D/bar D` or the collar toggle throughout every
ambiguous six-coordinate route.  Restore either tag before the next block
crossing or collar update.

For a left-going train keep the same physical order `U|V|P` and use the two
phases in the opposite order,

\[
 Y|U|V|P\leadsto U|V|Y|P\leadsto U|V|P|Y.            \tag{2.4}
\]

Use the reflected six-coordinate path for the first arrow and the reflected
tail-clean row for the second.  Thus the heads remain adjacent to a task
approached from the collar side, and no train-orientation conversion is
hidden at either endpoint.

### Lemma 2.1 (strict-state decoder)

Every macro and strict state in (2.1)--(2.3) recovers the source, train
type, direction, crossed-block value, local phase, and microstep.

#### Proof

At a macro checkpoint, `D` and the inverse completed block permutation give
the declared origin address.  The protected `Q` state gives the atom/setup
phase or the pair `(q,r)`, and the unique moving `P` gives the train tail and
boundary.  The deterministic task order, its literal `M` or zipper ticket,
and the already restored prefix give `U,V,Y` and the direction.

In a strict state of (2.2), `U,V` remain literal and contain at least one
head, while the tail is not `P`.  The five displayed routes, including the
two equal-mass rows, are pairwise endpoint-typed and simple.  In a strict
state of (2.3), the literal tail is `P`.  The task/ticket phase fixes the
ordered train pair `U,V`.  Subtracting its known mass from the invariant
six-coordinate mass gives `mass(Y)`.  The values `A,B,C,D` have masses
`0,2,4,3`; the sole remaining equality is `B/M`, resolved by the normal-form
delimiter or collar toggle stated above.  Thus the ordered endpoint of (2.3) is
recovered *before* its simple path is inverted, and simplicity then gives
the microstep.  Consequently paths chosen for different endpoint types may
intersect in their six-coordinate projection only when their unchanged
ticket/class records differ in the full state.  A strict state cannot belong
to both phases, and two full states in one phase agree only when their
source, direction, endpoint type, and microstep agree. \(\square\)

## 3. The pilot eliminates the commuting-word collision

The invalid two-block train had no physical occurrence label.  For example,
`H|A` could pass the identical motif factor `H|A` and return to the same
graph vertex after a nonempty closed walk.  The odd pilot makes that
impossible.

### Lemma 3.1 (strict pilot progress)

During a monotone sweep through the selected motif, no two distinct macro
checkpoints are the same graph vertex.

#### Proof

At every macro checkpoint the train contains the literal block `P=01`.
Every crossed raw, midpoint, or head block has even mass, while the only
other odd block in the selected support is the distinct value `D=21`.
In one macro step (2.1), the physical position of `P` advances by exactly one
block in the sweep direction.  When `P` crosses `D`, the two distinct odd
values exchange positions, so that step is visible as well.  Consequently
equality of two macro words would force the same physical `P` position and
hence the same completed crossing count. \(\square\)

The lemma is deliberately a graph-state statement; it does not assign
particle identities to equal even blocks.  The pilot value itself is
literal and moves to a different coordinate pair at every nonzero macro
step.

### Lemma 3.2 (setup/task/teardown phase separation)

No cart sweep used to preposition the pilot at the collar is revisited by a
task or teardown sweep.

#### Proof

The prepositioning sweep holds `Q_q`.  Before the first task begins, (1.9)
writes `widehat Q_(q,r) != Q_q`; every task and the complete teardown hold
that new state.  Hence even a geometric reversal of the prepositioning
route is a disjoint full-state route.

After task `i`, its literal target ticket remains at its labelled address.
Thus the set of completed tickets distinguishes successive task sweeps.  On
the final return every nonzero task target is already literal, whereas on
its earlier outward sweep its own source was still literal.  If there are
no nonzero tasks, the mandatory register change alone separates the final
return from prepositioning. \(\square\)

### Corollary 3.3 (piloted interval crossing)

A train in (1.4) crosses any part of the selected interval, and returns
through it, by a simple occurrence-labelled directed path.  The return
sweep restores every crossed block to its exact physical address and value.

#### Proof

Use Lemma 2.1 inside each block step and Lemma 3.1 between steps.  If a
strict local state met an earlier state, Lemma 2.1 would give the same local
subphase and macro boundary, contradicting either simplicity of the local
path or Lemma 3.1.  The reverse sweep applies the inverse three-block
permutation to the same list of blocks in reverse order.  Its endpoints
therefore restore the interval literally.  The fixed-row directed-lift
theorem orients every nonzero work edge after `p_1`.  Lemma 3.2 separates
different global visits. \(\square\)

## 4. Tensoring the pilot with the four task substitutions

The pilot never pays task mass.  Append it to the carrier constructions as
follows.

For a residual task, replace the old local display by

\[
 X|H_1|H_2|P
   \leadsto M|H_2|X|P.                               \tag{4.1}
\]

The three operations of the residual theorem act only on `X,H_1,H_2`; hold
`P` fixed.  The return train is `H_2|X|P`.

\[
 H_2|X|P|K_i\leadsto H_2|H|P|K_{i+1}.               \tag{4.2}
\]

Keep the returned `H_2` fixed and choose one simple path on the eight
coordinates `X|P|K_i -> H|P|K_(i+1)`.  Its mass identity is the old collar
identity with `mass(P)=1` added to both sides.  At the endpoint the pilot is
a literal separator between the regenerated cart and the collar:
`H|H|P|K_(i+1)`.  The outside returned head, the task ticket, and the
protected `Q` state recover the ordered endpoints of the simple path and
therefore its strict microstep.

For the zipper task use

\[
 X|H_1|H_2|P
   \leadsto X'|Z_d|H_2|P.                            \tag{4.3}
\]

Again `P` is fixed.  At the task ticket, interchange `Z_d|H_2` once while
`P` and `X'` are literal, producing the normalized return train
`H_2|Z_d|P`.  At the collar use

\[
 H_2|Z_d|P|K\leadsto H_2|H|P|K'.                    \tag{4.4}
\]

As in (4.2), keep `H_2` fixed and use one simple eight-coordinate path on
`Z_d|P|K -> H|P|K'`.  Equations (4.1)--(4.4) have exactly the mass identities
already proved in the residual and `G_1` theorems, with the unchanged pilot
mass on both sides.  The pilot changes neither the capacity schedule nor the
farthest-first ticket invariant.  Its endpoint position prevents the
temporary cart from merging with a collar record `R_0=H|H`.

### Theorem 4.1 (piloted four-task escort)

The capacity-safe order from the variable-mass `G_1` theorem realizes all
at most four tasks with a regenerated `H|H|P` after each task.  Every raw
corridor, completed `M` ticket, and crossing of the bounded origin support
has an occurrence decoder.

#### Proof

On a raw corridor, the odd pilot is an additional literal occurrence label;
the ticket-prefix proofs of the two task theorems apply with `P` tensored
through every local path.  If a task sweep crosses the selected support,
use Corollary 3.3 and restore it before continuing.  The only dirty
equal-mass row is `B/M`, which carries the literal delimiter or collar tag
through (2.3).
Equations
(4.1)--(4.4) regenerate the carrier, and the prior sign-order proof gives a
final collar mass of four. \(\square\)

## 5. Normalize the collar and retire the pilot

Let `K_f` be the final two-block collar.  Theorem 4.1 gives only
`mass(K_f)=4`.  While `widehat Q_(q,r)` and the regenerated `H|H|P` are
literal, choose a simple path

\[
 K_f\leadsto R_r,
 \qquad R_0=H|H,\quad R_1=H|M,\quad R_2=M|H.          \tag{5.1}
\]

The fixed train guards its strict states, `widehat Q_(q,r)` gives the
endpoint branch, and the completed labelled task tape determines `K_f`.
This is the missing order normalization; mass four alone is not used as a
decoder.

Keep `widehat Q_(q,r)` fixed and keep the collar at `R_r` at every return
macro checkpoint.  At a labelled `M` ticket, the temporary same-mass branch
toggle described after (2.3) may leave `R_r` for one local path and is
restored before the next block crossing.  Return `H|H|P` through the
completed task tape and the selected interval, using Corollary 3.3.  The
inverse departure sweep puts `H|H` at its source atom and reunites `P|D` at
the declared code berth.  Reverse the selected-support `M -> B`
normalization, the simple `P|D` code path, the bounded gathering
permutations, the private `M`-gap motion when present, and the transition or
neutral atom bootstrap.  During that late private-gap motion the unused
opposite pair and every exterior gap are already raw; together with
`R_r,widehat Q_(q,r)` they replace the old `Q_2/Q_3` phase label and recover
the unique atom branch and teardown direction.  The endpoint is the exact
raw zero-charge source motif.  Throughout this teardown,
`R_r,widehat Q_(q,r)` retain the collar order; `P|D` plus the returned cart
retains the motif source until each raw source block is literal.

Finally keep `widehat Q_(q,r)` fixed and traverse a simple mass-four collar
path

\[
                              R_r\leadsto H|H.         \tag{5.2}
\]

The endpoint is a literal source-independent permanent head at the fixed
collar berth.  The temporary cart and both odd code blocks have already
been restored to raw source values, so there is no temporary/permanent
`HHHH` coexistence checkpoint.

### Theorem 5.1 (piloted retirement)

Starting from the clean length-64 motif normal form, the complete pre-head
schedule:

1. writes the restored origin delimiter and moving pilot before the cart
   leaves;
2. copies the ordered source collar into `widehat Q_(q,r)` before changing
   the collar;
3. executes and source-decodes all residual and zipper tasks;
4. normalizes the final mass-four collar to `R_r`;
5. restores the exact raw motif and retires the temporary pilot/cart; and
6. writes a permanent fixed-berth `H|H`.

No theorem whose premise is a source-independent fixed head is invoked
before item 6.

#### Proof

The clean motif theorem gives item 1, and Sections 1.2--3 give item 2.
Theorem 4.1 gives item 3.
Equation (5.1) gives item 4.  Corollary 3.3 and the reverse setup paths give
item 5.  Equation (5.2) gives item 6.  At each join the old and new records
are simultaneously literal, so the individual occurrence decoders
concatenate without an information-free checkpoint. \(\square\)

## 6. Exact scope

The pilot changes no length threshold.  The clean selection theorem requires
reserved work length at least `64`, hence

\[
                         m\ge67,
                 \qquad k=2m-1\ge133.                \tag{6.1}
\]

The theorem is asymptotic only at this explicit threshold.  It makes no
claim for the finitely many odd values `k<133`, and it uses no finite search
to cover them.
