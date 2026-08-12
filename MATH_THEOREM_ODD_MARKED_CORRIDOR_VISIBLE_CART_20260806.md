# Odd current: marked-corridor serialization and the exact visible-cart atom

**Date:** 2026-08-06  
**Method:** literal connector algebra and reversible decoding; no search or
computation  
**Status:** unconditional global reduction.  The noncrossing/LIFO
serialization and a four-state protected boundary register are proved.
The entire remaining tape issue is one finite local visible-cart lemma,
stated exactly in Section 6.  Ordinary fixed-mass connectivity does not by
itself prove that lemma.

## 1. Code and marker alphabets

Write

\[
 A=00,\qquad B=20,\qquad C=22,
 \qquad T_A=21,\qquad T_C=01.
\tag{1.1}
\]

The source connector alphabet is \(\{A,B,C\}\).  Complement interchanges
\(A,C\) and fixes \(B\).  The tags \(T_A,T_C\) record an original
\(A,C\), respectively.  As in the zipper audit, centrality gives

\[
                         \#A=\#C.
\tag{1.2}
\]

For a stationary block put

\[
 \mu(B)=11,\qquad \mu(T_C)=10,\qquad \mu(T_A)=12.
\tag{1.3}
\]

The map \(\mu\) is injective, preserves block mass, and its image is
disjoint from the macro alphabet

\[
              \mathcal A=\{00,20,22,01,21\}.
\tag{1.4}
\]

The three values in (1.3) are called **corridor marks**.

## 2. Why the unmarked shuttle is not injective

The type of a moving block is not a position label.

### Proposition 2.1 (exact location collision)

An algorithm which moves the right member of a selected opposite pair
left through literal \(B\)-blocks, while recording only the phase and the
ordered block types in a fixed boundary delimiter, need not give disjoint
source paths.

#### Proof

Consider the two valid balanced connector words

\[
                         x=ABCB,
             \qquad      x'=ACBB.
\tag{2.1}
\]

They encode the ternary words \((0,1,2,1)\) and \((0,2,1,1)\), both of
length and digit sum four.  Common \(B\)-tails extend the example to every
larger semilength.

In \(x\), the first selected opposite pair is the displayed \(A,C\).
After the right \(C\) is interchanged once with the intervening \(B\), the
literal tape is \(ACBB=x'\).  In \(x'\), the same selected pair is already
adjacent.  The phase and ordered pair type are the same.  Therefore either
the ordinary-delimiter state of the first route meets the second source,
or, if the fixed delimiter is set before the pair conversion, the two
routes meet after the second route sets that same delimiter.  A graph path
cannot omit the interchange endpoint.  \(\square\)

Thus the earlier claim that a fixed branch tag plus an arbitrary simple
token path identifies the shuttle position is false.  A physical record
of the crossed interval is necessary.

## 3. The marked-corridor macro rewrite

Let

\[
 X\in\{A,C,T_A,T_C\},
 \qquad Y\in\{B,T_A,T_C\}.
\]

The forward corridor rewrite is

\[
                         Y\mid X
                  \longmapsto
                         X\mid\mu(Y).
\tag{3.1}
\]

The return rewrite is

\[
                         X'\mid\mu(Y)
                  \longmapsto
                         Y\mid X'.
\tag{3.2}
\]

Both preserve total mass.  Starting from

\[
                 Y_1Y_2\cdots Y_sX,
\]

successive applications of (3.1), from right to left, give

\[
                 X\mu(Y_1)\mu(Y_2)\cdots\mu(Y_s).
\tag{3.3}
\]

After the adjacent opposite pair is tagged or finalized, successive
applications of (3.2), from left to right, restore

\[
                 Y_1Y_2\cdots Y_sX'.
\tag{3.4}
\]

Hence the maximal corridor immediately to the right of the active block
records, in order, every crossed block and the exact origin distance.
This removes the collision in Proposition 2.1: its intermediate is
\(AC\mu(B)B=AC11B\), not \(ACBB\).

### Lemma 3.1 (checkpoint decoder)

At every endpoint of a rewrite (3.1) or (3.2), the tape, the global phase,
and the active direction recover the tape before the current shuttle and
the current shuttle position.

#### Proof

There is only one active shuttle.  Its corridor is the maximal contiguous
word over \(\{10,11,12\}\) immediately to the right of its active block.
Apply \(\mu^{-1}\) letter by letter.  In the left-moving phase, replace

\[
                   X\mu(Y_1)\cdots\mu(Y_j)
       \quad\hbox{by}\quad
                   Y_1\cdots Y_jX.
\]

In the returning phase, undo the already restored literal prefix and put
the active block back beside its mate.  The visible tags retain the two
source extremes.  Thus both the original macro tape and the number of
crossed blocks are recovered.  \(\square\)

## 4. Noncrossing cancellation and the LIFO finalization order

Delete all \(B\)-blocks and consider the remaining balanced \(A/C\) word.
Repeatedly delete the leftmost adjacent unlike pair.  Record the pairs in
deletion order

\[
                         P_1,P_2,\ldots,P_s.
\tag{4.1}
\]

### Lemma 4.1 (noncrossing invariant)

The pairs in (4.1) are noncrossing.  When \(P_i\) is processed in the
tagging pass, every block strictly between its endpoints is either \(B\)
or a tag belonging to an earlier pair.  If the pairs are finalized in the
reverse order

\[
                         P_s,P_{s-1},\ldots,P_1,
\tag{4.2}
\]

then every block strictly between the endpoints of the current pair is
again either \(B\) or an unfinalized tag.  In particular no finalized
\(A/C\) block ever has to be crossed.

#### Proof

Adjacent deletion is the standard noncrossing cancellation: if two arcs
crossed, the later-deleted endpoints of one arc would have separated the
endpoints of the earlier adjacent pair.  When \(P_i\) becomes adjacent in
the reduced word, every earlier extreme between its endpoints has already
been deleted and tagged, while every nonextreme block is \(B\).  This is
the first assertion.

If a pair lies strictly inside another pair, it was deleted earlier.
Therefore reverse deletion order processes every outer pair before all of
its descendants.  Its interior descendants are still tagged.  Disjoint
previously finalized pairs lie outside its interval.  This proves the
second assertion.  \(\square\)

The tagging pass uses (3.1), the literal adjacent conversions

\[
 A\mid C\leadsto T_A\mid T_C,
 \qquad
 C\mid A\leadsto T_C\mid T_A,
\tag{4.3}
\]

and (3.2).  The LIFO pass uses the same corridor together with

\[
 T_A\mid T_C\leadsto C\mid A,
 \qquad
 T_C\mid T_A\leadsto A\mid C.
\tag{4.4}
\]

Equations (3.3)--(3.4) restore every intervening block literally.  After
(4.4) has been applied to every pair, the tape is the connectorwise
complement of the source tape.

## 5. A protected four-state phase/branch register

Use the ordered boundary triple

\[
          (\hbox{root},\;2m,\;0),
\]

whose physical order is the three-vertex boundary path

\[
                 \hbox{root}--2m--0.
\]

The four states

\[
 E_{00}=021,\qquad E_{01}=012,
 \qquad E_{10}=201,\qquad E_{11}=210
\tag{5.1}
\]

all have mass three.  The first index is the global pass and the second is
a local branch bit.  Use \(E_{00}\) and \(E_{10}\) as the idle states of
the tagging and finalization passes, respectively.  The literal paths are

\[
 E_{00}\leftrightarrow E_{01},
 \qquad
 E_{00}\leftrightarrow111\leftrightarrow E_{10},
 \qquad
 E_{10}\leftrightarrow E_{11}.
\tag{5.2}
\]

Every arrow is one adjacent unit transfer on the displayed boundary path.
The persistent states have root zero or two.  At the only state with root
one, the boundary coordinate also equals one; every old promotion/aperture
state with root one has boundary coordinate in \(\{0,2\}\).  Thus (5.2)
avoids the old linkage.  It is disjoint from the active \(p_1\) pair, so
the shadow clock gives every arrow its directed lift.

For the twelve ordered macro types in (3.1), total four-coordinate mass
leaves at most two types in any mass layer:

\[
 1,\;2,2,2,2,2,\;1
\]

types in masses \(1,2,3,4,5,6,7\), respectively.  Thus the literal local
mass and the second bit in (5.1) identify the ordered type.  The pass bit
determines whether a tag or an extreme is moving outward or returning.

Setup and teardown are injective.  While (5.2) is traversed, the bulk tape
is held at a decoded checkpoint, so it already determines the source and
macrostage.  Two different setup paths can meet at the hub only if their
bulk tapes agree; the deterministic cancellation rule then gives the same
pass and branch.  The hub therefore does not merge source paths.

## 6. A double sentinel reduces the atom to a bounded initialization collar

The occurrence-label part of the visible-cart atom has a uniform literal
solution once one protected double sentinel is available.  Put

\[
                              H=02.
\tag{6.1}
\]

The value \(H\) belongs to neither the macro alphabet (1.4) nor the
corridor alphabet \(\{10,11,12\}\).  Reserve two consecutive connector
blocks in the state

\[
                              H\mid H.
\tag{6.2}
\]

### Lemma 6.1 (double-head transport)

The double head (6.2) can be moved reversibly through any word over the
macro and corridor alphabets with a source/stage decoder at every state.

#### Proof

To move the head left through one block \(Y\), perform

\[
       Y\mid H_1\mid H_2
          \leadsto H_1\mid Y\mid H_2
          \leadsto H_1\mid H_2\mid Y.
\tag{6.3}
\]

Each arrow in (6.3) is a swap of two adjacent two-coordinate blocks.
The relevant four-coordinate mass is strictly between zero and eight, so
Lemma 3.1 of the shuttle note supplies a simple adjacent-transfer path.
During the first swap \(H_2=02\) is fixed; during the second \(H_1=02\)
is fixed.  Hence a unique nonalphabet block locates the active
four-coordinate window at every strict intermediate state.

For a fixed local mass there are at most two possible crossed block types:

\[
 \begin{array}{c|ccccc}
 \operatorname{mass}Y&0&1&2&3&4\\ \hline
 Y&00&01,10&20,11&21,12&22.
 \end{array}
\tag{6.4}
\]

The branch bit in (5.1) distinguishes the two possibilities.  Within one
branch the chosen local path is simple, so its literal state gives the
microstep.  At the midpoint of (6.3), the two visible \(02\) blocks with
one decoded block between them identify the head and direction.  Reversing
(6.3) moves the head right.  Iteration preserves the order of every
crossed block, and moving the head back to its fixed berth restores the
tape literally.  \(\square\)

There is one small uniqueness detail.  A four-coordinate active window
can itself equal (02\mid02) only in mass four.  In that layer choose the
following head-swap paths:

\[
 \begin{aligned}
 20|02&:2002\to2011\to1111\to0211\to0220=02|20,\\
 11|02&:1102\to1111\to0211=02|11.
 \end{aligned}
\tag{6.5}
\]

For the two mass-four corridor branches use

\[
 \begin{aligned}
 01|21&:0121\to0211\to1111\to1201\to2101\to2110=21|10,\\
 21|01&:2101\to1201\to1111\to0211\to0121\to0112=01|12.
 \end{aligned}
\tag{6.6}
\]

The tagging and finalization paths in Section 2 also avoid (0202).
Thus no strict active state creates a second disjoint double head.  Outside
mass four this is automatic by mass.  There is therefore one unique
maximal run of at least two (02)-blocks; it contains the fixed head and
locates the active region.  If an active endpoint contributes one adjacent
(02), the branch and microstep identify which end of that run is the
fixed pair.

### Theorem 6.2 (visible-cart atom from a double head)

Assume the double head (6.2) has been installed in a fixed protected
berth, with the two displaced source blocks recorded in a bounded
delimiter.  Then every rewrite (3.1), every return rewrite (3.2), and the
adjacent tagging/finalization paths (4.3)--(4.4) have a literal
occurrence-labelled realization satisfying the visible-cart atom.

#### Proof

Use Lemma 6.1 to bring the double head immediately beside the active
four-coordinate window.  Keep both \(02\) blocks fixed while traversing
any simple fixed-mass token path between the required local endpoints.
The local mass and branch bit identify the ordered endpoint type, the
fixed double head identifies the occurrence, and simplicity identifies
the microstep.  Return the head to its berth by reversing Lemma 6.1.
The checkpoint decoder then applies.  \(\square\)

Thus no twelve-case collision-free path table is needed.  The exact
remaining premise is the following bounded collar statement.

### Finite collar lemma \(\mathsf{DH}\)

At the start of the bulk pass, choose two fixed excluded source blocks

\[
                         C(a)\mid C(b),
              \qquad (a,b)\in\{0,1,2\}^2.
\]

There are nine mutually disjoint literal setup paths which replace them
by (02\mid02), end in nine distinguishable protected delimiter records
(R_{a,b}), and avoid the old linkage.  The teardown paths restore
(C^*(a)\mid C^*(b)) from (R_{a,b}) and the double head.  Every
nonterminal state retains the root flag or the finite record.

The exact mass price of setup is

\[
       4-2(a+b)\in\{4,2,0,-2,-4\};
\tag{6.7}
\]

the collar must borrow or return that amount through the proved component
mass ladder.  Teardown pays the opposite amount.  This scalar transfer is
already feasible; the content of \(\mathsf{DH}\) is the literal
nine-record, mutually disjoint setup/teardown table.

There are only nine source types for this collar.  Component-mass
connectivity supplies its scalar feasibility, and the root/\(p_1\)/boundary
register has more than nine literal states, but neither fact alone is an
occurrence-labelled collar proof.  This finite initialization/retirement
table remains to be written.

Conditional on that collar, Lemmas 3.1, 4.1, and Theorem 6.2 give a global
source/stage decoder and hence pairwise-disjoint bulk recoder paths after
the fixed-\(p_1\) lift.

## 7. The omitted \(p_1\) connector

Deleting the one connector meeting \(p_1\) changes \(\#A-\#C\) by at
most one.  Hence the bulk tape leaves at most one unmatched extreme.  The
omitted connector has the opposite charge, so the two changes have total
mass zero.  This is one bounded labelled task, not a growing defect.

The component-mass router can move its four units, and the proved
aperture-retirement collar writes the exact \(p_1\)/boundary target.  To
obtain a completely literal counterflow, that one remote unmatched block
must remain under the same visible-cart decoder while it is routed to the
collar; unlabelled component connectivity alone is not a disjointness
proof.  Thus it belongs to the same finite visible-cart interface, not to
a new macroscopic packing theorem.

## 8. Exact conclusion

The marked corridor proves that arbitrary shuttle distance, nested
cancellation, and finalization order create no growing memory or damage.
It also gives the exact counterexample to the unmarked fixed-delimiter
proof.  The double-\(02\) head solves the occurrence-labelled local cart
uniformly.  The odd writer has been reduced to:

1. a nine-type bounded initialization/retirement collar for that head;
   and
2. the same finite tag for the one omitted \(p_1\)-connector charge.

No scalar, parity, complement-pairing, noncrossing, or unbounded-distance
obstruction remains.  The complete odd counterflow should not be cited as
proved until the \(\mathsf{DH}\) collar and the bounded residual handoff
are written literally.
