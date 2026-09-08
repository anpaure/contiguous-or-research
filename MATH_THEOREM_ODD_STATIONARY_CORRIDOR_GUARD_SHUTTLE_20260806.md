# Odd stationary-corridor guard shuttle

**Date:** 2026-08-06  
**Method:** one reversible premark, a growing marked corridor, and a
two-mark return tail  
**Status:** proof-safe occurrence-labelling theorem for shuttles with at
least two interior neutral/tag blocks.  The corrected return moves the
active block across the still-marked corridor and erases marks only after it
reaches its old address.  A generic one-interior table, iteration through
multiple residuals, and protected `p_1` compatibility remain finite open
cases.

## 1. Alphabets

Retain

\[
 A=00,\quad B=20,\quad C=22,\quad
 T_A=21,\quad T_C=01
\tag{1.1}
\]

and the guardable alphabet

\[
                  \mathcal G=\{B,T_A,T_C\}.
\tag{1.2}
\]

Define the mass-preserving injective mark map

\[
 \mu(B)=11,\qquad \mu(T_C)=10,\qquad \mu(T_A)=12.
\tag{1.3}
\]

Its image `C={10,11,12}` is disjoint from the macro alphabet
`{A,B,C,T_A,T_C}`.  Each change `Y<->mu(Y)` is one adjacent unit transfer
inside the two-coordinate block.

Assume one global pass/branch register is fixed.  As in the existing
four-state register, local mass plus the branch bit distinguishes the at
most two ordered endpoint types in each mass layer.  For every required
bounded block rewrite choose once and for all a simple path in the
corresponding fixed-mass token graph.

## 2. The guarded first crossing

Consider an active block `X` which must move right through

\[
                  Y_1Y_2\cdots Y_s,
             \qquad Y_i\in\mathcal G.
\tag{2.1}
\]

The left-moving version is its reflection.

If `s>=2`, first replace `Y_2` by `mu(Y_2)`.  This is a single literal
edge and has no strict intermediate.  Now perform the first local rewrite
on the two blocks `X|Y_1`, ending at

\[
                         \mu(Y_1)|X,
\tag{2.2}
\]

while `mu(Y_2)` remains fixed immediately to the right of the active
two-block window.  It therefore locates that window at every strict state
of the chosen simple local path.

Next swap `X` through the already marked `mu(Y_2)`, leaving that mark on
the left.  During this local path `mu(Y_1)` remains fixed immediately to
the left.  The result is

\[
                  \mu(Y_1)\mu(Y_2)X.
\tag{2.3}

Thereafter, for `j=3,...,s`, use the mass-preserving local rewrite

\[
                         X|Y_j
                    \leadsto
                         \mu(Y_j)|X.
\tag{2.4}

The nonempty marked corridor

\[
              \mu(Y_1)\cdots\mu(Y_{j-1})
\tag{2.5}

is fixed throughout that local path and locates its right boundary.

For `s=0` the active block is already adjacent to its target.  For `s=1`
there is no second stationary mark, so the argument above supplies no
strict-state occurrence label unless that particular three-block window is
independently protected.  Such a window need not lie in the fixed collar.
Thus the theorem below is unconditional for `s>=2` (and for any separately
certified zero/one-interior local table), not for every one-interior shuttle.

## 3. Decoder during the outward shuttle

### Lemma 3.1 (strict-state source decoder)

At every endpoint and strict local state of the construction above, the
literal tape together with pass/branch recovers:

1. the original source tape;
2. the physical address of `X`;
3. the number of completed crossings; and
4. the microstep on the current local path.

#### Proof

Outside the active local window, the only values in `C` form the marked
corridor (2.5), except during the first crossing when the fixed premark
`mu(Y_2)` is the unique such value.  The active window is respectively
immediately beside that premark or immediately beside the appropriate end
of the maximal marked corridor.  Apply `mu^-1` to the fixed marks to recover
the crossed source blocks and their order.  The pass gives the direction,
local mass and the branch bit give the ordered endpoint type, and simplicity
of the chosen local path gives its microstep.  Reinsert the decoded active
block at the recovered corridor boundary to reconstruct the source.

The first premark is itself injective: `mu` is injective, and different
physical premark addresses give different literal states.  It therefore
does not merge two source paths.  \(\square\)

## 4. Return without an unguarded last swap

After the bounded operation at the collar, let the active return block be
`X'`.  Move it left through the corridor in reverse order, but do **not**
erase a mark while crossing it.  For `j=s,s-1,...,1`, use

\[
                  \mu(Y_j)|X'\leadsto X'|\mu(Y_j).
\tag{4.1}
\]

For `j=s`, the fixed mark `mu(Y_(s-1))` guards the active window on its
left; for `1<j<s` a fixed mark exists on both sides; and for `j=1` the
already crossed mark `mu(Y_2)` guards it on its right.  This is why two
marks, rather than one, were installed before the first crossing.  Once
`X'` has returned to its labelled source address, the tape has the form

\[
                         X'\mu(Y_1)\mu(Y_2)\cdots\mu(Y_s).
\tag{4.2}

Restore each `mu(Y_j)->Y_j` by the single literal edge inverse to (1.3).
There is no strict unmarked intermediate on any such edge.  Hence the
return has a decoder throughout, moves `X'` back to the old address of
`X`, and restores every crossed block at its original address.

### Theorem 4.1 (stationary-corridor visible cart)

Every shuttle through a word of length at least two over `G` has pairwise
source-disjoint literal paths and returns all nonactive blocks to their
labelled addresses.  The same holds for a zero- or one-interior shuttle
only when its local conversion has a separately certified protected collar
or visible strict-state table.  No double `02|02` head or anonymous work
reservoir is used in the length-at-least-two construction.

#### Proof

Sections 2 and 4 give the paths.  Lemma 3.1 and its reversed decoder show
that every current literal state recovers source, phase, active address,
and microstep.  Two paths meeting at a state would therefore have the same
source and the same step, proving pairwise disjointness.  \(\square\)

### Corollary 4.2 (bounded train extension)

The active block `X` in Theorem 4.1 may be replaced by any fixed-length
word `X_1...X_t`, provided every required interchange with one marked or
unmarked stationary block has nonextreme total mass.  In particular, two
equal residual extremes can first be gathered into a two-block train and
then transported together, whenever each nontrivial corridor used in this
two-stage operation has length at least two.

#### Proof

Nothing in Sections 2--4 used that the active window had exactly two
coordinates.  Replace each local two-block token graph by the capacity-two
token graph on the `2t+2` coordinates occupied by the train and one
stationary block.  It is connected in every nonextreme fixed-mass layer, so
a simple local path exists.  The stationary mark still lies immediately
beside the now longer active window and therefore locates it; the active
length `t` is part of the finite phase.  The same inverse corridor decoder
applies verbatim.

To gather two equal extremes, shuttle the second through the neutral/tag
word between them without yet restoring that corridor.  The resulting
two-block train is labelled by this first corridor.  Shuttle the train to
the collar through a second corridor, perform the bounded collar operation,
and reverse the second and then the first shuttle.  The two subphases are
distinguished by the fixed pass register, and at least one complete marked
corridor is retained throughout each strict local path.  Hence their
composition remains source-decodable.  \(\square\)

## 5. Application to noncrossing odd cancellation

The noncrossing cancellation theorem says that, when an opposite pair is
processed, every physical block strictly between its endpoints is either
`B` or a tag belonging to an earlier pair.  These are exactly the members
of `G`.  In reverse deletion order, the same statement holds during
finalization.  Theorem 4.1 therefore supplies the strict-state visible cart
for every such shuttle with at least two intervening blocks.  An adjacent
pair uses the already explicit local tag/finalization paths.  A pair with
exactly one intervening block still needs the finite protected three-block
table described in Section 6.

For the balanced midpoint packet, first pair all possible opposite signs
inside the packet, and pair an opposite collar pair internally.  The
remaining packet extremes all have one sign, the remaining collar extremes
have the opposite sign, and their counts are equal by the exact packet--
collar charge identity.  Since the collar has two blocks, this common count
is at most two.  Thus there is never a three-block cross remainder.

In the two-cross case, gather the two raw packet extremes before performing
any midpoint conversion and regard them as one length-two train.  Corollary
4.2 transports this train to the two collar extremes, both cross pairs are
converted in one bounded fixed-mass collar window, and the midpoint train is
returned before its two members are separated back to their labelled
addresses.  No pre-existing midpoint block is crossed.  This is unconditional
when the gathering and collar corridors have length zero or at least two;
the one-interior subcase remains part of the finite table below.

## 6. Exact remaining scope

The theorem proves occurrence labelling, not permission to alter a
protected connector.  To close the odd package one must still verify that
the local paths involving the first `p_1` connector:

1. use the transported shadow clock rather than the old linkage edge;
2. preserve the fixed three-row collar record and root/boundary register;
3. do not traverse a protected aperture state; and
4. return the first connector to the labelled address required by the
   complement endpoint.

In addition to the protected first-connector compatibility check, one finite
one-interior three-block table remains.  The train construction removes the
former multiple-midpoint ordering issue.  All ordinary noncrossing
cancellation shuttles and midpoint/train shuttles with zero or at least two
intervening blocks are covered.
