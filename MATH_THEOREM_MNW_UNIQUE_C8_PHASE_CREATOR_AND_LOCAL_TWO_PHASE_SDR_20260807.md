# The unique MNW boundary phase creator is a `C_8`, and it is locally compatible with the source `C_8` in opposite SDR phases

**Date:** 2026-08-07  
**Method:** Boolean-incidence detour normal form and exact touching phases;
no computation or search  
**Status:** unconditional finite local theorem.  It constructs the unique
shortest creator in the leaf-boundary-preserving detour class and proves
that its old/new banks and those of the
fused source cycle form a valid two-phase partial ordered-SDR switch.  The
creator has one terminal q2 casualty, so a support-closed global extension
is still required.

## 1. Leaf notation

Put

\[
\begin{aligned}
 K&=0010001101,\\
 X&=K+1=1010001101,\\
 X_2&=K+2=0110001101,\\
 X_9&=K+9=0010001111,
\end{aligned}
\]

and

\[
 R=K+12=1110001101,qquad
 M=K+29=0110001111,qquad
 Q=K+19=1010001111.                                \tag{1.1}
\]

The leaf transport hexagon is

\[
 X-R-X_2-M-X_9-Q-X,                                \tag{1.2}
\]

with status word `101010`.  Its selected source edge is

\[
                         e_*=X_2M.                  \tag{1.3}
\]

The fused contextual source cycle `H_0 triangle H_1` also contains `e_*`
as a selected edge.  Hence those two current orientations cannot be put in
opposite ordered-SDR phases.

The correct phase creator must avoid `e_*` while changing the other two
selected leaf edges `XR` and `X_9Q`.

## 2. All shortest detours avoiding `e_*`

Retain the five-edge outside path

\[
                         X-R\quad\cdots\quad M-X_9-Q-X            \tag{2.1}
\]

from (1.2), and replace the two-edge path `R-X_2-M` by a four-edge
incidence path.  Any resulting simple `C_8` has the form

\[
 X-R-Y_1-S-Y_2-M-X_9-Q-X,                           \tag{2.2}
\]

where, for one `s in K`,

\[
 Y_1=R-s,qquad Y_2=M-s,qquad
 S=K-s+1+2+9.                                      \tag{2.3}
\]

### Lemma 2.1 (detour normal form)

Equations (2.2)--(2.3) list every simple length-eight incidence cycle
which contains `XR` and `X_9Q`, uses the outside path (2.1), and avoids
`e_*`.

### Proof

The first new owner is a rank-five facet `Y_1=R-s`; avoiding `X` forces
`s ne 2`.  The last new owner is `Y_2=M-t`.  For `Y_1,Y_2` to have a
common rank-six neighbour, they must differ in exactly one coordinate.
The fixed sets `R=K+1+2` and `M=K+2+9` already differ by `1` versus `9`.
Deleting different elements of `K` would introduce two further
differences, while deleting `1,9`, or `2` either repeats a vertex or
repeats `Q`.  Hence `s=t in K`, and their union is the set `S` in (2.3).
This proves necessity; direct substitution proves sufficiency. \(\square\)

Since

\[
                         K=\{3,7,8,10\},             \tag{2.4}
\]

there are four formal detours.

## 3. Exact alternation classification

For (2.2) to alternate in the current gamma--alpha factor, the required
new conditions are

\[
 Y_1S\text{ selected},\quad Y_1R\text{ unselected},
 \qquad
 Y_2M\text{ selected},\quad Y_2S\text{ unselected}.              \tag{3.1}
\]

These are exactly the auxiliary-owner conditions in the complete
source-boundary-restoring hex classification.  That classification proves
that among `s in {3,7,8,10}` only `s=3` satisfies (3.1).

For `s=3`, put

\[
 Y_1=1100001101,qquad
 S=1100001111,qquad
 Y_2=0100001111.                                   \tag{3.2}
\]

Then

\[
 \boxed{
 C_{\rm pc}=X-R-Y_1-S-Y_2-M-X_9-Q-X}               \tag{3.3}
\]

has status word

\[
                         10101010.                  \tag{3.4}
\]

### Theorem 3.1 (unique shortest leaf-boundary detour creator)

`C_pc` is the unique alternating `C_8` in the detour class of Lemma 2.1.
Its symmetric-difference current is exactly the current of `H_leaf`
followed by the unique nonreversing source-boundary-restoring hexagon.

In particular, it repairs the destination incidence, restores the source
incidence `e_*`, and avoids toggling `e_*` in its net edge bank.

Its exact q2 current is

\[
 \boxed{
 \partial_2 C_{\rm pc}
   =[1010101111]-[1100101111].}                    \tag{3.5}
\]

The negative target in (3.5) has one provider, so `C_pc` is not by itself
q2-support safe.

The uniqueness assertion is deliberately limited to creators retaining
the five-edge outside leaf path (2.1).  A different `C_8` which changes
additional boundary or rail incidences is not classified here.

## 4. The source `C_8` and phase creator form a valid two-phase partial switch

Write the contextual source cycle as

\[
\begin{aligned}
 C_{\rm src}={}&01O_a-01A-01O_2-01D\\
               &-01O_3-01B-01O_c-01C-01O_a,
\end{aligned}                                      \tag{4.1}
\]

with old bank consisting of the first, third, fifth, and seventh edges in
this order.  Its first old edge is `X_2M=e_*`.

Give `C_src` phase zero and `C_pc` phase one.  Their old banks are

\[
\begin{aligned}
 O^0={}&\{X_2M, (01O_2)(01D),
              (01O_3)(01B), (01O_c)(01C)\},\\
 O^1={}&\{XR, Y_1S, Y_2M, X_9Q\}.                \tag{4.2}
\end{aligned}

Their new banks are the complementary four edges of (4.1) and (3.3).

### Theorem 4.1 (local ordered-two-SDR compatibility)

The four sets `O^0,N^0,O^1,N^1` satisfy the local-simplicity hypotheses of
the two-phase balanced-switch theorem:

1. each old and new bank is a matching;
2. no old edge and no new edge is repeated between phases;
3. at every vertex, at most one packet of each phase is incident; and
4. the only shared vertex of the two packets is the colour `M`, where the
   phase-zero replacement is
   `X_2M -> (01O_2)M` and the phase-one replacement is
   `Y_2M -> X_9M`.

Consequently, **if** one ordered two-SDR extends the old banks (4.2) in the
declared phases and avoids both new banks, the two cycles may be switched
simultaneously and the result is again a spanning simple two-factor.

### Proof

Every alternating cycle contributes disjoint old edges and disjoint new
edges.  Comparing the literal vertex lists (3.3) and (4.1), the only common
vertex is `M`; the four incident edges displayed in item 4 are distinct.
Thus the family is locally simple.  Apply the balanced-union switch
theorem. \(\square\)

This is a local compatibility theorem, not a proof that the prescribed
partial matching pair extends globally or has the required socket
permutation.

## 5. What remains

Theorem 4.1 removes the immediate shared-edge obstruction: the correct
extra circuit is not `H_leaf` itself but the unique combined creator
`C_pc`.  Three finite rows remain for a complete ten-bit module:

1. extend (4.2), the remaining B8 transport phases, and the inherited
   connector marks to one ordered two-SDR;
2. repair the unit q2 casualty `1100101111` without reopening another
   unit target; and
3. certify the combined occurrence-level socket permutation, not merely
   degree two.

Thus the smallest phase geometry is now explicit.  The remaining
obstruction is support-closed completion and global coloured matching, not
the existence of a boundary phase creator.
