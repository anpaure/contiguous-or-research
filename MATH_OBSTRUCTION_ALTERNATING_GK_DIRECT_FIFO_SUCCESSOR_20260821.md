# Canonical alternating GK first successors admit no FIFO cycle

**Status (2026-08-21).**  The scoped obstruction below is proved.  It rules
out the direct proposal which repeatedly emits the first upward
Greene--Kleitman successor of the current middle source and drops the oldest
letter of its FIFO window.  In fact, every such trajectory stops after at
most `b^2` updates.  The stronger shifted-prefix equations are therefore
irrelevant: the first-successor equation alone is already acyclic.

This is not an obstruction to the integral Boolean retired-chain matching,
to packing different chains into product atoms, or to changing/conjugating
the linear order between atoms.  It applies to one fixed alternating linear
coordinate order and its canonical GK successor map.

## 1. The first GK addition

Fix the coordinate order

\[
             A_1,B_1,A_2,B_2,\ldots,A_b,B_b              \tag{1.1}
\]

and identify it with the integers `1,...,2b`.  For a rank-`b` set `S`, let

\[
 h_S(j)=2|S\cap[1,j]|-j,\qquad 0\le j\le2b.              \tag{1.2}
\]

Thus a member of `S` is an up-step and a nonmember is a down-step, and
`h_S(0)=h_S(2b)=0`.  Standard Greene--Kleitman bracketing pairs every
down-step with the latest unpaired up-step to its left.  If the chain through
`S` has a nonempty upward part, its first added coordinate `f(S)` is the
rightmost unpaired zero.  Equivalently,

\[
 f(S)=\min\{j:h_S(j)=\min_i h_S(i)\},                     \tag{1.3}
\]

where the common minimum is negative.

### Lemma 1.1 (strictly below the current maximum)

Whenever `f(S)` is defined,

\[
                         \boxed{f(S)<\max S.}              \tag{1.4}
\]

#### Proof

At `j=f(S)`, the walk has just attained a negative global minimum.  It ends
at height zero, so after `j` it must contain an up-step.  That later
coordinate belongs to `S`, proving (1.4).  \(\square\)

## 2. FIFO acyclicity

An ordered FIFO state is a tuple

\[
 q_t=(y_{t-b+1},\ldots,y_t)                               \tag{2.1}
\]

of `b` distinct coordinates, with underlying source `S_t`.  The direct GK
successor rule is

\[
 y_{t+1}=f(S_t),\qquad
 q_{t+1}=(y_{t-b+2},\ldots,y_t,y_{t+1}).                  \tag{2.2}
\]

Because `f(S_t)` is outside `S_t`, the next tuple again has distinct
entries.  Put `M_t=max S_t`.

### Theorem 2.1 (no direct-successor FIFO cycle)

Along every trajectory on which (2.2) is defined,

\[
 M_{t+1}\le M_t,
 \qquad
 M_{t+b}<M_t                                                   \tag{2.3}
\]

whenever the next `b` updates exist.  Consequently (2.2) has no directed
cycle, and every trajectory contains at most `b^2` defined updates.

#### Proof

Lemma 1.1 says that the appended coordinate is strictly smaller than the
current maximum, so one update cannot increase `M_t`.  The occurrence of
`M_t` already in the queue is dropped within the next `b` FIFO updates.
Before it is dropped no update can append it, because every appended
coordinate is strictly below the then-current maximum `M_t`.  After it is
dropped, every remaining or newly appended coordinate is strictly below
`M_t`.  This proves the second inequality in (2.3).

There can be no cycle because its integer maximum would have to decrease
strictly after every `b` steps.  Also `b\le M_t\le2b` for every `b`-set.
If `b^2` consecutive updates exist, applying (2.3) in `b` blocks gives
`M_{t+b^2}\le b`, hence `S_(t+b^2)=[1,b]`.  Its word is `1^b0^b`, all
coordinates are paired, and `f` is undefined.  Thus no further update
exists.  \(\square\)

### Corollary 2.2 (the shifted-prefix bypass fails)

Suppose the GK upward additions from `S` are
`a_1(S),a_2(S),...`.  Any proposed physical lift satisfying

\[
 S_{t+1}=S_t-\{y_{t-b+1}\}+\{a_1(S_t)\},
 \qquad
 a_j(S_{t+1})=a_{j+1}(S_t)\quad(1\le j<H)                 \tag{2.4}
\]

also satisfies (2.2).  Hence it has no cyclic FIFO realization, regardless
of the depth `H` of the second condition.  In particular it cannot serialize
an exponential family of middle sources; its maximal run is only `O(b^2)`.

The obstruction is caused by the fixed linear boundary of canonical GK
bracketing.  A construction using product-atom translations, atom-dependent
conjugations, or a different successor map is outside its scope.

## 3. H100 audit

The companion checker
`scratch/audit_gk_fifo_successor_cycles_20260821.py` constructs the canonical
GK additions literally.  For every ordered distinct rank-`b` queue through
`b=6` (up to `P(12,6)=665280` states), it verifies (1.3)--(1.4), the
one-step maximum inequality, strict descent over every defined `b`-step
block, the `b^2` stopping bound, and absence of directed cycles.  It also
measures the shifted-prefix compatibility depth on every cycle; there are no
cycles even before that filter is imposed.  The theorem is the analytic
argument above, not a finite extrapolation.
