# Odd APH: protected-island cart transport and a collision-free two-berth schedule

**Date:** 2026-08-06  
**Method:** literal reinterpretation of identical heads, guarded fixed-mass
block transpositions, and one reserved separator; no computation or search  
**Status:** unconditional once a temporary literal `H|H` cart with an early
origin record has been constructed.  This repairs the protected-island,
sentinel-crossing, and two-head-coexistence joins from the independent APH
audit.  It does not construct the temporary cart or the permanent collar
head.

## 1. Protected islands

Put

\[
                         H=02,\qquad M=11.
\]

The only atom-origin islands exported by the audited setup paths are

\[
                         H,\qquad H|M,\qquad M|H.     \tag{1.1}
\]

Assume that an early literal record fixes the island type and orientation
before any head moves.  Let a temporary cart be the adjacent pair `H|H`.

### Lemma 1.1 (the cart crosses every origin island)

The cart has a reversible occurrence-labelled transport across each word in
(1.1), preserving that word literally.

#### Proof

Write the motion from left to right; reflection gives the other direction.

For an isolated `H`,

\[
                         HH|H=H|HH.                  \tag{1.2}
\]

No physical edge is required.  Suppress the duplicate macro checkpoint and
change only the parse: before (1.2) the left pair is the cart, afterward the
right pair is the cart.  The sweep direction and the early island record
determine the parse.  A run of several identical heads is treated as one
such zero-length crossing, so no graph vertex is repeated.

For `H|M`, first use (1.2) and then move the reparsed cart through `M`:

\[
                         HH|H|M
                    =    H|HH|M
                    \leadsto H|M|HH.                 \tag{1.3}
\]

For `M|H`, move the cart through `M` first and then reparse the terminal
head run:

\[
                         HH|M|H
                    \leadsto M|HH|H
                    =       M|H|HH.                  \tag{1.4}
\]

The nontrivial arrow in each line is the proved double-head swap through the
mass-two block `M`.  During (1.3) the island head on the left remains fixed;
during (1.4) the island head on the right remains fixed.  It locates every
strict local state.  The early orientation record distinguishes the two
reflected branches, and simplicity of the chosen fixed-mass path gives the
microstep.  Reversal proves the return statement.  \(\square\)

The equality in (1.2) is not an illicit identity-of-particles argument.  The
state graph has no particle labels.  It says that crossing an identical
block contributes no edge and that the next nontrivial edge is decoded using
the stored sweep direction.

## 2. A bulk shuttle may cross a protected island

The audit also requires cancellation arcs whose endpoints lie on opposite
sides of an atom record.  The cart alone crossing the island is not enough;
the active block must cross it too.

### Theorem 2.1 (protected-island active-block transport)

Let `X` be one active connector or tag block, and keep a literal `H|H` cart
at the island side of the bounded active support.  Then `X` can be moved
reversibly through any island in (1.1), preserving the island and the cart.
All strict states have a source/stage decoder.

#### Proof

For the isolated island, use

\[
                         X|H|HH\leadsto H|X|HH.       \tag{2.1}
\]

Choose a simple path interchanging `X|H` in their four-coordinate
fixed-mass layer and hold the right `H|H` literally fixed.  The relevant
total masses are two, four, or six for the source alphabet and remain
nonextreme for every tag/corridor block, so the capacity-two token graph is
connected.

For the two-block islands, apply (2.1) one island block at a time:

\[
 \begin{aligned}
 X|H|M|HH&\leadsto H|X|M|HH
                 \leadsto H|M|X|HH,\\
 X|M|H|HH&\leadsto M|X|H|HH
                 \leadsto M|H|X|HH.                 \tag{2.2}
 \end{aligned}
\]

At the first strict path in either row, the untouched remainder of the
island together with the fixed cart is a bounded literal sentinel.  At the
second path, the already restored first island block and the fixed cart are
sentinels.  If an island `H` merges visually with the cart, the early island
orientation and the current one-of-two subphase determine which adjacent
pair is held fixed.  Local mass fixes the endpoint class and simplicity
fixes the microstep.  Therefore equality of two full states forces equality
of source, island address and orientation, subphase, and microstep.

Reflection gives right-to-left transport.  Reversing the two simple paths in
the opposite order restores every island block and the cart.  \(\square\)

### Corollary 2.2 (protected-island marked/LIFO extension)

The marked/LIFO bulk theorem remains valid when finitely many early-recorded
atom supports of types (1.1) are deleted from its cancellation word.
Cancellation arcs may cross those supports: bring the cart to the active
block using Lemma 1.1, use Theorem 2.1 to cross the complete support, and
continue the ordinary marked shuttle.  The island is restored before the
next macro operation.

#### Proof

The ordinary marked theorem already decodes every segment between protected
supports.  Lemma 1.1 supplies cart transport from one segment to the next,
and Theorem 2.1 supplies the missing active-block transposition.  Each added
macro is reversible and restores its island before composition.  The early
record and the deterministic noncrossing/LIFO order identify which island
is active.  Hence the individual decoders concatenate without an
information-free checkpoint.  \(\square\)

This corollary is precisely the protected-island theorem that the old phrase
"treat the origin trails as protected supports" did not prove.

## 3. Reserve one separator for two simultaneous heads

For a completely literal coexistence schedule, reserve one additional
connector block `D` between the temporary berth and the two-block permanent
collar berth.  The value of `D` may be any source block in
\(\{A,B,C\}\); it is held literal during head creation and therefore is
never `H`.

Deleting `p_1`, the two collar blocks, and `D` leaves a word of length
\(m-4\) and imbalance at most four.  The proof of the one-atom theorem gives
the following useful bound.

### Lemma 3.1 (one atom after also reserving a separator)

Every linear word with \(|\#A-\#C|\le4\) and length at least ten contains
an ordinary transition or `BB` atom.

#### Proof

If the reduced extreme word has a transition, use it.  Otherwise all
extremes have one sign and there are at most four.  If `BB` is absent, at
most five `B`-runs each have length at most one, giving total length at most
nine.  \(\square\)

Thus one anchored source atom and one fixed separator coexist for
\(m\ge14\), equivalently \(k\ge27\).  A two-atom construction may require a
larger threshold, but no asymptotic obstruction is introduced.

## 4. Exact temporary/permanent berth schedule

Let

\[
              \mathfrak b_T\;|\;D\;|\;\mathfrak b_P \tag{4.1}
\]

be respectively a two-block temporary berth, the one-block separator, and
the two-block fixed collar berth.  Assume a recorded temporary cart has been
assembled and can be returned to \(\mathfrak b_T\), while the protected
collar accumulator creates the permanent cart at \(\mathfrak b_P\).

### Theorem 4.1 (two-head-bank schedule)

There is a schedule in which the temporary and permanent carts coexist
without ever losing their literal identities:

1. use the temporary cart for every bulk and pre-head collar operation;
2. restore `D` literally after each crossing;
3. on the final collar operation, return the temporary cart across `D` to
   \(\mathfrak b_T\) while the newly created permanent cart remains fixed;
4. retain the state
   \[
                         HH|D|HH                       \tag{4.2}
   \]
   until the temporary origin atoms are retired; and
5. keep the right pair in (4.2) fixed while the left pair returns to and
   retires its source support.

At every stage the active cart and the permanent cart are occurrence
labelled.

#### Proof

Before the last collar operation there is only one cart, so the established
early origin record and cart decoder apply.  During the last bounded
operation, the source collar and the temporary cart label the active local
path.  Once the target `H|H` appears at \(\mathfrak b_P\), keep it fixed.
The temporary cart crosses `D` by the ordinary double-head transport theorem;
the permanent pair is an additional fixed sentinel throughout this bounded
return.

At (4.2), `D` is not `H`, so the two maximal head runs are disjoint and their
physical berths distinguish them.  The right run is declared permanent and
never moves during temporary teardown.  The left run moves away from it;
Lemma 1.1 handles any protected origin island met on return.  Reversing the
early atom paths retires the temporary support while the permanent run and
its berth remain literal.  Hence no `HHHH` checkpoint and no unique-head
assumption occurs.  \(\square\)

## 5. Exact scope and remaining condition

Theorems 1.1 and 2.1 close the audit's sentinel/cart and protected-island
rows.  Theorem 4.1 closes the disjoint temporary/permanent berth schedule.
They are implications from a recorded temporary cart and a successful
permanent-collar accumulator.

The sole pre-head premise not supplied here is therefore not an informal
"cart can probably cross its records" statement.  It is the following named
condition:

> **Recorded temporary-cart creation / anchored-catalyst condition.**  From
> the one recorded anchored head of the early-record theorem (or from two
> jointly recorded atoms), construct the temporary `H|H` cart and execute the
> at most four zipper-split collar increments before invoking the fixed-cart
> theorem.

Once this condition is proved, the present theorem supplies all subsequent
island crossings and the two-head coexistence/retirement schedule.  No
further protected-island or berth assumption is hidden in the composition.
