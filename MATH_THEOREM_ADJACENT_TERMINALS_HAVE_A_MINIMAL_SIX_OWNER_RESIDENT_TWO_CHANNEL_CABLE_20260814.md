# Adjacent Johnson terminals have a minimal six-owner resident two-channel cable

**Date:** 2026-08-14  
**Status:** exact symbolic local theorem.  Every adjacent pair of rank-`r`
Johnson owners, for `r>=4`, is joined by a six-owner owner/lower/upper-simple
two-channel cable with owner and immediate-upper q2 residence.  The cable is
phase-independent and therefore contributes zero signed q2 current.  This
solves the local two-dart topology omitted by a one-edge lead; simultaneous
D5 planting and crossing collars remain separate gates.

## 0. Outcome

Let `C,E` be adjacent rank-`r` owners in the Johnson graph on a ground set of
size `2r-1`.  There is a simple six-cycle

\[
                 C,E,P_1,P_2,Q_0,Q_1,C                         \tag{0.1}
\]

whose two `C--E` arcs are

\[
             C-E,
             \qquad C-Q_1-Q_0-P_2-P_1-E.                       \tag{0.2}
\]

Treating those arcs as the two boundary channels gives a literal
degree-two cable between the two-dart ports of `C` and `E`.  The six owners,
their six immediate-lower resources, and their six immediate-upper resources
are each distinct.  Every nonconstant coordinate on the owner trace has
cyclic run pair `(3,3)`, and every nonconstant coordinate on the
immediate-upper trace has positive/zero minima `(4,2)`.

Thus `(0.1)` is q2-biresident in the owner/upper convention used by the D5
factor.  Six owners are minimal for any nonconstant simple cyclic cable with
these q2 owner runs.

## 1. Formula

Write

\[
          H=C\cap E,\qquad C=H+z,\qquad E=H+b.                  \tag{1.1}
\]

Choose `a in H`, put `K=H-a`, choose distinct `x_1,x_2 in K`, and choose
distinct `y_1,y_2` outside `K` and outside `{a,z,b}`.  These choices exist
for `r>=4`.  Define

\[
\begin{aligned}
 P_1&=(K-x_1)+y_1+a+b,\\
 P_2&=(K-x_1-x_2)+y_1+y_2+a+b,\\
 Q_0&=(K-x_1-x_2)+y_1+y_2+z+a,\\
 Q_1&=(K-x_2)+y_2+z+a.
\end{aligned}                                                  \tag{1.2}
\]

Since `C=K+z+a` and `E=K+a+b`, the six successive exchanges in `(0.1)` are

\[
 z\leftrightarrow b,\quad
 x_1\leftrightarrow y_1,\quad
 x_2\leftrightarrow y_2,\quad
 b\leftrightarrow z,\quad
 y_1\leftrightarrow x_1,\quad
 y_2\leftrightarrow x_2.                                      \tag{1.3}
\]

Hence every consecutive pair in `(0.1)` is a Johnson edge and `(0.2)` gives
two internally disjoint channels.  The direct edge is used by one pair of
boundary darts and the five-edge return by the other; no factor edge is
reused.

## 2. Simplicity

The immediate-lower resources around `(0.1)` are

\[
\begin{array}{lll}
 K+a,&(K-x_1)+a+b,&(K-x_1-x_2)+y_1+a+b,\\
 (K-x_1-x_2)+y_1+y_2+a,&(K-x_1-x_2)+y_2+z+a,&(K-x_2)+z+a.
\end{array}                                                    \tag{2.1}
\]

Their missing-clock and active-label profiles are distinct.  The six
immediate-upper resources are

\[
\begin{array}{lll}
 K+z+a+b,&K+y_1+a+b,&(K-x_1)+y_1+y_2+a+b,\\
 (K-x_1-x_2)+y_1+y_2+z+a+b,&(K-x_2)+y_1+y_2+z+a,&K+y_2+z+a,
\end{array}                                                    \tag{2.2}
\]

and are separated by the same profiles.  Formula `(1.2)` similarly gives
six distinct owners.  Therefore the cable is owner/lower/upper-simple.

The lower and upper three-owner values are the single-port lists obtained
from the same profiles:

\[
\begin{array}{lll}
 (K-x_1)+a,&(K-x_1-x_2)+a+b,&(K-x_1-x_2)+y_1+a,\\
 (K-x_1-x_2)+y_2+a,&(K-x_1-x_2)+z+a,&(K-x_2)+a,
\end{array}                                                    \tag{2.3}
\]

and

\[
\begin{array}{lll}
 K+z+y_1+a+b,&K+y_1+y_2+a+b,
 &(K-x_1)+z+y_1+y_2+a+b,\\
 (K-x_2)+z+y_1+y_2+a+b,&K+z+y_1+y_2+a,
 &K+z+y_2+a+b.
\end{array}                                                    \tag{2.4}
\]

These are also distinct.  If the cable is installed identically in the old
and new factor states, every occurrence in `(2.3)--(2.4)` is copied, so both
signed q2 currents vanish exactly.

## 3. Residence

Every coordinate in the fixed core `K-{x_1,x_2}` and the anchor `a` is
constant.  Reading `(0.1)`, each of

\[
                         x_1,x_2,y_1,y_2,z,b                    \tag{3.1}
\]

occurs in exactly three consecutive owners and is absent from the other
three.  Thus the owner trace has exact nonconstant run pair `(3,3)`.

Direct reading of the adjacent-owner unions gives nonconstant
immediate-upper minima `(4,2)`.  These are precisely the depth-two
owner/upper residence bounds used by the resident D5 reset.

The statement is internal.  At a graft, the first two exterior exchange
supports on either side must still be disjoint from the two clock pools
`{x_1,y_1}` and `{x_2,y_2}`, or the actual mixed collar must be audited
directly.

## 4. Minimality

Any nonconstant simple cyclic Johnson cable has a coordinate whose value
changes.  If its owner trace is q2-biresident, that coordinate has a positive
cyclic run of length at least three and a zero cyclic run of length at least
three.  Hence the cable contains at least six owners.  Construction `(0.1)`
attains six.

This is an architecture-relative minimum for a self-contained cyclic
two-channel cable.  A tapped larger router may expose the two channels
without adding a separate six-cycle, and is not excluded.

## 5. D5 consequence and remaining gate

For a hard D5 row, choose a common neighbour `E` of the distance-two heads
`B,C`, different from the occupied tail.  Then `B,E` are adjacent and can be
the two marked head sockets of the 18-owner marked-C6 router, while `(0.1)`
relocates the `E` socket to the external terminal `C` using two physical
channels.

This proves local existence of the required topology.  A separate H100
replay finds, for each of the three endpoint orbits at rank seven, mutually
q1/q2-disjoint router and cable banks except at their intended boundary
owner.  It does **not** prove the cut-open splice, its crossing current, or
that all 164 cables can be made simultaneously owner/lower/upper-disjoint
from the D5 factor and from one another.  Those are now explicit finite
coinstantiation and collar/current problems rather than a missing
topological mechanism.  The tapped marked-C6 construction is stronger
locally because it realizes both D5 terminal types without a serial cable.
