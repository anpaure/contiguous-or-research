# Odd APH: a clean zero-charge cart-and-code motif exists locally

**Date:** 2026-08-06  
**Scope:** joint selection of the temporary cart atom and its persistent
piloted origin code before the residual bank is chosen  
**Method:** a signed sliding four-extreme window, a `BBBB` alternative, and
copy-before-erase under a stationary `H|H`; no computation or search  
**Status:** unconditional for reserved work words of length at least 64 and
imbalance at most three.  The selected support has zero signed charge, so
the later residual bound remains `t<=3` and is automatically disjoint from
the code.

## 1. Why a fixed preselected atom has no bounded halo

There is no universal bounded-radius aperture theorem around an arbitrary
already selected atom.  For `N>=2`, consider the balanced word

\[
                         A^N C A^N C^{2N-1}.          \tag{1.1}
\]

If the first displayed transition `A|C` is chosen as the cart atom, the
blocks immediately outside it are both `A`; the nearest remaining `C` is at
distance `N`.  There are no residual tasks after deleting that zero-charge
atom, so task avoidance does not repair the distance.  Thus locality must be
obtained by choosing the cart atom and code support jointly.

## 2. A balanced four-extreme window

Let `w` be a linear word over `{A,B,C}` and assume

\[
                         |#A(w)-#C(w)|\le3.           \tag{2.1}
\]

Delete the `B` blocks and write the resulting extreme word as

\[
                         e_1e_2\cdots e_E,
                  \qquad e_i\in\{A,C\}.             \tag{2.2}
\]

Encode `A` by `-1` and `C` by `+1`, writing the resulting signs as `z_i`.

### Lemma 2.1 (sliding four-window lemma)

If `E>=16`, four consecutive vertices of (2.2) contain exactly two `A`'s
and two `C`'s.

#### Proof

Suppose no four-window is balanced.  Put

\[
                         W_j=z_j+z_{j+1}+z_{j+2}+z_{j+3}.
                                                               \tag{2.3}
\]

Every `W_j` belongs to `{-4,-2,2,4}`.  Consecutive values differ by

\[
                         W_{j+1}-W_j=z_{j+4}-z_j
                                  \in\{-2,0,2\}.      \tag{2.4}
\]

They therefore cannot change sign without taking the forbidden value zero.
All `W_j` have one sign, and hence

\[
             \left|\sum_{j=1}^{E-3}W_j\right|\ge2(E-3).        \tag{2.5}
\]

In the sum on the left, an interior `z_i` has coefficient four; the six
boundary coefficient deficits are `3,2,1,1,2,3`.  Consequently

\[
 \left|\sum_jW_j\right|
   \le4\left|\sum_i z_i\right|+12
   \le24                                                   \tag{2.6}
\]

by (2.1).  Equations (2.5)--(2.6) give `E<=15`, a contradiction. \(\square\)

## 3. The local zero-charge motif

### Theorem 3.1 (clean motif dichotomy)

If `w` satisfies (2.1) and `|w|>=64`, then `w` contains one of the following
zero-charge supports.

1. Four consecutive neutral blocks `BBBB`.
2. A physical interval of at most thirteen blocks whose four retained
   extreme vertices contain two `A`'s and two `C`'s.

#### Proof

If a `B` run has length at least four, outcome 1 holds.  Assume every `B`
run has length at most three.

There are at most `E+1` linear `B` runs.  If `E<=15`, then

\[
                         |w|\le E+3(E+1)
                                  \le63,             \tag{3.1}
\]

contrary to the hypothesis.  Hence `E>=16`.  Lemma 2.1 supplies four
consecutive extremes with two of each sign.  Their three intervening `B`
gaps have length at most three, so their complete physical span has length
at most

\[
                              4+3+3+3=13.             \tag{3.2}
\]

The support has zero signed charge because its extreme multiset is
`{A,A,C,C}`; all intervening `B` blocks are neutral. \(\square\)

The constants are deliberately elementary.  No claim of sharpness is
needed for the asymptotic odd transition.

## 4. Literal cart, moving pilot, and stationary delimiter

Retain

\[
 H=02,\qquad M=11,\qquad
 P=01,\qquad \bar P=10,\qquad D=21.                 \tag{4.1}
\]

The two new code blocks have odd masses one and three, respectively, and

\[
                         \operatorname{mass}(P|D)=4. \tag{4.2}
\]

Thus either spare zero-charge pair may be routed to `P|D` without borrowing
mass from the collar.  The block `P` will travel with the temporary cart;
`D` remains at the declared origin berth.  Since the raw and midpoint
alphabets `{A,B,C,M,H}` have even block mass, both odd blocks are literal
delimiters.  The alternate orientation `bar P` has the same mass as `P` and
is reserved as a strict-state check; the final tail-clean crossing does not
need to occupy it persistently.

Use the following literal routes for the three possible spare sources:

\[
\begin{array}{c|l}
BB&2020\to2011\to2002\to1102\to1111\to0211\to0121,\\
AC&0022\to0112\to0121,\\
CA&2200\to2110\to2020\to2011\to2002\to1102
       \to1111\to0211\to0121.
\end{array}                                           \tag{4.2a}
\]

Every arrow is one adjacent unit transfer, and no strict state is
`H|H=0202`.  Thus a fixed cart beside the route never merges with an active
second cart into an unparsed `HHHH` run.  The early atom state and the
declared left/right code berth separate the displayed routes when their
work projections meet.

The protected four-state register of the early atom theorem remains in its
final raw-phase atom state `Q_q`.  Here `q=0,1,3` for the neutral,
`CB^sA`, and `AB^sC` branches.  On the last branch, complete the private
`M`-gap crossing and the proved `Q_2 -> Q_3` update before declaring the
departure normal form.  Thus `Q_2` never occurs on the later cart-to-collar
sweep.  The ordered source collar remains literal.  Its order is copied
only after the piloted cart reaches the collar; the separate pilot theorem
gives that mandatory phase-changing transfer.

### 4.1 The `BBBB` branch

Use the first two blocks as the neutral cart atom and the last two as the
pilot/delimiter pair:

\[
                         BB|BB.                      \tag{4.3}

\]

Apply the proved path `BB -> HH` to the first pair.  Keep that `HH` fixed
and route the second `BB` inside `V_4` to `P|D`.  The early atom register
labels the neutral branch and the stationary cart labels every strict work
state.  The physical order `HH|P|D` recovers all four source `B` blocks.
Attach `P` to the mobile side of the cart.  The stationary odd delimiter
`D` remains at the source berth, `Q_0` remains literal, and the source
collar is unchanged.

### 4.2 The four-extreme branch

Among four consecutive binary extreme vertices containing two signs of each
kind, choose deterministically one adjacent unlike pair in the reduced word.
Together with its intervening `B` gap it is an ordinary transition atom.
Bootstrap it to a stationary `HH`; the gap is retained as its literal `M`
trail.

If this is the `AB^sC` private-gap orientation, move the cart through the
complete `M^s` trail now and perform the proved `Q_2 -> Q_3` update at its
first raw checkpoint.  The trail and early register retain the translated
cart origin.  Thus every later pilot-code state already has its final
raw-phase atom record; no `Q_2` state contains the completed `P|D` code.

The two unused extremes are again one `A` and one `C`.  Inside the physical
interval of length at most thirteen, bring those two blocks to a declared
two-block code berth.  Move an intervening `B` by the literal
`B|C -> C|M` path or its reflected version; move a block through the
stationary cart one head at a time.  At every nontrivial block interchange
one cart head remains literal.  The resulting `M` gaps, the declared berth,
and the deterministic left-to-right order retain every displaced `B`
occurrence.

There are two possible orientations of the remaining opposite pair.  Put
its code berth on the left side of the cart for `A|C` and on the right side
for `C|A`.  That physical side is a persistent orientation bit.  Route the
adjacent opposite pair in `V_4` to `P|D`.  The fixed cart and the still
literal early atom register guard the complete path.  Apply the gap
normalization below while `P|D` is literal, attach `P` to the mobile side of
the cart, and keep the resulting raw-phase atom state `Q_q` fixed.  At the
departure checkpoint:

* the side of the code berth gives the source orientation;
* the `M` trails give all original `B` gaps;
* the stationary cart address and the bounded geometry give the four source
  extreme addresses; and
* `D` locates the origin, `P` labels the moving train, and `Q_q` gives the
  atom branch while the source collar still gives its order.

Thus the whole source motif is recoverable before the original cart moves.

Before `P` is attached, normalize every selected-support `B` which is not
part of the already converted cart or pilot pair to `M`, in deterministic
left-to-right order.  The move `B=20 -> M=11` is one internal fixed-mass
edge.  Keep `H|H`, `P|D`, and `Q_q` literal while performing it.  The
declared interval geometry records exactly which source addresses are being
normalized, so the reverse teardown restores `B` at those and only those
addresses.  Consequently the selected support contains no background `B`
at its departure checkpoint: its noncode gap alphabet is `{M}`.  Raw blocks
which later enter the vacated interval remain in `{A,B,C}` and are
distinguished from these selected `M` occurrences by the inverse completed
train permutation from the delimiter `D`.

### Lemma 4.1 (copy-before-erase decoder)

The setup paths in Sections 4.1--4.2 are pairwise source disjoint.  After
their endpoint, `H|H|P` may leave the motif as a piloted mobile cart while
`D`, `Q_q`, and the literal source collar remain an injective source/order
record.

#### Proof

Before a motif block is altered, its literal source value and the source
collar label the chosen branch.  During every block transposition the fixed
cart supplies a literal sentinel, and the already restored prefix or
declared bounded subphase locates the active window.  The marked `B` gaps are
injective and retain their lengths and orientations.

During the final `P|D` route, projected paths belonging to different atom
types remain separated by the early register.  The fixed cart, code-berth
side, gap trails, local mass, and simplicity of the chosen `V_4` path
recover the source and microstep.  At the endpoint the four items listed in
Section 4.2, or the literal order in (4.3), recover the complete motif;
`Q_q` retains its atom branch and the unchanged source collar retains its
order.  During the final `B -> M` normalization the complete code and
declared address order remain literal, and on reverse each `M` is erased
only after its raw `B` address is restored.  Hence there is no
information-free checkpoint.

The stationary record contains the odd block `D` and lies within thirteen
blocks of the cart origin.  Its declared side and bounded geometry therefore
locate that origin after `H|H|P` leaves.  The other odd block `P` remains
inside the moving train. \(\square\)

All nonzero edges used here lie in the work suffix.  The proved fixed-row
generator consequently gives their directed lift one edge at a time.

## 5. Disjointness from the residual tasks

Remove the complete support selected in Theorem 3.1 from the cancellation
input before defining the residual bank.  Its signed charge is zero.
Therefore the signed imbalance of the remaining cancellation word is
unchanged, and the proved residual theorem still gives

\[
                              t\le3.                 \tag{5.1}

\]

Every residual occurrence is outside the cart/code motif by construction.
This directly repairs the false inference in the original OC18 Section 5,
where a nonzero-charge aperture chosen after the atom could itself be a
residual task.

### Theorem 5.1 (clean persistent temporary cart)

For every reserved work word of length at least 64 and imbalance at most
three, one may jointly choose a zero-charge bounded support and construct on
it:

1. a mobile temporary `H|H` cart;
2. a moving odd pilot `P` and an odd origin delimiter `D`, restored after
   every completed visit;
3. a persistent final atom state `Q_q` and the still-literal ordered source
   collar; and
4. a residual bank of size at most three disjoint from the complete code
   support.

The construction precedes every residual or `G_1` task and invokes no
source-independent fixed-head theorem.

#### Proof

Apply Theorem 3.1 and the corresponding construction in Section 4.  Then
apply the zero-charge deletion argument of Section 5.  Lemma 4.1 gives the
work-level occurrence decoder and the fixed-row audit gives the directed
lift. \(\square\)

## 6. Exact scope

If the reserved-collar work word has length `m-3`, the sufficient condition
`m-3>=64` is

\[
                         m\ge67,
                  \qquad k=2m-1\ge133.               \tag{6.1}

This intentionally trades threshold sharpness for a proof with no finite
search and no unbounded address record.  Smaller work words are not ruled
out; they are simply outside this selection theorem.

The pilot is mass-neutral bookkeeping: it is held fixed in every residual,
zipper, and collar conversion.  A separate piloted-train theorem must still
prove its occurrence-labelled crossing and retirement before this selection
theorem can be composed into APH.
