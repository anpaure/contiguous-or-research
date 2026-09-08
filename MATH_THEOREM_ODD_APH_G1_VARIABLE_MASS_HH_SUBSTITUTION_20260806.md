# Odd APH: variable-mass `G_1` task by double-head substitution

**Date:** 2026-08-06  
**Scope:** the one nonresidual task in `ACT4`, namely
`(G_1,B_2) -> (G_1^*,B_2)`  
**Method:** leave the target at its fixed source address, return a canonical
mass block with one head, and regenerate `H|H` at the collar; no computation
or search  
**Status:** unconditional from a recorded temporary cart and a decoded
task-to-collar corridor.  Together with the farthest-first residual carrier,
this closes the four-task escort schedule; persistent-origin construction
and retirement remain separate interfaces.

## 1. The canonical return block

Write

\[
                  X=(G_1,B_2),\qquad
                  X'=(G_1^*,B_2),                   \tag{1.1}
\]

and put

\[
                  d=\operatorname{mass}(X')-
                     \operatorname{mass}(X)
                    \in\{-2,0,2\}.                 \tag{1.2}
\]

Choose a canonical block `Z_d` by

\[
 \begin{array}{c|ccc}
 d&2&0&-2\\ \hline
 Z_d&A&H&C.
 \end{array}                                       \tag{1.3}
\]

Then

\[
                   \operatorname{mass}(Z_d)=2-d,
\tag{1.4}
\]

and hence

\[
 \operatorname{mass}(X)+2
    =\operatorname{mass}(X')+\operatorname{mass}(Z_d).
\tag{1.5}
\]

When `d=0`, the task is already at its target and may be omitted.  We retain
that row in the algebra to make the substitution uniform.

## 2. Leave `X'` at the fixed zipper address

The physical address of `(G_1,B_2)` is source independent: it is the first
ordinary zipper record immediately after the selected `p_1` clock.  Move the
recorded temporary cart through the decoded work interval to obtain

\[
                              X|H_1|H_2.             \tag{2.1}

\]

Keep `H_2` fixed and choose a simple path in the four-coordinate fixed-mass
layer

\[
                              X|H_1\leadsto X'|Z_d.  \tag{2.2}

\]

Equation (1.5) puts its endpoints in one layer.  The layer is nonextreme
because the full bounded state retains the fixed `H_2`, and if the
four-coordinate sublayer itself is extreme its two endpoints agree.  Thus
the prefix-discrepancy path supplies (2.2).  The fixed `H_2`, the named
zipper address, the decoded value of `a_1`, and simplicity give the strict
state decoder.

The endpoint is

\[
                              X'|Z_d|H_2.             \tag{2.3}

\]

It leaves the exact target at the labelled zipper address and exports the
return train `Z_d|H`.

## 3. Return the source mass to the collar

For one decoded intervening block `Y`, move the train right by

\[
       Z_d|H|Y
           \leadsto Z_d|Y|H
           \leadsto Y|Z_d|H.                        \tag{3.1}

\]

The second interchange keeps `H` fixed.  During the first, the fixed zipper
target `X'` and the already restored prefix identify the active boundary.
For a raw interval this is exactly the ticket-prefix decoder of the
farthest-first theorem, with the source-independent `X'` berth replacing a
residual `M` ticket.

If capacity forces one residual task to precede this task, the decoded
interval may contain its one literal `M`.  Its physical address is already
recorded, so the same prefix normal form includes that `M`.  A one-bit
collar branch distinguishes `B` from `M` in the only equal-mass local row;
the collar is then nonextreme by Lemma 4.1 below.  Concretely, normalize the
mass-two or mass-six collar to the first state in

\[
       A|B\longleftrightarrow A|M,
       \qquad
       B|C\longleftrightarrow M|C.                  \tag{3.2a}
\]

Each displayed toggle is one adjacent unit transfer and preserves collar
mass.  Write its second state only for the `M` branch, hold it throughout
that local crossing, and restore the first state before the collar update.
The literal zipper target and the still-decoded task tape make both toggles
copy-before-erase.  Thus the return remains
source disjoint over `{A,B,C,M}`.

At the collar, keep the returned `H` fixed and route

\[
                             K|Z_d\leadsto K'|H,      \tag{3.2}

\]

where `K,K'` are the collar states before and after the `G_1` increment.
Indeed the collar pays the negative task increment,

\[
                  \operatorname{mass}(K')
                     =\operatorname{mass}(K)-d,      \tag{3.3}
\]

so (1.4) gives

\[
       \operatorname{mass}(K)+\operatorname{mass}(Z_d)
          =\operatorname{mass}(K')+2.               \tag{3.4}

\]

The fixed outside head guards a simple path for (3.2).  Its endpoint is a
regenerated adjacent `H|H` carrier.

## 4. Capacity-safe insertion into the residual order

### Lemma 4.1 (at most one residual must precede `G_1`)

Let the initial collar mass be one of `0,2,4,6,8`.  The `G_1` task may be
processed first unless

\[
                         (\operatorname{mass}K,d)
                              =(0,2)\quad\hbox{or}\quad(8,-2).
\tag{4.1}

\]

In either exceptional row there are exactly three residual increments of
the opposite sign.  Processing the farthest residual first moves the collar
to mass two or six, after which the `G_1` task is legal.

#### Proof

The proposed first collar mass is `mass(K)-d`, so only the two rows in
(4.1) leave `[0,8]`.  Write `mass(K)=4+2c` with `c in {-2,-1,0,1,2}`.
The complete external increment is `2c`.  In the first exceptional row it
equals `-4`, while `d=2`; hence the residual sum is `-6`, namely three
`C -> M` increments.  One raises the collar from zero to two.  The second
row is the reflected statement: the residual sum is `6`, namely three
`A -> M` increments, and one lowers the collar from eight to six. \(\square\)

The preliminary residual is chosen farthest from the collar.  After the
`G_1` task, the remaining residuals retain their farthest-to-nearest order,
so the no-old-ticket invariant of the residual carrier theorem is unchanged.

## 5. The zipper escort theorem

### Theorem 5.1 (double-head substitution for `G_1`)

From a recorded temporary `H|H` cart, the zipper task
`(G_1,B_2) -> (G_1^*,B_2)` has pairwise source-disjoint directed paths which:

1. leave the target at the fixed zipper address;
2. restore every crossed work block;
3. update the collar by the exact opposite mass increment;
4. regenerate `H|H` at the carrier berth; and
5. compose with the farthest-first residual schedule after at most one
   preliminary residual task.

No source-independent fixed cart is assumed.

#### Proof

Equations (2.2), (3.1), and (3.2) give the path.  The fixed zipper address,
one literal head in every bounded conversion, the restored-prefix normal
form, and the optional one-bit `B/M` branch give its decoder.  Lemma 4.1
proves the capacity schedule.  Every work edge lies after `p_1` and therefore
has the audited fixed-row directed lift. \(\square\)

## 6. Exact consequence

Combine Theorem 5.1 with
`MATH_THEOREM_ODD_APH_FARTHEST_FIRST_HH_CARRIER_ESCORT_20260806.md`.
Starting from a persistent recorded temporary cart, all at most four `ACT4`
tasks now have an occurrence-labelled sequential realization.  No four-slot
simultaneous gather is needed:

* each residual leaves `M` at its source and regenerates the cart;
* the zipper task leaves `X'` at its fixed source and regenerates the cart;
* the collar follows the proved sign order and ends at mass four.

The remaining APH interfaces are construction/retirement of the persistent
temporary-cart origin support and the final mass-four collar-order copy.
