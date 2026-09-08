# Odd APH: recorded-motif crossing and temporary-cart retirement

**Date:** 2026-08-06  
**Scope:** the final bounded interface after the clean zero-charge origin
motif, residual carrier, and `G_1` substitution theorems  
**Method:** literal block permutations through a recorded interval of length
at most thirteen, zero-edge head reparsing, and copy-before-erase at the
collar; no computation or search  
**Status:** **SUPERSEDED / DO NOT CITE.**  The independent work-level audit
found that Lemma 2.1 is false: with motif `B|H|A` and train `H|A`, the macro
word `B|H|A|H|A` is reached at two different crossing counts.  The `B/M`
strict routes also lacked a persistent branch bit.  The collar normalization
in (3.1) is valid, but the crossing theorem is not.  The piloted replacement
is stated separately in
`MATH_THEOREM_ODD_APH_ODD_PILOT_TRAIN_AND_RETIREMENT_20260806.md`.

## 1. Recorded motif normal form

The clean selection theorem leaves one bounded interval `I` with

\[
                              |I|\le13.              \tag{1.1}

\]

Its persistent origin word is one of

\[
                   O_0=H|B,\qquad
                   O_1=B|H,\qquad
                   O_2=H|M,                         \tag{1.2}

\]

at a declared berth and side of the temporary-cart origin.  The remaining
blocks of `I` belong to `{A,B,C,M}`.  Their physical gap lengths and
orientations, together with the early atom register, recover the complete
raw source motif.  In particular every code head in (1.2) is adjacent to a
literal nonhead delimiter `D in {B,M}`.

The mobile objects which cross `I` are of two kinds:

\[
                       H|H,
          \qquad       P|H\ \hbox{ or }\ H|P,        \tag{1.3}

\]

where `P` is the returned payload of a residual or zipper task.  Their
length is always two.

## 2. Literal train crossing

For a nonhead motif block `Y`, move a right-going train `H|P` through it by

\[
             H|P|Y\leadsto H|Y|P\leadsto Y|H|P.     \tag{2.1}

\]

The first interchange keeps the train head fixed.  At the second
interchange the payload is fixed, while the already crossed motif prefix and
the recorded delimiter in (1.2) locate the active boundary.  The reflected
path treats a left-going train and the orientation `P|H`.

For a motif head, use

\[
                         H|P|H\leadsto H|H|P.         \tag{2.2}

\]

Only the interchange `P|H -> H|P` is nontrivial; the other interchange of
the two identical heads is a zero-edge reparse.  The sweep direction and
the adjacent code delimiter `D` decide which member of the resulting head
run is the motif head and which is the train head.  Thus (2.2) neither
creates a duplicate graph vertex nor loses the code parse.

For the double cart, the corresponding crossing of a motif head is the
identity

\[
                              HH|H=H|HH.              \tag{2.3}

\]

Suppress that duplicate macro checkpoint.  A nonhead motif block is crossed
by the proved two-swap double-head transport, one head fixed at each swap.

### Lemma 2.1 (bounded crossing decoder)

Let a train in (1.3) cross `I` monotonically by (2.1)--(2.3).  At every
macro and strict state, the full state recovers:

1. the source motif and its cart berth;
2. the collar-order class `r`;
3. the train direction, payload, and number of completed motif blocks; and
4. the current local microstep.

#### Proof

At a macro checkpoint the motif word is split into an already crossed prefix
and an untouched suffix, with the visible train at their common boundary.
Apply the inverse block permutation to concatenate those two pieces.  The
result is the normal form of Section 1, which recovers the source motif and
`r`.

At the first strict swap in (2.1), the train head remains literal.  At the
second, the literal payload is immediately beside the active window and the
already crossed prefix fixes its other boundary.  Local mass and the global
task branch give the ordered endpoint type; simplicity gives the microstep.
Equation (2.2) has the same decoder, with the fixed delimiter `D` separating
the code parse from the train parse.  Equation (2.3) has no strict state.

Different source motifs cannot meet: reversing the completed block
permutations at a purported common state would give the same normal form in
Section 1.  The clean-origin theorem then gives the same source. \(\square\)

### Corollary 2.2 (out-and-back restoration)

If a double cart crosses `I` on its outward task sweep and a length-two
return train crosses `I` in the reverse direction, every motif block returns
to its original physical address and value.

#### Proof

At the macro level both moves are inverse permutations of a length-two train
and the word `I`; the internal train values do not affect that permutation.
Every nonhead block is moved two positions out and two positions back.
Identical-head crossings use only the reparses (2.2)--(2.3).  Reversing the
list of crossed motif blocks therefore restores the exact word.  Lemma 2.1
gives the decoder throughout. \(\square\)

This corollary supplies the protected-support qualifier in the
farthest-first residual theorem and in the variable-mass zipper theorem.

## 3. Return the temporary cart to its origin

After all remote tasks, the temporary cart has again been regenerated at
the collar side and the persistent motif is in its original coded normal
form.  The task schedule says only that the current two-block collar state
`K_f` has mass four.  It does **not** yet say that `K_f` is the desired
order record.  While the persistent endpoint `O_r` is still literal, freeze
the regenerated cart and choose a simple path in the mass-four collar layer

\[
                              K_f\leadsto R_r,
 \qquad R_0=H|H,\quad R_1=H|M,\quad R_2=M|H.        \tag{3.1}
\]

The fixed cart guards every strict state, and `O_r` gives `r`.  The
completed labelled task tape and the fixed zipper address determine `K_f`;
simplicity of the chosen path determines its microstep.  Thus (3.1) is a
source-disjoint normalization, not an appeal to collar mass alone.

Now keep `R_r` literal and move the cart back through the completed task
tape.  Ordinary blocks are crossed by double-head transport, and each
recorded motif block is crossed by Lemma 2.1.  The final crossing puts the
cart at the declared source berth and the code at the teardown parse which
is the reverse of its setup parse.

### Lemma 3.1 (motif retirement)

While the collar record remains fixed, reverse the code route and the cart
atom bootstrap.  The endpoint is the exact raw source motif, and the paths
are pairwise source disjoint.

#### Proof

The code endpoint `O_r`, its declared side, every `M` gap, and the returned
cart recover the setup branch before any reverse edge is taken.  Reverse the
chosen simple `V_4` code path, then reverse the bounded block permutations
which gathered the unused opposite pair.  At each strict state the returned
cart has a literal fixed head.  Finally reverse the transition-atom or
neutral-atom bootstrap.

The fixed collar record retains `r`; the code/gap normal form retains the
source motif until the literal source blocks reappear.  Erase a code item
only after the corresponding source item is literal.  This is
copy-before-erase at every subphase, so two source paths cannot meet.
\(\square\)

The temporary cart is now gone and the complete selected zero-charge motif
is raw again.  Every residual `M` and the zipper target remain at their
labelled addresses, as required by the pre-head checkpoint.

## 4. Write the permanent collar head

Use the mass-four collar records

\[
                         R_0=H|H,\qquad
                         R_1=H|M,\qquad
                         R_2=M|H.                   \tag{4.1}

\]

Before changing `R_r`, copy `r` into the protected root/boundary register.
The literal raw source motif and `R_r` label that register route.  Then keep
the register fixed and use a simple path in `V_4` from `R_r` to `H|H` at the
source-independent collar berth.

### Lemma 4.1 (permanent-head copy schedule)

The route in Section 4 is source disjoint and leaves a literal permanent
`H|H` while preserving the selected `p_1` row.

#### Proof

While the register is written, `R_r` is literal.  Afterward the register is
an injective copy of `r`.  It labels every strict state of the chosen simple
mass-four collar path.  The source motif is already raw, so it labels
retirement of the old atom-phase meaning of the register.  All register and
collar edges have the existing fixed-row directed lift. \(\square\)

## 5. The complete bounded interface

### Theorem 5.1 (recorded motif crossing and retirement)

For every clean cart/code motif furnished by the length-64 selection theorem:

1. every residual or zipper carrier crosses the complete motif and restores
   it after the task;
2. the final mass-four collar is normalized to `R_r` while `O_r` is still
   literal;
3. the temporary cart returns to its source support after all tasks;
4. the exact raw source motif is restored;
5. the collar order is copied before the temporary code is erased; and
6. a literal source-independent permanent `H|H` is written at the fixed
   collar berth.

Every path is occurrence labelled and directed under the fixed `p_1` row,
and no permanent fixed-head theorem is invoked before item 5.

#### Proof

Item 1 is Lemma 2.1 and Corollary 2.2.  Item 2 is (3.1).  Items 3--4 are
Lemma 3.1.  Items 5--6 are Lemma 4.1.  Their information records overlap in
copy-before-erase order, so concatenation introduces no unlabelled
checkpoint. \(\square\)

The motif family is explicitly finite.  There is one `BBBB` branch; in the
four-extreme branch there are six balanced binary orders and three `B` gaps
of lengths `0,1,2,3`.  Thus at most

\[
                              1+6\cdot4^3=385         \tag{5.1}

\]

source motif modes occur before the three collar-order classes.  The literal
normal form, rather than an anonymous 1,155-state register, stores that
mode.  One crossing has at most thirteen block steps and two local swaps per
step.  This is an absolute finite-state interface, not a growing tape
compiler.
