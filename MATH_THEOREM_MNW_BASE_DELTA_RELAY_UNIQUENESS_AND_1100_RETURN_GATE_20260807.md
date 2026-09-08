# The base delta relay is unique, but its `1100` carry returns the `J` hole

**Date:** 2026-08-07  
**Method:** exact touching-step phases, q2 inverse multiplicities, and
incidence-context transport; no computation or search  
**Status:** unconditional local classification and signed-current theorem.
It closes the native semilength-three delta casualty, but proves that the
naive positive-`1100` carry is not support-closed in the current ten-bit
relay state.  A compound phase preparation is still required.

## 1. The six base q2 targets

Let `T_i` be the rank-five word of length six whose unique zero is in
position `i`.  The exact canonical q2 multiplicities are

\[
\begin{array}{c|cccccc}
i&1&2&3&4&5&6\\ \hline
T_i&011111&101111&110111&111011&111101&111110\\
\mu(T_i)&2&2&1&1&2&2.
\end{array}                                         \tag{1.1}
\]

The delta tuple has current

\[
 \partial_2\delta=[T_1]+[T_5]-[T_3]-[T_6].          \tag{1.2}
\]

Thus its only native support casualty is `T_3=110111`, whose unique inverse
witness is `(4,5)` at owner `110001`.

## 2. Complete one-face classification for restoring `T_3`

Every one-face restoration must create `T_3` at an owner
`T_3-\{p,q\}` at which exactly one of additions `p,q` is selected.  Endpoint
centres cannot carry q2 turns.  The exact touching-step list of internal
candidates in the post-delta factor is

\[
\begin{array}{c|c|c|c}
\{p,q\}&T_3-\{p,q\}&\text{current selected pair}&
 \text{completion}\\ \hline
\{1,6\}&010110&\{3,6\}&\text{none},\\
\{2,4\}&100011&\{2,3\}&\text{none},\\
\{2,5\}&100101&\{3,5\}&\text{core }6,\\
\{2,6\}&100110&\{2,3\}&\text{none},\\
\{4,5\}&110001&\{3,4\}&\text{reverse delta}.
\end{array}                                         \tag{2.1}
\]

For example, the scalar-ideal centre `100110` would replace addition three
by six and would have old turn `T_6`.  Its possible cores are `1,4,5`.
At the first auxiliary owner the selected additions are respectively
`\{1,6\}`, `\{2\}`, and `\{2\}`.  Core one is itself selected in the only
case containing addition six, and the other cases do not contain six.
Hence no incidence hexagon completes that desired swap.

The unique nonreversing face in (2.1) has

\[
 K=100100,\qquad\text{active labels }6,3,2.          \tag{2.2}
\]

Its owners are

\[
 Z=100101,\qquad Z_3=101100,\qquad Z_2=110100,       \tag{2.3}
\]

and its colours are

\[
 P=101101,\qquad N=111100,\qquad Q=110101.           \tag{2.4}
\]

The selected additions are

\[
 Z:\{3,5\},\qquad Z_3:\{2\},\qquad Z_2:\{6\}.     \tag{2.5}
\]

Thus the cyclic selected incidences are `Z-P`, `Z_3-N`, and `Z_2-Q`;
the complementary three are unselected.  The face is alternating.  The two
auxiliary owners are Dyck endpoints, so only `Z` contributes a q2 turn:

\[
                         T_2\longleftarrow T_3.
\]

Equivalently its current is

\[
                         \partial_2 C=[T_3]-[T_2].   \tag{2.6}
\]

The owners, colours, and incidences of `C` are disjoint from the delta
cycle.  Both switches are therefore simultaneously literal in the native
canonical factor.

### Corollary 2.1 (native closed relay)

\[
 \boxed{
 \partial_2(\delta+C)
   =[T_1]+[T_5]-[T_6]-[T_2].}                       \tag{2.7}
\]

Both negative targets in (2.7) have native multiplicity two.  Hence
`delta+C` is support-closed in the native six-coordinate factor.

## 3. Why native closure does not survive the positive context

Prefix every base target by the fixed positive context `1100`.  Put

\[
\begin{aligned}
 U&=1100T_1=1100011111,\\
 J&=1100T_2=1100101111,\\
 K_0&=1100T_5=1100111101,\\
 R_0&=1100T_6=1100111110.
\end{aligned}                                       \tag{3.1}
\]

The contextual signed current is

\[
 \boxed{+[U]+[K_0]-[R_0]-[J].}                     \tag{3.2}
\]

This is exactly the current furnished algebraically by carrying the native
circulation from its natural down-context `0011` through

\[
                         0011\longrightarrow1001
                              \longrightarrow1100.   \tag{3.3}
\]

The native circulation has fourteen signed incidence occurrences (the
eight-cycle delta support and the disjoint six-cycle support of `C`).  The
context-transport identity therefore uses at most twenty-eight transport
hexagons before cancellations.

However, native multiplicity two is not invariant under prefix context.
In the relay state after the direct `J` face, `J` has load exactly one:
the boundary-restoring face first removed its unique canonical provider and
the direct face installed one new provider.  Thus (3.2) fills `U` but
deletes the sole restored `J` occurrence.  Moreover `R_0` has canonical
load one in this context.  The native closed relay is therefore **not** a
closed ten-coordinate relay.

This is the exact return obstruction:

\[
                         U\longleftarrow J.           \tag{3.4}
\]

It cannot be removed by citing the native loads in (1.1).

## 4. The tempting reverse-alpha cancellation is algebraic only

The reverse base alpha current is

\[
                         [T_6]-[T_5].                \tag{4.1}
\]

Adding it to (2.7) gives

\[
                         [T_1]-[T_2],                \tag{4.2}
\]

and the positive contextual image would be `+[U]-[J]`.  This cancels the
extra `K_0,R_0` pair algebraically, but the required contextual reverse
alpha is not a literal independent switch in the current factor.

Indeed its contextual owner

\[
                         Z=1100100101                \tag{4.3}
\]

and contextual colours

\[
                         P=1100110101,
                         \qquad Q=1100100111          \tag{4.4}
\]

are exactly the centre and two boundary colours of the direct `J` face.
Both switches require the same incidence replacement `ZP -> ZQ`.  Before
the direct face they overlap in the same direction; after it the reverse-
alpha phase at this owner has already been consumed.  They cannot be
applied sequentially as two alternating cycles, and their binary symmetric
difference is not the sum of their signed currents.

There is an independent phase obstruction as well.  At the contextual
reverse-alpha owner `1100110100`, the canonical factor selects the endpoint
addition four, whereas the two cycle colours require additions nine and
ten.  Neither cycle incidence is selected.  Thus the whole contextual
reverse-alpha cycle is not alternating even before the shared-edge issue is
considered.

## 5. Exact remaining compound gate

After the direct `J` face, reversing the second boundary face is literal and
creates a second `J` provider.  Its q2 current is `+[J]-[B]`, where
`B=0110101111` has load two at that moment.  This would make the scalar
current `+[U]-[J]` support-safe.  But it also returns the q1 boundary to the
post-first-face, source-flipped state.

Consequently the remaining statement is not another target-current
identity.  It is the following compound incidence theorem:

> Plant the two-step `0011 -> 1100` transport prism together with the
> direct `J` face and the reversed boundary face so that the shared
> `ZP,ZQ` phase is used once, the source boundary is the phase required by
> the annulus sweep, the contextual `R_0` casualty is cancelled, and the
> final component action extends to one MNW spanning hypertree.

All scalar q2 currents needed by that statement are explicit.  What is
open is their one-factor phase and topology realization.

