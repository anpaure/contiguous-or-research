# The full rigid-`C6` rotation orbit is serially legal but never a topology fusion

**Date:** 2026-08-05  
**Method:** literal PBBS shape/voltage calculus and cut-path permutations;
no computation or search  
**Status:** unconditional for `m>=4`.  The `n=2m+1` rotated copies of the
canonical single-soliton clean `C6` may be applied consecutively despite
their shared owners.  Their final endpoint permutation is explicit.  The
result has `1+gcd(n,3)` components, never one.  The graph-level serial
handoff is not a complete occurrence-state handoff, and full rotation does
not give a context-free all-upper current cancellation.

## 1. The rotated packet family

Work on `Z_n`, where

\[
                         n=2m+1,\qquad m\ge4.
\]

For the canonical rigid packet put

\[
 K=\{1,\ldots,m-2\},\quad
 (a_0,a_1,a_2)=(m-1,m,m+1),\quad c=0,
\]

and

\[
 P_i=K+a_i+a_{i+1},\qquad Q_i=K+a_i+c.
\]

Let `rho` be coordinate rotation and write

\[
 P_i(t)=\rho^tP_i,\qquad Q_i(t)=\rho^tQ_i.
\]

At phase `t`, the old and new directed edges are

\[
 E_i(t):P_i(t)\longrightarrow Q_i(t),\qquad
 N_i(t):P_i(t)\longrightarrow Q_{i+1}(t).       \tag{1.1}
\]

The two key literal overlaps are

\[
                         Q_0(t)=P_0(t-1),
 \qquad                  Q_1(t)=P_2(t-1).        \tag{1.2}
\]

The first is the consecutive-interval single-soliton identity.  The second
follows directly from

\[
 Q_1=\{0,1,\ldots,m-2,m\}=\rho^{-1}P_2.
\]

## 2. Every descending phase is a legal next switch

### Theorem 2.1 (serial graph composability)

Starting from the PBBS factor, apply the clean `C6` switches in the order

\[
                         t,t-1,t-2,\ldots,t-(n-1). \tag{2.1}
\]

Every switch is literally legal when it is reached.  Every intermediate
graph is a simple directed two-factor.  Moreover the q1, upper-q1 and
selected-q2 multisets remain exact at every intermediate step.

#### Proof

The spatial orbits of `E_0,E_1,E_2` are disjoint.  The first lies on the
single-soliton shape, while `E_2` and `E_1` occupy respectively the rooted
two-soliton shapes `A_1` and `B_(m-2)`.  Rotation changes the root, not the
shape.  Each orbit has length `n`.  Thus no not-yet-used old edge is removed
by an earlier phase.

The only consecutive shared owners needed for the descending order are
(1.2).  After phase `t`, the old incoming edge at `P_0(t-1)=Q_0(t)` has
changed from `E_0(t)` to `N_2(t)`, while its outgoing edge `E_0(t-1)` is
untouched.  Likewise the old incoming edge at `P_2(t-1)=Q_1(t)` has changed
from `E_1(t)` to `N_0(t)`, while `E_2(t-1)` is untouched.  The third old edge
`E_1(t-1)` is elsewhere and is untouched.  Hence all three old edges of the
next packet remain present.

At the two shared owners the companion **edge occurrence** changes, but its
q1 row value does not:

\[
 \begin{aligned}
  E_0(t)&\text{ and }N_2(t)&&\text{both have row }R_0(t),\\
  E_1(t)&\text{ and }N_0(t)&&\text{both have row }R_1(t).
 \end{aligned}                                      \tag{2.2}
\]

The companion at `P_1(t-1)` is unchanged.  Therefore the authenticated
common-deletion q2 calculation applies again at phase `t-1`.  Induction gives
q1/q2 exactness throughout.

The new edge types are

\[
 \begin{aligned}
 N_0(t)&:P_0(t)\longrightarrow P_2(t-1),\\
 N_2(t)&:P_2(t)\longrightarrow P_0(t-1),\\
 N_1(t)&:P_1(t)\longrightarrow Q_2(t).
 \end{aligned}                                      \tag{2.3}
\]

Their endpoint shape types are distinct except for the two displayed
`P_0--P_2` families.  An undirected equality between `N_0(t)` and `N_2(s)`
would force simultaneously `t=s-1` and `t=s+1` modulo the odd number `n`,
which is impossible.  Thus no new edge is duplicated.  Every switch replaces
one incident edge at each of its six endpoints, so degree two and simplicity
hold at every step.  `square`

The overlap in (1.2) is therefore a genuine **graph-state** handoff, not a
collision.

## 3. The residual paths in the two-soliton cycle

Let `p=2m-3` be the two-soliton shape-cycle length.  In the rooted shape
notation, the `g=f^2` transitions are

\[
 \begin{array}{ll}
 A_j\to A_{j+1}&\text{with root shift }-1,quad 1\le j<m-1,\\
 A_{m-1}\to B_1&\text{with root shift }-3,\\
 B_j\to B_{j+1}&\text{with root shift }-1,quad 1\le j<m-2,\\
 B_{m-2}\to A_1&\text{with root shift }-1.
 \end{array}                                      \tag{3.1}
\]

Here `P_2(t)` is `A_1` with root `t`, `Q_2(t)` is `A_2` with root `t-1`,
and `P_1(t)` is `B_(m-2)` with root `t`.

After all `E_1(t),E_2(t)` are cut, the equality
`Q_1(t)=P_2(t-1)` gives a zero-length residual path between those two
consecutive cut edges.  The other residual path starting at `Q_2(t)` follows

\[
 A_2,A_3,\ldots,A_{m-1},B_1,\ldots,B_{m-2}.       \tag{3.2}
\]

It has `p-2=2m-5` unchanged edges.  Its total root shift is

\[
 -(m-3)-3-(m-3)=-2m+3\equiv4\pmod n.             \tag{3.3}
\]

Since the starting root is `t-1`, its terminal owner is

\[
                         P_1(t+3).                 \tag{3.4}
\]

Thus the remaining old edges of the two-soliton component partition into
`n` directed paths

\[
                         H_t:Q_2(t)\leadsto P_1(t+3). \tag{3.5}
\]

The edge count is `n(p-2)`, as required after deleting `2n` edges from the
old `np`-cycle.

## 4. Exact endpoint permutation

### Theorem 4.1 (full-orbit topology)

After all `n` rotated switches, the final two-factor has exactly

\[
                         \boxed{1+\gcd(n,3)}        \tag{4.1}
\]

components on the two old PBBS components.

#### Proof

The old single-soliton cycle consists entirely of the `E_0(t)`, so it has no
residual edge.  By (2.3), the `N_0,N_2` edges form the two-edge transitions

\[
 P_0(t)\xrightarrow{N_0(t)}P_2(t-1)
       \xrightarrow{N_2(t-1)}P_0(t-2).           \tag{4.2}
\]

Their return permutation on phase labels is

\[
                         t\longmapsto t-2.         \tag{4.3}

\]

Since `n` is odd, this is one orbit.  Hence all `P_0` and `P_2` owners form
one directed cycle.

The remaining new edge is `N_1(t):P_1(t)->Q_2(t)`.  Following it by the
residual path (3.5) gives

\[
                         P_1(t)\longmapsto P_1(t+3). \tag{4.4}
\]

The phase permutation `t->t+3` has `gcd(n,3)` orbits.  These give exactly
the remaining components.  Equations (4.3)--(4.4) use every new edge and
every residual old path, proving (4.1).  `square`

### Corollary 4.2 (sharp topology no-go)

The full rotation orbit never fuses the two old components into one:

\[
 \#\text{components}=
 \begin{cases}
  2,&3\nmid n,\\
  4,&3\mid n.
 \end{cases}                                      \tag{4.5}
\]

It is topology-neutral when `3` does not divide `n` and splits the
two-soliton residue into three cycles when `3` divides `n`.

## 5. Why the complete-state coboundary theorem does not apply

The next packet is exposed as a graph switch, but not as the same complete
occurrence-labelled input state.  At `P_0(t-1)`, the input companion
occurrence expected in the untouched rotation is `E_0(t)`, whereas after
the preceding switch it is `N_2(t)`.  These edges have the same q1 value
`R_0(t)` but different tails (`P_0(t)` versus `P_2(t)`) and different path
histories.  At `P_2(t-1)`, `E_1(t)` is similarly replaced by `N_0(t)`.

Hence

\[
                  D^+(\mathcal P_t)\ne
                  \rho^{-1}D^-(\mathcal P_t)      \tag{5.1}
\]

as a complete occurrence-labelled state.  Equality of immediate row values
is enough for Theorem 2.1 above, but not for the cyclic-orbit coboundary
theorem.  A separate literal transport of the changed histories would be
needed.

There is a second physical obstruction to stamping the known minimal
common-history source decoration on the entire orbit.  The `E_0(t)` form
`n` consecutive transitions around the single-soliton rail.  A run of
`d+1` consecutive minimal two-set decorations forces

\[
                         r-2\le2d.                 \tag{5.2}
\]

In the OR-word regime `d=Theta(sqrt r)`, this fails for all sufficiently
large `r`.  Thus the exact all-lower per-packet decoration cannot simply be
overlaid on this full consecutive orbit.

## 6. Necklace averaging also does not close the full fan universally

For every **individually prospectively decorated** rigid packet, owner,
q1, q2 and every strict-lower current are already zero before rotation.
Rotation adds nothing to those rows.  Arbitrary upper contexts are different.

At the first context-dependent upper width, attach a private prefix label
`p=2m` in one role.  The packet changes

\[
 \begin{aligned}
 T^-&=\{0,1,\ldots,m-1,m+1,2m\},\\
 T^+&=\{0,1,\ldots,m,2m\}.
 \end{aligned}                                    \tag{6.1}
\]

The second set is one cyclic occupied run of length `m+2`; the first has a
run of length `m+1` and a separated singleton.  They belong to different
binary-necklace classes.  Therefore the signed necklace coefficient of this
one-packet upper current is nonzero, and its full coordinate-rotation orbit
cannot cancel it.

Consequently the rigid full orbit has no context-free complete-fan current
theorem.  A specially planted construction may still keep protected upper
witnesses away from all cuts or transport an independently complete upper
bank; rotation averaging alone does not do so.

## 7. Verdict

The single-soliton overlap is useful but insufficient:

1. all `n` rigid `C6` graph moves are serially composable;
2. q1, upper-q1 and selected q2 remain exact throughout;
3. the exact endpoint phase maps are `t->t-2` and `t->t+3`;
4. the final component count is `1+gcd(n,3)`, never one;
5. the complete occurrence-state handoff required for fan coboundary
   telescoping fails; and
6. full-orbit necklace averaging has an explicit arbitrary-upper
   obstruction.

Thus the full rigid rotation orbit is a sharp topology no-go, not the missing
PBBS regenerative fusion.  Its useful residue is the literal moving graph
packet: a successful construction must stop at a non-full phase set, add a
second nongauge actuator, or protect/transport the upper bank independently.

## 8. Dependencies

This proof uses the explicit rigid packet and two-soliton shape cycle from

* `MATH_THEOREM_PBBS_RIGID_SINGLE_SOLITON_CLEAN_C6_Q2_PALETTE_REPAIR_20260805.md`,
* `MATH_THEOREM_PBBS_CLEAN_C6_Q2_NEUTRAL_GRAPHIC_NEUTRAL_20260805.md`,

and the exact current qualifications from

* `MATH_THEOREM_PBBS_CYCLIC_ORBIT_COBBOUNDARY_AND_ROTATION_LENGTH_GATE_20260805.md`,
* `MATH_THEOREM_PBBS_ROTATION_ORBIT_CURRENT_BALANCE_CRITERION_20260805.md`,
* `MATH_THEOREM_PBBS_CLEAN_C6_COMMON_HISTORY_ALL_LOWER_DEPTH_LIFT_AND_SHARP_UPPER_BOUNDARY_20260805.md`, and
* `MATH_OBSTRUCTION_PBBS_CONSECUTIVE_C6_MINIMAL_COMMON_HISTORY_SCREEN_PACKING_20260805.md`.
