# The balanced bottom owner band has fixed rank

**Date:** 2026-08-05  
**Method:** exact backward FIFO recursion; no computation or search  
**Status:** unconditional reduction.  After all owner levels from `s` upward
have been installed, the remaining bottom `s` levels are one
`(s+1)`-uniform matching problem: one task vertex and `s` owner vertices per
option.  In particular `s=2` converts the only balanced endgame into a fixed
3-uniform matching, while every earlier sequential level retains at least
threefold right-side slack.

## 1. Fixed upper state and the fresh reservoir

Fix one requested punctured copy `i`, with hull `R_i` of rank `r-1`.  Assume
that

\[
 T_s^i,T_{s+1}^i,\ldots,T_d^i                       \tag{1.1}
\]

have already been selected, where `1<=s<=d-1`.  Hence the terminal
coordinate `u_i` and the later queue labels

\[
                         x_{s+1}^i,\ldots,x_d^i               \tag{1.2}
\]

are known.  Put

\[
 Y_i=[k]\setminus
       \bigl(R_i\cup\{u_i,x_{s+1}^i,\ldots,x_d^i\}\bigr).
 \tag{1.3}
\]

Since `[k]-R_i` has size `q=k-r+1`,

\[
                         |Y_i|=q-d+s-1.                       \tag{1.4}
\]

Choose an ordered `s`-tuple of distinct elements

\[
                         (x_s^i,x_{s-1}^i,\ldots,x_1^i)
                         \in(Y_i)_s.                          \tag{1.5}
\]

Read the FIFO recurrence backward:

\[
                         T_{j-1}^i
      =T_j^i-\{b_j^i\}+\{x_j^i\},\qquad j=s,s-1,\ldots,1.
 \tag{1.6}
\]

All the resulting owners are distinct within the copy, because the
successive event labels `b_1,...,b_s,x_1,...,x_s` are distinct.

## 2. Exact bottom-band hypergraph

Let `I` be the copy set and let

\[
 F_s=\{T_j^i:i\in I, s\le j\le d\}                 \tag{2.1}
\]

be the owners already occupied by the upper levels.  Define

\[
                         A_s={ [k]\choose r}\setminus F_s.   \tag{2.2}
\]

Construct an `(s+1)`-uniform labelled multihypergraph `K_s` on the disjoint
vertex set

\[
                         I\mathbin{\dot\cup}A_s.              \tag{2.3}
\]

For every copy `i` and every tuple (1.5) for which all owners from (1.6)
belong to `A_s`, add the edge

\[
                         \{i,T_0^i,T_1^i,\ldots,T_{s-1}^i\}.
 \tag{2.4}
\]

### Theorem 2.1 (fixed-rank bottom-band equivalence)

The upper owner paths (1.1) extend to globally owner-disjoint complete FIFO
paths if and only if `K_s` has a matching saturating the task shore `I`.

#### Proof

Every complete extension supplies the tuple of its first `s` queue labels.
The backward identity (1.6) makes its task and bottom owners an edge of
`K_s`.  Global owner distinctness makes those edges a matching.

Conversely, a matching edge through copy `i` determines the unique ordered
tuple (1.5): at step `j`, the new coordinate is the unique element of
`T_(j-1)^i-T_j^i`.  Equations (1.3)--(1.6) give a legal fresh FIFO extension.
The matching makes all bottom owners distinct across copies, while (2.2)
makes them distinct from every upper owner.  \(\square\)

Before the upper owner bank `F_s` is deleted, every task has exactly

\[
                         (q-d+s-1)_s                           \tag{2.5}
\]

labelled options, counted with their ordered-tuple realizations.  Thus the
local supply is polynomial of degree `s` in
\(q=\Theta(k)\) and is enormous for every fixed `s`.

## 3. The two-level endgame

For `s=2`, put

\[
                         y=q-d+1.                              \tag{3.1}
\]

Every copy has `y(y-1)` raw ordered choices, with

\[
 \begin{aligned}
 T_1&=T_2-\{b_2\}+\{x_2\},\\
 T_0&=T_2-\{b_2,b_1\}+\{x_2,x_1\}.                         \tag{3.2}
 \end{aligned}
\]

The completion hypergraph is 3-uniform:

\[
                         \{i,T_0,T_1\}.                       \tag{3.3}
\]

This is the smallest band which couples the balanced last level to one
buffer level.  It retains a quadratic option menu but has fixed edge size,
so no growing-uniformity theorem is needed for this endgame.

## 4. Exact size balance

Let

\[
                         H=|I|,\qquad W={k\choose r},        \tag{4.1}
\]

and use the optimal copy count

\[
                         H=\left\lfloor {W\over d+1}\right\rfloor
                           +O(W/d^2).                          \tag{4.2}
\]

The installed levels `s,s+1,...,d` occupy `(d-s+1)H` owners.  Hence

\[
 \begin{aligned}
 |A_s|
   &=W-(d-s+1)H\\
   &=sH+O(W/d).                                             \tag{4.3}
 \end{aligned}
\]

The bottom matching needs exactly `sH` owner vertices.  Thus (4.3) is the
correct scalar balance, with only the already budgeted separator bank left
over.

For `s=2`, all sequential levels `j>=2` have right-to-left ratio at least
three before the next matching is selected.  The final fixed-rank problem
then consumes two owners per task from a bank of size `2H+O(W/d)`.

## 5. Sharpened proof target

It is enough to prove the following two statements with a total of
`O(W/d^2)` discarded copies.

1. **Slack-level extension.**  Install levels `d-2,d-3,...,2` while
   preserving the last-two hull reservation and enough pseudorandomness in
   the residual owner bank.
2. **Bottom 3-graph matching.**  In the resulting `K_2`, find a matching
   saturating all remaining tasks.

The second statement is a fixed-uniformity, task-partite matching problem
with quadratic local menus.  The first is a sequence of ordinary bipartite
Hall problems with at least threefold size slack.  This is strictly weaker
than the former connected integral growing-rank macro-factor theorem.

Topology is still downstream: after owner-disjoint copies exist, the
terminal `Sym(h)` switches can merge cycle components without changing any
owner or lower resource.

## 6. Dependencies

The complete backward-SDR factorization is in

`MATH_THEOREM_LEVEL_STRATIFIED_OWNER_SDR_REDUCTION_20260805.md`.

The last-two hull alteration is in

`MATH_THEOREM_OWNER_HULL_OBSTRUCTION_AND_TERMINAL_ALTERATION_20260805.md`.
