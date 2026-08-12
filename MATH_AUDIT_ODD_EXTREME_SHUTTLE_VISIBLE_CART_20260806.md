# Independent audit: the extreme-shuttle tape recoder still needs a literal visible cart

**Date:** 2026-08-06  
**Scope:** `MATH_THEOREM_ODD_EXTREME_SHUTTLE_TAPE_RECODER_20260806.md`,
especially the branch-tag assertion in Section 3 and the pairwise-disjointness
conclusion in Theorem 4.1.  No computation is used.

## Verdict

The connector involution, balance identity, literal tag/finalization paths,
finite fixed-mass block-interchange lemma, and termination of the two-pass
cancellation schedule all pass.

The claimed occurrence-labelled path bank does **not** yet pass.  Its smallest
missing premise is a literal visible-cart encoder for the finite block-crossing
branches.  The already proved root flag and `p_1` interfaces give a plausible
12-state raw alphabet, but the current theorems do not show that this alphabet
is a persistent, writable branch tag while `p_1` is simultaneously serving as
the shadow clock.

Accordingly, Theorem 4.1 is proof-safe only conditional on the visible-cart
condition stated in Section 5 below.

## 1. Parts that pass

For the connector code

\[
                 C(a)\in\{00,20,22\},
\]

reflection swaps `00` and `22` and fixes `20`.  Central balance gives equal
numbers of the two extreme codes.  The two literal paths

\[
\begin{aligned}
0022&\to0112\to1012\to1102\to2002\to2011\to2101,\\
2200&\to2110\to1210\to1120\to0220\to0211\to0121
\end{aligned}
\]

and the two finalization paths

\[
2101\to2110\to2200,
\qquad
0121\to0112\to0022
\]

are legal adjacent unit transfers.  The tags `21` and `01` retain the
orientation of the processed extreme pair.  The capacity-two token graph on a
finite path is connected in each nonextreme mass layer, so every finite block
interchange asserted in Lemma 3.1 exists.  The deterministic cancellation
schedule therefore reaches the reflected tape as an unlabelled walk.

These facts do not by themselves prove that the walks for all sources are
pairwise vertex-disjoint.

## 2. A stage tag is mathematically necessary

The literal local paths themselves overlap across the two passes.  For example,

\[
 00|22\longrightarrow 0112
\]

is the first tagging move in the first orientation, while

\[
 01|21=0121\longrightarrow 0112
\]

is the first finalization move in the opposite orientation.  Likewise `0022`
is both the first tagging endpoint and the opposite finalization endpoint.
The symmetric collision is

\[
 22|00\longrightarrow2110
 \qquad\hbox{and}\qquad
 21|01=2101\longrightarrow2110.
\]

Take two balanced source tapes with the same blocks outside the active pair,
and with active source pairs `00|22` and `22|00`, respectively.  Global balance
does not distinguish them: both active pairs contain one extreme of each type.
At the displayed local state their work tapes can therefore be literally
equal.  A visible pass/branch tag is essential; the processed `01/21` tags and
the balance equation alone do not prove injectivity.

## 3. Why the existing 12 literal states are not automatically 12 tags

The six selected nonquiet `p_1` states are the endpoints of three matching
rows,

\[
 01\leftrightarrow10,
 \qquad
 02\leftrightarrow11,
 \qquad
 12\leftrightarrow21.
\tag{3.1}
\]

Together with the root flag `f in {0,2}`, they give twelve instantaneous
literal pairs `(f,p_1)`.

However, the shadow-clock compilation theorem toggles the selected `p_1`
endpoint after **every** physical work transfer.  Thus the invariant carried
unchanged by a tail walk is only

\[
   (f,\hbox{the selected row of (3.1)}),
\]

which has six possibilities.  The endpoint bit can still be used, but only
after proving a parity cocycle: for every branch and every local microstep the
decoder must know whether to read the originally assigned endpoint or its
mate.  No such assignment or collision audit appears in the recoder theorem.

In particular, merely counting

\[
  2\ \text{root flags}\times6\ \text{selected states}=12
\]

does not establish twelve persistent branch labels.

There is a second issue.  Moving between the three rows in (3.1) changes the
clock mass.  The shadow-clock mass-router theorem proves scalar reachability
of those rows, but its own conclusion explicitly leaves labelled
serialization open.  Invoking that router to *write and erase the label used
to prove labelled serialization* is circular unless the setup and teardown
paths are themselves supplied with an injective decoder.

## 4. Processed tags do not close the internal-time gap

At macrostep boundaries, the alphabet

\[
 \{00,20,22,01,21\}
\]

does identify source, processed, and target blocks once the global pass is
known.  It also makes the deterministic leftmost cancellation pair
recoverable at those boundaries.

Inside a finite interchange, Lemma 3.1 supplies only existence of a simple
path for each ordered pair of block types.  Simplicity prevents repetition
within one chosen path; it does not prevent two different branch paths, or a
tagging path and a finalization path, from sharing a local state.  The explicit
overlaps in Section 2 show that this distinction is real.

The statement

> current local state and delimiter recover the ordered input type and the
> microstep

is therefore exactly the missing premise, not a consequence of Lemma 3.1.

## 5. Smallest proof-safe completion

It is enough to prove the following finite interface.

### Visible-cart condition

Let `Theta` be the finite set of tagging, shuttling, return, and finalization
branches, including orientation.  For every `theta in Theta`, give a directed
setup--work--teardown path on the root, `p_1`, and a bounded collar such that:

1. `p_1` is a selected nonquiet row at every work vertex, so the fixed shadow
   clock remains valid;
2. after accounting for the forced mate toggle in (3.1), the current cart
   state together with the current local tape state uniquely determines
   `(theta,microstep)`;
3. setup and teardown states satisfy the same injectivity, not merely the
   steady work states;
4. different branch trajectories can meet only where their accompanying tape
   states are already disjoint;
5. the root and collar are restored to the prescribed ordinary delimiter at
   the end; and
6. every clock-mass change is routed by a specified occurrence-labelled path,
   rather than by scalar token-graph connectivity alone.

Under this condition, the tagged time-expansion lemma applies exactly as
claimed: the processed `01/21` tags recover macro history, the visible cart
recovers the active finite branch and microstep, and the fixed `p_1` clock
directs every tail transfer.  The remainder of Theorem 4.1 then passes.

## 6. Exact frontier

The recoder has reduced the old macroscopic tape problem to a bounded finite
one, which is genuine progress.  But the present proof has not yet shown that
the existing `(root flag,p_1 selected state)` bank realizes that finite cart.
The correct status is therefore:

\[
\boxed{
\text{unlabelled reflected tape recoding: proved;}
\quad
\text{simultaneously disjoint directed bank: conditional on visible cart.}
}
\]

