# Odd APH: farthest-first double-head carrier closes the residual escort row

**Date:** 2026-08-06  
**Scope:** the residual-extreme part of `ACT4` / `OC-ACT4`  
**Method:** a regenerated `H|H` carrier, a literal `M` source-address ticket,
and farthest-to-nearest ordering; no computation or search  
**Status:** unconditional on a raw task interval and a previously recorded
temporary cart.  The theorem supplies every residual task `A,C -> M` and
regenerates the cart after each task.  It does not construct the persistent
cart-origin code, select its clean aperture, or perform the separate
`G_1 -> G_1^*` task.

## 1. Setup and the ordering invariant

Put

\[
             A=00,\qquad B=20,\qquad C=22,
             \qquad H=02,\qquad M=11.               \tag{1.1}
\]

Fix a collar side of the linear work word.  Suppose the residual task
occurrences are

\[
                         x_1,x_2,\ldots,x_t,
                  \qquad t\le3,                     \tag{1.2}
\]

listed in strictly decreasing distance from the collar.  All task blocks
have one common source value

\[
                         X\in\{A,C\}                 \tag{1.3}
\]

and all have target `M`.  Assume that ordinary blocks in the interval from
the current task to the collar are still raw over `{A,B,C}`.  Any bounded
recorded support deleted from that interval is crossed by its separately
proved protected-support macro and restored before the raw sweep resumes.

Let `K_i` be the two-block collar state before task `i`.  The signed collar
schedule gives

\[
       \operatorname{mass}(K_i)+\operatorname{mass}(X)
          =\operatorname{mass}(K_{i+1})+2,           \tag{1.4}
\]

and keeps every collar coordinate in capacity.  The number two on the right
is both `mass(M)` and `mass(H)`.

Assume a literal temporary cart `H|H` is at the collar-side carrier berth,
and assume its displaced adaptive origin is retained by a persistent literal
record.  This is a temporary recorded cart, not the source-independent
permanent head which APH is constructing.

### Lemma 1.1 (no old ticket is crossed)

Immediately before task `i`, every old residual target `M` lies strictly
farther from the collar than `x_i`.  Hence the open interval from `x_i` to
the collar contains no old `M` ticket.

#### Proof

Tasks `1,...,i-1` occur at the positions farther from the collar than
`x_i`, by the ordering in (1.2).  Each completed task changes only its own
source position to `M` and restores every intervening block.  No other
residual target has yet been written. \(\square\)

Thus each new carrier sweep sees a raw interval even though the global tape
may already contain up to two old `M` targets.

## 2. Deposit the ticket and split off a return train

Use the recorded-cart transport theorem to move `H|H` from the collar
through the raw interval to the right side of the current `X`.  It reaches

\[
                         X\mid H_1\mid H_2.           \tag{2.1}
\]

Perform the following three bounded operations:

\[
 \begin{aligned}
 X|H_1|H_2
   &\leadsto H_1|X|H_2\\
   &\leadsto H_1|H_2|X\\
   &\longrightarrow M|H_2|X.                        \tag{2.2}
 \end{aligned}
\]

The first block interchange keeps `H_2` fixed.  The second keeps `H_1`
fixed.  The last arrow is the single internal work edge

\[
                              02\longrightarrow11.   \tag{2.3}
\]

It keeps `H_2` fixed.  Therefore every strict state in (2.2) has a literal
head sentinel, and its endpoint leaves:

* the target `M` at the exact physical source address `x_i`; and
* the two-block return train `H|X` immediately on its collar side.

Total mass is unchanged in (2.2).

## 3. The train restores the raw interval

Write the source interval from the task toward the collar as

\[
                         X|Y_1Y_2\cdots Y_s|HH,
              \qquad Y_j\in\{A,B,C\}.               \tag{3.1}
\]

After (2.2) it is

\[
                         M|H|X|Y_1\cdots Y_s.         \tag{3.2}
\]

Move the train right through one raw block by

\[
       H|X|Y
          \leadsto H|Y|X
          \leadsto Y|H|X.                           \tag{3.3}
\]

The first interchange in (3.3) keeps `H` fixed.  During the second, the
rightmost `X` is fixed and the already restored prefix on the left gives the
active boundary.  Iteration gives the macro checkpoints

\[
 M|Y_1\cdots Y_j|H|X|Y_{j+1}\cdots Y_s,
                  \qquad 0\le j\le s,               \tag{3.4}
\]

and ends at

\[
                         M|Y_1\cdots Y_s|H|X.         \tag{3.5}
\]

Every raw block has returned to its original physical address.

### Lemma 3.1 (ticket-prefix decoder)

Every macro and strict state of (3.3)--(3.4) recovers the current source,
task address, completed crossing count, local endpoint type, and microstep.

#### Proof

By Lemma 1.1 the current `M` is the first completed residual ticket met when
the task line is scanned away from the collar; older residual tickets lie
strictly beyond it.  Any atom-origin `M` trail belongs to a separately
recorded deleted support and is not part of the raw interval.  Hence the
displayed `M` identifies `x_i` literally.

At a macro checkpoint, the unique `H|X` return train on the collar side of
that ticket gives the split in (3.4).  Replacing the ticket by `X` and moving
the train back to the ticket through the restored prefix recovers (3.1).
If a crossed block equals `X`, its block interchange is a zero-length
reparse; suppressing that duplicate checkpoint changes no graph vertex and
the deterministic sweep direction fixes the parse.

At the first strict interchange in (3.3), `H` remains literal and locates
the active window.  At the second strict interchange, the fixed `X` lies
immediately to the right of the active two-block window.  On its left is the
normal form

\[
                         M|Y_1\cdots Y_j.             \tag{3.6}
\]

The chosen simple `H|Y -> Y|H` paths have a strict state outside the raw
alphabet; the first deviation from (3.6) therefore locates the active
window.  Local mass and the fixed branch state choose `Y in {A,B,C}`, and
simplicity chooses the microstep.  Inverting that microstep and the completed
train moves recovers the unique source.

Thus equality of two full states forces equality of the task ticket,
source, `j`, local branch, and microstep. \(\square\)

## 4. Regenerate the double head at the collar

At (3.5), keep the returned `H` fixed and apply a simple fixed-mass work path
on the two collar blocks and `X`:

\[
                         K_i|X\leadsto K_{i+1}|H.     \tag{4.1}
\]

Equation (1.4) is exactly the mass identity for (4.1).  Its layer is
nonextreme because its endpoint contains `H`.  The prefix-discrepancy
algorithm therefore supplies a simple path.  The fixed outside `H` locates
every strict state.  The persistent collar-order record and the literal
task ticket choose the collar branch, while simplicity chooses its
microstep.

After (4.1), the fixed outside head and the newly written head are adjacent:

\[
                              H|H.                   \tag{4.2}
\]

Thus the temporary cart is regenerated before the next task.

## 5. The residual escort theorem

### Theorem 5.1 (farthest-first `HH` carrier)

Under the hypotheses of Section 1, all `t<=3` residual tasks have pairwise
source-disjoint directed paths which:

1. change every labelled residual source `X` to `M` at its original address;
2. restore every crossed raw block after each task;
3. update the collar by the exact signed increment (1.4);
4. regenerate the same literal temporary `H|H` carrier after each task; and
5. preserve the selected `p_1` row and the persistent cart-origin/collar
   records.

No source-independent fixed head and no unlabelled task shuttle is invoked.

#### Proof

For task `i`, Lemma 1.1 makes its complete carrier interval raw.  Recorded
double-head transport gives (2.1), the fixed-head-at-each-swap construction
(2.2) deposits the literal address ticket, Lemma 3.1 decodes the complete
return, and (4.1) regenerates the carrier.  Each task restores its open
interval before the next starts, so induction preserves the hypotheses.

The work supports lie after `p_1`.  Every nonzero local edge therefore has
the already audited fixed-row directed lift.  Concatenating the individual
decoders proves pairwise source disjointness. \(\square\)

## 6. Exact boundary of this theorem

The theorem closes the old two-residual ordering obstruction.  Processing
near-to-far made a later shuttle cross an old `M`; processing far-to-near
used to make the first raw residual cross unlabelled extremes.  The temporary
double cart now labels that outward raw crossing, and the newly deposited
`M` labels the returning train.  No dirty-alphabet single-head theorem is
needed.

Three interfaces remain separate.

1. The persistent temporary-cart origin code and a clean support for it must
   be constructed before Theorem 5.1 is invoked.
2. If that bounded code support lies inside a task interval, its cart/train
   crossing must use a stated protected-support macro; alternatively the
   selector may place it outside all residual task intervals.
3. The zipper task `G_1 -> G_1^*` has a target of variable mass and is not an
   `X -> M` row.  Its analogous bounded carrier substitution remains a
   separate lemma.

Subject only to those interfaces, the occurrence-labelled residual
gather/scatter row of `ACT4` is closed.

