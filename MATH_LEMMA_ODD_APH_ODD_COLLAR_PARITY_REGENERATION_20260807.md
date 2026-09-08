# Odd-APH regeneration can be made collar-parity visible

**Date:** 2026-08-07  
**Scope:** repair target for equation (5.3) of the projection-coded odd-APH
candidate  
**Method:** two boundary transfers and connectivity of bounded-composition
layers; no computation or search  
**Status:** unconditional abstract lemma; its application requires the two
stated boundary-aperture checks.

## 1. Two-segment token graph

Let a capacity-two coordinate path be split at one physical edge into a
left segment `L` and a right segment `R`.  A state is `(x,y)`, where every
coordinate lies in `{0,1,2}`.  A graph edge transfers one unit between two
adjacent coordinates.

Write `|x|,|y|` for the segment masses.  Edges internal to one segment
preserve both masses; the one edge across the split changes them by one in
opposite directions.

For every segment length `a` and every `0<=s<=2a`, the capacity-two
fixed-mass graph

\[
             \{z\in\{0,1,2\}^a:|z|=s\}             \tag{1.1}
\]

is connected.  One proof moves units greedily along adjacent edges from
left to right until the lexicographically first packed state is reached;
reversing one such path and following another joins any two states.

## 2. Parity-visible two-transfer lemma

### Lemma 2.1

Let `(x_0,y_0)` and `(x_1,y_1)` have the same total mass and suppose

\[
                         |y_1|-|y_0|=2\epsilon,
                  \qquad\epsilon\in\{-1,+1\}.       \tag{2.1}
\]

Assume:

1. one boundary transfer in direction `epsilon` is legal at the source,
   taking `(x_0,y_0)` to `(u_0,v_0)`; and
2. one boundary transfer in the same direction is legal into the target,
   taking `(u_1,v_1)` to `(x_1,y_1)`.

Then there is a simple path

\[
 (x_0,y_0)\longrightarrow(u_0,v_0)
   \leadsto(u_1,v_1)\longrightarrow(x_1,y_1)         \tag{2.2}
\]

whose strict interior has constant right-segment mass

\[
                         |v|=|y_0|+\epsilon.         \tag{2.3}
\]

In particular, if both endpoint right masses are even, every strict
interior state has odd right mass.

#### Proof

After the first boundary transfer,

\[
 |v_0|=|y_0|+\epsilon,\qquad
 |u_0|=|x_0|-\epsilon.
\]

Because the last boundary transfer has the same direction and ends at a
state whose right mass is `|y_0|+2 epsilon`, its predecessor satisfies

\[
 |v_1|=|y_1|-\epsilon=|y_0|+\epsilon,
 \qquad |u_1|=|u_0|.                                 \tag{2.4}

Use only edges internal to `L` and `R` between these two states.  By (1.1),
the product of the two required fixed-mass segment layers is connected, so
there is a path from `(u_0,v_0)` to `(u_1,v_1)`.  Choose it simple.  It has
the constant segment masses in (2.3).  The two endpoint states have right
mass differing by one from every interior state, so neither can reappear
inside.  Concatenation proves the claim. \(\square\)

## 3. Application to the odd-APH collar update

In the candidate regeneration

\[
                    X|P_r|K_i\leadsto H|P_r|K_{i+1}, \tag{3.1}
\]

take `L=X|P_r` and `R=K_i`.  Every macro collar state has even mass, and a
nonzero task changes collar mass by exactly two.  Therefore Lemma 2.1 gives
an occurrence-visible regeneration path as soon as the two boundary
transfers can be opened:

* the preceding and following train sweeps keep an even-mass collar;
* every strict state of (2.2) has an odd-mass collar;
* within (2.2), simplicity gives the microstep.

This removes the circular sentence "the task record selects the
regeneration phase": collar parity itself selects the phase.

The only remaining local checks are literal apertures at the physical
`P_r|K` boundary.  If the collar gains mass, the pilot-side boundary digit
must be positive and the collar-side digit below capacity at the first and
last transfer.  If the collar loses mass, the reverse inequalities are
required.  The pilot rows

\[
                 P_0=01,\qquad P_1=10,\qquad P_2=21 \tag{3.2}
\]

show that `P_1` is the only automatic pilot-side failure when the collar is
on its right: it blocks the first transfer of a gain and the last transfer
of a loss.  It can be addressed only by a separately audited pre- or
post-normalization (for example `10 <-> 01` while the new task ticket is
literal) or by reversing the local berth orientation.

Likewise the collar endpoint family must be chosen with an open boundary
digit.  That is an endpoint-design condition, not a connectivity problem.
No claim is made here that the current candidate already supplies these
apertures.

### Lemma 3.1 (a simultaneous collar aperture family)

For each even collar mass `s in {0,2,4,6,8}`, one may choose three labelled
states (allowing coincidence at the two extreme masses) whose pilot-side
boundary digit is

\[
 b(s)=\begin{cases}
 0,&s=0,\\
 1,&s=2,4,6,\\
 2,&s=8.
 \end{cases}                                          \tag{3.3}
\]

One explicit table is

\[
\begin{array}{c|ccc}
s&r=0&r=1&r=2\\ \hline
0&0000&0000&0000\\
2&1100&1010&1001\\
4&1201&1120&1012\\
6&1122&1212&1221\\
8&2222&2222&2222.
\end{array}                                           \tag{3.4}
\]

For every gain transition `s -> s+2`, the source boundary digit is below
capacity and the target boundary digit is positive.  For every loss
transition `s -> s-2`, the source digit is positive and the target digit is
below capacity.  Hence the collar side of both boundary apertures in Lemma
2.1 is simultaneously feasible for every legal signed schedule.

#### Proof

Every row in (3.4) has the displayed mass and the boundary digit in (3.3).
The four aperture inequalities are the strict monotonicity statements

\[
             b(s)<2,\quad b(s+2)>0,
       \qquad b(s)>0,\quad b(s-2)<2,                 \tag{3.5}
\]

in their respective legal ranges. \(\square\)

Thus no growing collar case split is needed.  Once a task ticket is
literal, an arbitrary old collar of the same mass can be moved by a simple
fixed-mass collar path to its labelled state in (3.4); the old collar is
left immediately and need not recur.  This preliminary normalization still
needs the ordinary translated-path occurrence audit, but all subsequent
collar-side apertures are automatic.

On the pilot side, rows `P_0` and `P_2` already open both directions.
For a gain in row `P_1`, the one internal move

\[
                           10\longrightarrow01       \tag{3.6}
\]

opens the first transfer; the odd-collar interior can be arranged to end at
a predecessor whose last transfer writes `P_1=10`.  For a loss, the first
transfer is already open, but the odd-collar path ends by writing `01`; use
the reverse `01 -> 10` only after the second boundary transfer.  Consequently
the only remaining aperture-specific occurrence row is the appropriate
even-collar pre- or post-normalization (3.6), not the eight-coordinate
interior.

## 4. Exact gain

Equation (3.1) no longer needs an arbitrary eight-coordinate path-bank
disjointness theorem.  It needs only:

1. an occurrence audit for the preliminary collar normalization to (3.4);
   and
2. an occurrence audit for the `P_1` gain/loss normalization (3.6).

Once those are proved, odd collar mass separates the complete regeneration
interior from every even-collar train phase, uniformly over all translated
task occurrences.
