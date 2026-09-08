# Odd current: a ternary zipper removes background collisions from an aligned root sweep

**Date:** 2026-08-06  
**Method:** literal first-nonquiet scan identities and reversible decoding;
no computation or search  
**Status:** unconditional marker theorem and exact reduction.  The theorem
removes the `2011 -> 2020` background-collision obstruction for every
one-way sweep admitting the aligned clock schedule in Theorem 4.1.  It does
not construct that schedule at the two endpoint collars.  A complete
boundary-partner counterflow still requires one
oppositely directed sweep, equivalently a two-root clock junction.  That
junction is not constructed here.

## 1. Scan notation

Use the boundary-last scan and contraction from
`MATH_THEOREM_ODD_QUIET_SOURCE_CLOCK_MINOR_AND_BOUNDARY_HANDOFF_GATE_20260806.md`.
On a quiet compressed digit put

\[
 q(0)=00,\qquad q(1)=20,\qquad q(2)=22.
\tag{1.1}
\]

For \(b\in\{0,2\}\), put

\[
                         c(b)=(1,b).
\tag{1.2}
\]

Thus \(c(0)=10\) and \(c(2)=12\) are active clock states in the
mass-one and mass-three rows.  If two consecutive scan pairs are written
as `left | right`, their connector joins the second coordinate on the left
to the first coordinate on the right.

Define two binary functions on a ternary digit:

\[
 \beta(a)=\begin{cases}0,&a=0,\\2,&a=1,2,\end{cases}
 \qquad
 \gamma(a)=\begin{cases}0,&a=0,1,\\2,&a=2.\end{cases}
\tag{1.3}
\]

The ordered pair \((\beta(a),\gamma(a))\) determines \(a\), since its
three possible values are

\[
                         (0,0),\quad(2,0),\quad(2,2).
\tag{1.4}
\]

## 2. The ternary clock rewrite

### Theorem 2.1 (one-step ternary zipper)

For every \(a\in\{0,1,2\}\) and \(b\in\{0,2\}\), there is a directed
two-arc rewrite

\[
              q(a)\mid c(b)
       \leadsto
              c(\beta(a))\mid(\gamma(a),b)
\tag{2.1}
\]

in the contracted scan digraph.  Written literally, the three rows are

\[
\begin{array}{rcl}
 00\mid1b&\longrightarrow&01\mid0b\longrightarrow10\mid0b,\\
 20\mid1b&\longrightarrow&21\mid0b\longrightarrow12\mid0b,\\
 22\mid1b&\longrightarrow&21\mid2b\longrightarrow12\mid2b.
\end{array}
\tag{2.2}
\]

The first arrow is a physical connector transfer and the second is the
selected edge on the earlier pair:

\[
                         01\to10,\qquad21\to12.
\tag{2.3}
\]

In particular the rewrite is injective in the ordered data \((a,b)\).

#### Proof

For \(a=0\), move one unit from the first coordinate of the right pair to
the second coordinate of the left pair.  For \(a=1\), make the same move.
For \(a=2\), move one unit in the opposite direction.  This gives the
three first arrows in (2.2).  In every row the left pair is now the first
nonquiet scan pair, so the indicated scan edge is the unique following
matching edge.  The left clock and first coordinate of the right record
are exactly \((\beta(a),\gamma(a))\), which determines \(a\) by (1.4),
while the second coordinate of the record is the old clock label \(b\).
\(\square\)

The binary zipper previously used only the first and third rows of (2.2).
The middle row is the missing identity that allows a readable clock to
cross an arbitrary ternary background rather than an all-one or binary
background.

## 3. A whole prefix is reverse-decodable

Let \(a_1,\ldots,a_j\in\{0,1,2\}\), let \(b_{j+1}\in\{0,2\}\), and put

\[
                         b_i=\beta(a_i)\quad(1\le i\le j).
\tag{3.1}
\]

The four possible record pairs in (2.1) are

\[
                         00,\quad02,\quad20,\quad22.
\tag{3.2}
\]

Assume that the initial clock is on an internal scan pair and is followed
on its right by a readable
delimiter \(\Delta\) outside this four-state record alphabet.  It can be a
second active pair supplied by the activation collar; only its being
recognizable after the record chain is used below.

### Theorem 3.1 (ternary zipper code)

Repeated use of Theorem 2.1 gives a directed path

\[
 q(a_1)\cdots q(a_j)c(b_{j+1})
 \leadsto
 c(b_1)(\gamma(a_1),b_2)\cdots
          (\gamma(a_j),b_{j+1}),
\tag{3.3}
\]

At every majority-shore vertex, the first nonquiet scan pair is the
current clock.  From that pair, the records to its right, and the untouched
suffix, one recovers:

1. the entire crossed ternary prefix \(a_1,\ldots,a_j\);
2. the old clock label \(b_{j+1}\); and
3. the current position on the zipper path.

Consequently the zipper paths obtained from distinct source words, clock
positions, or untouched suffixes are pairwise vertex-disjoint.

#### Proof

Apply (2.1) from right to left.  After the clock has crossed digit \(a_i\),
the pair immediately to its right stores \((\gamma(a_i),b_{i+1})\), while
the new clock stores \(b_i=\beta(a_i)\).  This proves (3.3).

For decoding, read \(b_1\) from the active clock.  The next record supplies
\(\gamma(a_1)\) and \(b_2\), so (1.4) recovers \(a_1\).  Continue
inductively.  The final record retains \(b_{j+1}\).  The first pair outside
the record alphabet is the delimiter, so the decoder also recovers the
starting clock position and the record-chain length.  Pairs strictly to the
left of the clock are still quiet.  Some records to the right can be
nonquiet, but they occur later in the scan, so the current clock is still
the first nonquiet pair.

Thus every majority vertex recovers its source and its stage.  Every
minority intermediate is the unique scan mate of the following majority
vertex, so a collision between minority vertices would give a collision
between majority vertices.  No vertex has the physical boundary pair as
its first nonquiet pair; hence the whole family avoids the deleted
boundary-current endpoint set.  \(\square\)

### Corollary 3.2 (the raw-convoy collision is not intrinsic)

If a long root or chip sweep is interleaved with a delimiter-equipped
zipper so that every crossed background digit is written into the record
chain, then a state on the sweep recovers the original background.  In
particular an intermediate such as `2020` cannot collide with a source
having background `(0,2)`: the clock/record signature distinguishes the
two histories.

This does not claim that every required sweep is directed under one fixed
scan.  It says that background collision, by itself, is no longer an
obstruction.

### Proposition 3.3 (the delimiter is necessary)

If starting clock positions are allowed to vary, the clock state alone is
not a sufficient tag.  Indeed the first row of (2.2), with \(b=0\), gives

\[
                         q(0)\mid c(0)
             \leadsto   c(0)\mid q(0).
\tag{3.4}
\]

The terminal on the right is literally a zero-step state whose clock
started one pair earlier.  Hence the two path families meet unless a
delimiter, activation signature, or equivalent start-position label is
retained.  The delimiter hypothesis in Theorem 3.1 is therefore
load-bearing rather than cosmetic.

## 4. Marked one-way sweeps

The preceding proof is stable under reversible work in the untouched
tail.

### Theorem 4.1 (tagged time-expansion lemma)

Between successive delimiter-equipped zipper rewrites, let the current
clock remain fixed and perform a prescribed path in the tail token graph,
disjoint from the clock pair.  Suppose that at every local time in a fixed
clock slice the map from its allowed input tails to the current tail states
is injective, and that its inverse is determined by the clock position and
local time.  Then all such interleaved source paths are pairwise
vertex-disjoint and survive in the contracted digraph.

#### Proof

The clocked-tail-minor theorem lifts every directed tail edge to a directed
two-arc path while keeping the first nonquiet clock fixed.  A majority
vertex first identifies its clock position.  Reverse the prescribed tail
operation in that slice, then apply the decoder from Theorem 3.1.  This
recovers the unique source and stage.  Minority vertices again recover from
their unique following scan mate.  The first nonquiet pair is internal, so
no lifted vertex belongs to the deleted boundary-current endpoint set.
\(\square\)

In particular, on every segment disjoint from the current clock pair, a
distinguished literal value one can be bubbled through an arbitrary
background by the reversible local swaps

\[
                         10\leftrightarrow01,
 \qquad                  11\leftrightarrow11,
 \qquad                  12\leftrightarrow21.
\tag{4.1}
\]

The zipper supplies the missing physical time/source label.  Therefore any
one-way root sweep for which the clock can be kept on an internal pair
disjoint from the current tail move, and for which every clock handoff
crosses a still-quiet pair, is macroscopically collision-free without
erasing the background into an all-one corridor.  Establishing those two
alignment conditions at the initial and terminal collars is part of the
junction in Section 8 and is not claimed here.

## 5. Why one sweep is not the boundary transposition

Let \(v_0,\ldots,v_L\) be the nonwrap coordinate path and let
\(s_i=(v_i\ v_{i+1})\).  Bubbling the distinguished endpoint value along
the whole path applies

\[
                         U=s_0s_1\cdots s_{L-1},
\tag{5.1}
\]

a cyclic rotation of all \(L+1\) coordinate values.  The physical
boundary partner instead applies only

\[
                         \tau=(v_0\ v_L).
\tag{5.2}
\]

The exact Coxeter factorization is

\[
 \boxed{
 (v_0\ v_L)=s_0s_1\cdots s_{L-1}s_{L-2}\cdots s_1s_0.}
\tag{5.3}
\]

Thus the collision-free forward sweep from Section 4 is exactly half of
the required operation.  A second sweep in the opposite index direction
must return the displaced endpoint value while leaving the transported
root at the far endpoint.

This is why the one-valued root bubble does not by itself prove the
boundary-paired basis theorem.

## 6. A sharp local reverse-handoff obstruction

The same first-nonquiet clock cannot simply be pushed to the right by the
mirror image of (2.2).

### Proposition 6.1 (no one-connector reverse zipper)

Start with an active clock \(c(b)\) on a scan pair and a quiet pair to its
right.  No single transfer across their connector can make the old clock
quiet.  Consequently no path of the form

\[
 \text{one connector transfer}\quad+\quad
 \text{one selected scan edge}
\tag{6.1}
\]

moves the first nonquiet clock one pair to the right.  This remains true
for either choice of the mass-two scan phase.

#### Proof

For \(c(0)=10\), the connector is incident with the zero in the old clock.
The only possible transfer into that zero changes the old pair to `11`;
there is no unit available to transfer out of it.  For \(c(2)=12\), the
only possible connector transfer changes the old pair to `11`.  Hence the
old pair is still nonquiet after the physical edge.

At mass two, either scan phase pairs `11` with one of `02` and `20`.
Both endpoints of the selected row are nonquiet.  The following matching
edge therefore cannot make the old pair quiet, so a later pair cannot
become first nonquiet.  \(\square\)

The obstruction is local and exact: it does not contradict a longer
four-site handoff, a preloaded shadow clock, or a change of scan root/order.

There is, however, an exact handoff as soon as the unpaired root is placed
on the other side of the old clock.

### Proposition 6.2 (root-buffered clock handoff)

Suppose an unpaired root coordinate of value one is adjacent to the first
coordinate of the old clock \(c(b)\).  Suppose also that a later scan pair
is already nonquiet, and that every pair between the old and later clocks
is quiet.  Then one physical root transfer followed by one scan edge
deactivates the old clock and hands control to the later clock:

\[
\begin{array}{rcll}
 1\mid10&\longrightarrow&2\mid00,&b=0,\\
 1\mid12&\longrightarrow&0\mid22,&b=2.
\end{array}
\tag{6.2}
\]

After the displayed transfer the later pair is the first nonquiet scan
pair, so its selected edge is the unique next matching edge.  The handoff
is therefore a directed two-arc path.  It leaves the root flag

\[
                         2-b\in\{0,2\}.
\tag{6.3}
\]

#### Proof

For \(b=0\), move the one in the first clock coordinate into the root;
the old pair becomes quiet `00`.  For \(b=2\), move the root unit into the
first clock coordinate; the old pair becomes quiet `22`.  All earlier
pairs remain quiet, so the preloaded later clock is now first nonquiet.
The physical edge reverses the shore and its selected scan edge returns to
the majority shore.  \(\square\)

There is a mirror form adapted to the geometry in which the unpaired root
lies immediately to the right of a scan pair.  With
\(\bar c(b)=(2-b,1)\), one has

\[
 \bar c(b)\mid1
   \longrightarrow
 (2-b,0)\mid2.
\tag{6.4}
\]

The transfer moves the second clock coordinate into the root.  For
\(b=0,2\), the old pair becomes respectively `20` and `00`, both quiet in
phase zero.  Hence, if a later clock has been preloaded, (6.4) followed by
its selected edge is the same directed handoff, now with the permanent
root flag equal to two.

### Corollary 6.3 (a literal sweep-direction separator)

If the forward sweep keeps this root coordinate equal to one, and the
return sweep starts with Proposition 6.2 and does not touch the root until
its terminal collar, then no vertex of the return-sweep interior equals a
vertex of the forward sweep: their root values lie in disjoint sets

\[
                         \{0,2\}\quad\text{and}\quad\{1\}.
\tag{6.5}
\]

This separates reverse majority vertices from forward minority vertices
as well.  The terminal restoration of the root to one remains part of the
two-root junction.

### Corollary 6.4 (the delimiter supplies the shadow clock)

In a delimiter-equipped zipper state, take the first nonquiet pair strictly
after the old clock.  It exists because the delimiter is nonquiet, and all
intervening pairs are quiet by definition.  Hence this pair is exactly the
preloaded later clock required in Proposition 6.2.  No additional
macroscopic clock bank is needed.

The remaining placement condition is that the unpaired root be adjacent to
the appropriate side of the old clock; the two literal forms (6.2) and
(6.4) cover the two clock orientations once that placement is achieved.

That placement can in fact be made at the initial scan-design stage.

### Proposition 6.5 (root-adjacent boundary-last scan order)

Keep the physical boundary pair last, but inspect the internal pairs from
the unpaired root inward.  Orient the first internal pair so that its first
coordinate is adjacent to the unpaired root.  Then every activation and
zipper proof from Sections 2--5 remains valid, and every promoted terminal
clock lies beside the root in the geometry of Proposition 6.2.

#### Proof

The first-nonquiet construction uses only three facts about the internal
scan list: its pairs are disjoint, consecutive listed pairs have one
physical connector for the zipper rewrite, and the physical boundary pair
is later than every internal active clock.  Reversing the list of internal
pairs preserves all three facts; reversing the ordered coordinates inside
each pair merely reflects the local tables (1.2).

Concretely, starting at the root side, take the ordered pairs

\[
 (2m-2,2m-3),(2m-4,2m-5),\ldots,(2,1),
\tag{6.6}
\]

then place the physical boundary pair last.  Coordinate \(2m-1\) is still
unpaired and is adjacent to the first coordinate \(2m-2\) of the first
pair.  The activation partition and reverse-decoding arguments are
unchanged after this relabelling.  The zipper terminates on the first pair,
so (6.2) applies literally.  \(\square\)

Together, Propositions 6.2 and 6.5 and Corollary 6.4 construct the **entry**
half of the two-root junction for the root-coded clock basis: the old clock
is deactivated, a shadow clock takes over, and the root acquires a non-one
sweep-direction flag.  This reordered scan does not automatically preserve
the later coordinate-zero aperture, whose original proof used the
boundary-adjacent pair as the first clock.  Synchronizing that aperture with
the root-adjacent order, as well as exit restoration and the directed
reflected phase profile, remains a bounded-collar problem.

## 7. The reflected sweep has a phase-clean record alphabet

There is a useful exact form of the second sweep.  On one ordered scan pair
put

\[
                         \rho(x,y)=(2-y,2-x).
\tag{7.1}
\]

This is reflection followed by literal complement.  It preserves the quiet
alphabet, with

\[
                         \rho(q(a))=q(2-a),
\tag{7.2}
\]

and sends the forward clock to the reverse clock

\[
                 \bar c(b):=\rho(c(b))=(2-b,1).
\tag{7.3}
\]

Reflect the order of the two pairs in (2.1) and apply \(\rho\) to each
pair.  With

\[
 \bar\beta(a)=\begin{cases}2,&a=0,1,\\0,&a=2,\end{cases}
 \qquad
 \bar\gamma(a)=\begin{cases}0,&a=0,\\2,&a=1,2,\end{cases}
\tag{7.4}
\]

one obtains the literal reverse-scan identity

\[
 \bar c(b)\mid q(a)
 \leadsto
 (2-b,\bar\gamma(a))\mid\bar c(\bar\beta(a)).
\tag{7.5}
\]

Here `leadsto` is directed relative to the reflected scan order.  It is not
being asserted directed relative to the original boundary-last reference
matching.

### Proposition 7.1 (phase-clean reverse records)

The record left by (7.5) is always quiet in one of the two mass-two scan
phases, determined only by the old clock label \(b\):

\[
\begin{array}{c|c|c}
b&\text{possible records}&\text{phase in which all are quiet}\\ \hline
0&20,22&0,\\
2&00,02&1.
\end{array}
\tag{7.6}
\]

#### Proof

Substitute \(b=0,2\) and \(a=0,1,2\) in (7.5).  Phase zero has mass-two
quiet state `20`; phase one has mass-two quiet state `02`; `00` and `22`
are quiet in both phases.  \(\square\)

Thus the reverse sweep has no intrinsic record-collision problem either.
It asks for a spatially controlled phase profile: a processed pair uses
phase zero when its incoming clock label is zero and phase one when that
label is two.  The boundary-locked dual-phase linkage already proves that
phase-zero and phase-one code-one states are connected disjointly away
from the physical boundary.  What is not yet proved is that these local
phase choices can be installed adaptively along the reflected zipper while
remaining one directed linkage in the original contraction.

The literal forward and reverse **majority-clock** alphabets are disjoint:

\[
                 \{10,12\}\cap\{21,01\}=\varnothing.
\tag{7.7}
\]

Consequently a forward-sweep majority vertex cannot equal a reverse-sweep
majority vertex.  The root flag in Corollary 6.3 gives full cross-sweep
separation, including minority vertices, provided the return sweep avoids
that coordinate.  Without the root flag, `01` and `21` also occur as the
minority scan mates inside a forward two-arc lift, so the disjoint clock
alphabets alone would not suffice.

## 8. The reduced positive target

The odd physical problem is therefore reduced from a macroscopic
background-packing question to the following junction.

> **Two-root zipper junction.**  Link the terminal of the forward ternary
> zipper to a clock whose scan order is reversed (or whose unpaired root is
> on the other side of the corridor), without using an installed boundary
> current endpoint.  Use the delimiter-provided shadow clock, apply the root-buffered
> handoff (6.2), support the reverse sweep in (5.3) while preserving the
> root flag, and restore the root only in the terminal collar.

If that junction exists, Theorems 3.1 and 4.1 make each sweep
reverse-decodable: every physical state recovers its sweep, clock position,
source background, and stage.  Equation (5.3) then supplies the literal
boundary transposition rather than a mere rotation.

There is one additional, load-bearing endpoint condition.  Let

\[
                         A:Q\longrightarrow A_\partial
\tag{8.1}
\]

be the proved aperture bijection and let

\[
                         J=\mathsf cR^{2^{v_2(m)}}.
\tag{8.2}
\]

For the deterministic counterflow permutation to be \(J\), the route
indexed by \(u\) must have the literal endpoint specification

\[
                 \boxed{A(Ju)\leadsto\tau A(u),}
\tag{8.3}
\]

and, after leaving \(A(Ju)\), must avoid every aperture path.  A route
\(A(u)\leadsto\tau A(u)\) has last-intersection permutation equal to the
identity and is useless for the paired-basis gate, regardless of how
well it is marked.

The reflected sweep in Section 7 contains exactly the complement part of
\(J\), while a root sweep supplies rotations.  But this document has not
proved that their composition is the conjugated terminal map

\[
                         \tau A J^{-1}A^{-1}.
\tag{8.4}
\]

If the two-root junction realizes (8.3), the one-odd-orbit theorem for
\(J\) leaves exactly the all-one socket.  The remaining issue is therefore
not an entropy shortage and not the raw `2011 -> 2020` collision.  It is a
bounded local change-of-root interface **plus** the exact endpoint-conjugacy
check (8.3) between two already readable one-way sweeps.

## 9. Scope

Proved here:

1. a literal ternary extension of the first-nonquiet zipper, conditional
   only on the readable delimiter already furnished by a two-pair
   activation collar;
2. reverse decoding and macroscopic vertex-disjointness over arbitrary
   ternary backgrounds;
3. collision-freeness of every aligned macroscopic one-way root-sweep
   interface, conditional on its two explicit clock-support conditions;
4. the exact two-sweep factorization of the boundary transposition; and
5. the impossibility of obtaining the reverse sweep from one connector
   transfer and one scan edge under the same clock; and
6. an exact root-buffered handoff to a preloaded later clock, together with
   a literal cross-sweep direction flag; and
7. an exact reflected reverse zipper whose records are quiet under the
   clock-controlled choice of the two known mass-two phases.

Not proved here:

1. synchronizing the root-adjacent entry with the coordinate-zero aperture
   and restoring the flagged root at the far collar;
2. the endpoint conjugacy (8.3) implementing the parity-perfect source
   permutation rather than the identity;
3. simultaneous compatibility of that junction with the previously
   installed fan/receiver paths; or
4. the final matching-faithful counterflow bank and its one socket.
