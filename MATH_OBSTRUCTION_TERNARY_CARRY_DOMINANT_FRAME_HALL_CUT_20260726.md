# The dominant-frame Hall cut for the phase-dense ternary-carry factor

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The ternary-carry fusion theorem closes the ownership and seam ledgers,
but it does **not** supply the positive-density pair-frame mixing forced
by the fixed-frame Gaussian census.

Let

\[
 W=\binom{2m}{m},\qquad
 q=x\sqrt m+o(\sqrt m),\qquad x>0,
\tag{0.1}
\]

and let the carry construction use `t` recoupled eight-blocks, so its
fused cycles have length

\[
 L=4t\,3^t.
\tag{0.2}
\]

Write `G=W-o(W)` for the good middle-owner mass.  There is one fixed
global coordinate pairing `P_1`, namely the all-new associator pairing,
with the following exact properties.

1. Each fused component has exactly

   \[
                       3^t-1                         \tag{0.3}
   \]

   outgoing edges which are not `P_1`-pair flips.

2. If `A_q` is the number of starts whose length-`q` physical window
   contains at least one such edge, then for either signed shadow

   \[
   \boxed{
    {1-3^{-t}\over4t}G
    \le A_q\le
    {q(1-3^{-t})\over4t}G.}
   \tag{0.4}
   \]

   The exact value is the cyclic gap sum in Theorem 4.1 below.

3. Therefore the exact mass of depth-`q` occurrences which remain inside
   the single frame `P_1` is

   \[
   \boxed{I_q=G-A_q.}                                 \tag{0.5}
   \]

   In particular, if `q/t=o(1)`, then

   \[
                         I_q=W-o(W).                  \tag{0.6}
   \]

The relevant strengthening of the fixed-frame escape theorem is
window-level, not cycle-level.  For an arbitrary exact middle-owner
factor, if only `A_{P,q}` signed depth-`q` windows leave a fixed pairing
`P`, then

\[
 \boxed{
 M_q^\pm\ge D_{m,q}-A_{P,q},}
\tag{0.7}
\]

where

\[
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+                       \tag{0.8}
\]

is the exact one-frame type deficit.  Consequently the carry factor
satisfies

\[
 \boxed{
 {M_q^\pm\over W}
 \ge
 \delta(x)-{q\over4t}+o(1),}
\tag{0.9}
\]

where

\[
 \delta(x)=e^{-x^2}\Phi(x/2)-\Phi(-3x/2)>0.          \tag{0.10}
\]

In the constant-one parameter regime of the carry theorem,

\[
 {H\over\sqrt m}\longrightarrow\infty,
 \qquad H\le t<2H,
\tag{0.11}
\]

so `q/t=o(1)` at every fixed Gaussian depth.  Hence

\[
 \boxed{
 M_q^-\ge(\delta(x)-o(1))W,
 \qquad
 M_q^+\ge(\delta(x)-o(1))W.}
\tag{0.12}
\]

This is a literal target-set cut, not merely a pair-type or scalar
transport warning.  It disproves the desired conclusion

\[
 \sum_{q\le H}(M_q^-+M_q^+)=o(W)                     \tag{0.13}
\]

for the present ternary-carry atlas.

The conceptual reason is simple.  The static all-new shore may have large
`W_1` displacement relative to the old pairing, but the fixed-frame
deficit is frame-covariant.  After moving to the new shore, `P_1` becomes
the dominant frame and has its own Gaussian deficit.  The ternary carry
changes only `Theta(G/t)` genuinely frame-escaping edges, so its
depth-`q` escape mass is only `O(qG/t)=o(W)`.

Thus there is no global mixed-frame expansion theorem for this factor.
Any repair must install at least

\[
 \boxed{
 B_P\ge{D_{m,q}-M_q^\pm\over q}}
\tag{0.14}
\]

genuinely `P`-escaping outgoing edges.  To obtain `M_q^\pm=o(W)` at a
fixed Gaussian depth requires `Omega_x(W/q)` such edges relative to every
fixed frame.  The carry factor has only

\[
 B_{P_1}={1-3^{-t}\over4t}G=o(W/q).                  \tag{0.15}
\]

## 1. The two local pair frames

In one associator block write

\[
 P_0=ab\mid cd\mid uv\mid wx,
 \qquad
 P_1=ac\mid bd\mid uv\mid wx.                       \tag{1.1}
\]

The old local factor consists of four main squares whose active pairs are
`ab,cd`, and two reservoir squares whose active pairs are `uv,wx`.  The
new local factor consists of four main squares whose active pairs are
`ac,bd`, and two reservoir squares whose active pairs are again `uv,wx`.
Thus every edge of the new factor is a `P_1`-pair flip.  Among the six
old rows, exactly four use a pair outside `P_1`, while the two reservoir
rows still use a pair of `P_1`.

Apply (1.1) in every labelled eight-block of the global block partition
and pair the at most six leftover coordinates arbitrarily.  This gives a
single global perfect matching, again denoted `P_1`.  The canonical
first-`t` eligible-block rule does not make this frame owner-dependent:
it only decides which blocks move.  Every unselected block is frozen, and
every all-new transition in a selected block is a `P_1`-pair flip.

The carry factor is defined relative to the static all-new factor.  At
one designated adjacent-colour port in each selected block, it sometimes
uses the old matching instead.  Therefore an outgoing carry edge fails to
be a `P_1`-pair flip if and only if both of the following occur:

1. the ternary carry triggers at that port;
2. the current old row is one of the four main rows rather than one of
   the two reservoir rows.

This distinction is important.  The total opposite-shore switch count
from the fusion theorem overcounts genuine pair-frame escape by the
factor `3/2`.

## 2. A window-level fixed-frame Hall theorem

Fix a perfect matching `P` of the `2m` ground coordinates.  For a middle
owner `X`, let `f_P(X)` be the number of full `P`-pairs in `X`.  Put

\[
 V_f={m!\over f!^2(m-2f)!}\,2^{m-2f}.                \tag{2.1}
\]

For a rank-`m-q` lower target of `P`-type `f`, the exact target count is

\[
 T_{f,q}=
 {m!\over f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.            \tag{2.2}
\]

The same number counts upper targets after exchanging full and empty
pairs.  Define `D_{m,q}` by (0.8).

Consider any physical exact factor on a subset of the middle owners,
using each retained owner once.  Call a signed depth-`q` window
`P`-internal when all its `q` replacement moves flip distinct pairs of
`P`.  Let `A_{P,q}^\pm` be the number of noninternal signed windows.

### Theorem 2.1 (window-level positive-density frame escape)

For both signs,

\[
 \boxed{
 M_q^\pm\ge
 \bigl[D_{m,q}-A_{P,q}^\pm\bigr]_+.}                 \tag{2.3}
\]

More generally, if middle owners may be repeated with total repeat
excess `E_0`, then

\[
 M_q^\pm\ge
 \bigl[D_{m,q}-E_0-A_{P,q}^\pm\bigr]_+.             \tag{2.4}
\]

#### Proof

First suppose owners are used at most once.  A `P`-internal lower window
starting from a source of type `f` preserves all source-full pairs and
empties `q` source-split pairs.  Its lower target therefore has the same
type `f`.  There are only `V_f` middle owners of that type, so the
`P`-internal windows can cover at most

\[
                         \min(V_f,T_{f,q})            \tag{2.5}
\]

distinct type-`f` targets.  The noninternal windows can cover at most
`A_{P,q}^-` further literal targets in total.  Hence the total number of
covered lower targets is at most

\[
 \sum_f\min(V_f,T_{f,q})+A_{P,q}^-
 =N_q-D_{m,q}+A_{P,q}^-.                             \tag{2.6}
\]

Subtracting from `N_q` proves (2.3) for the lower sign.  A `P`-internal
upper window fills `q` split pairs and preserves the number of source
empty pairs, giving the identical upper argument.

If sources may repeat, write `r_f` for the repeat excess in type `f`.
Then at most `V_f+r_f` internal starts have type `f`, and
`sum_f r_f\le E_0`.  Replacing `V_f` by `V_f+r_f` in (2.5)--(2.6) loses
at most `E_0`, proving (2.4).  \(\square\)

### Corollary 2.2 (an explicit literal Hall cut)

Let

\[
 \mathcal Z_{P,q}^-=
 \mathop{\dot\bigcup}_{f:T_{f,q}>V_f}
 \mathcal L_{P,f,q}^-                                \tag{2.7}
\]

be the union of the deficient literal lower target orbits.  Then the
`P`-internal starts can cover at most

\[
 \sum_{f:T_{f,q}>V_f}V_f                              \tag{2.8}
\]

members of this target set, while all noninternal starts together can
cover at most `A_{P,q}^-` more.  Therefore the actual carry incidence
fails the target-set Hall cut (2.7) by at least

\[
                         D_{m,q}-A_{P,q}^-.            \tag{2.9}
\]

The upper target family gives the same cut.  Thus (2.3) is already a
literal-face obstruction; no additional orbit-to-literal rounding gap is
being used.

Theorem 2.1 is stronger than the earlier whole-strip escape theorem for a
dynamic-frame factor.  A fused carry cycle is not supported by `P_1` as
a whole, so a whole-cycle test would classify all its mass as mixed.  But
almost every shallow window of that cycle is still `P_1`-internal.  The
window-level census is the quantity relevant to shadow Hall.

## 3. Exact genuinely escaping edge mass of the carry factor

Fix one fused component.  It is indexed by a binary orbit vector

\[
 b\in\mathbb Z_2^t
\tag{3.1}
\]

and a Hamming translate `k`.  During one `4t`-step phase lap, there is one
designated adjacent-colour carry port in every block.  Order these ports
chronologically as digits `1,...,t`.

The row coordinate in a port fibre is

\[
                         z_s\in\mathbb Z_3.            \tag{3.2}
\]

The carry rule triggers digit `s` precisely when the already updated
lower digits are zero.  Before the update this is equivalent to

\[
                         z_1=\cdots=z_{s-1}=2.         \tag{3.3}
\]

Over one complete `3^t`-lap odometer orbit, (3.3) holds at digit `s` on
exactly

\[
                         3^{t-s+1}                    \tag{3.4}
\]

laps.  The active digit `z_s` is unrestricted and each of its three
values occurs exactly `3^{t-s}` times.

For fixed `b`, the adjacent-port holonomy orbit has two main old rows and
one old reservoir row.  Hence exactly two of the three values of `z_s`
produce an old main edge, and one produces an old reservoir edge.  By
Section 1, precisely the first two are outside `P_1`.  Therefore digit
`s` creates exactly

\[
                         2\,3^{t-s}                   \tag{3.5}
\]

genuinely `P_1`-escaping edges on one fused component.

### Theorem 3.1 (exact bad-edge count)

Every fused component contains exactly

\[
 \boxed{
 B_C=\sum_{s=1}^t2\,3^{t-s}=3^t-1}                  \tag{3.6}
\]

outgoing edges which are not pair flips of `P_1`.

Since the component length is `L=4t3^t`, the exact bad-edge density is

\[
 \boxed{
 {B_C\over L}={1-3^{-t}\over4t}.}                   \tag{3.7}
\]

Thus over all good owners the bad-edge mass is

\[
 \boxed{
 B_{P_1}={1-3^{-t}\over4t}G.}                       \tag{3.8}
\]

#### Proof

Equation (3.5) and the geometric sum give (3.6).  The component length
gives (3.7).  The fused components partition the `G` good middle owners,
so multiplying the density by `G` proves (3.8).  \(\square\)

For comparison, the total number of opposite-shore switches on one
component is

\[
 \sum_{s=1}^t3^{t-s+1}
 ={3\over2}(3^t-1).                                  \tag{3.9}
\]

Thus the global changed-edge count from the carry theorem is

\[
 E={3(1-3^{-t})\over8t}G,                            \tag{3.10}
\]

and (3.8) is exactly `2E/3`.  The remaining one-third are old reservoir
edges, which still flip the common pairs `uv` or `wx` and do not escape
`P_1`.

## 4. Exact depth-`q` frame occurrence mass

On a fused component `C`, list its `B_C=3^t-1` bad outgoing edges in
cyclic order.  Let

\[
 g_{C,1},\ldots,g_{C,B_C}\in\mathbb Z_{>0},
 \qquad
 \sum_jg_{C,j}=L,                                    \tag{4.1}
\]

be the cyclic distances from one bad edge to the next.

### Theorem 4.1 (exact cyclic gap formula)

For every `1\le q<L`, the number of forward depth-`q` starts on `C`
whose window is not `P_1`-internal is exactly

\[
 \boxed{
 A_q(C)=\sum_{j=1}^{B_C}\min(q,g_{C,j}).}            \tag{4.2}
\]

The reverse/upper count has the same value.  Consequently

\[
 \boxed{
 A_q^- =A_q^+
 =\sum_C\sum_{j=1}^{B_C}\min(q,g_{C,j}),}            \tag{4.3}
\]

and the exact `P_1`-internal occurrence mass is

\[
 \boxed{I_q^\pm=G-A_q^\pm.}                          \tag{4.4}
\]

#### Proof

A bad edge at cyclic position `e` belongs to the forward windows starting
at the `q` positions

\[
                         e-q+1,\ldots,e.              \tag{4.5}
\]

Thus the exceptional start set is the union of equal length-`q` arcs
ending at the bad positions.  Between two consecutive bad positions at
distance `g`, that union contributes exactly `min(q,g)` new starts.
Summing around the component proves (4.2).  Reversing the cyclic order
preserves the multiset of cyclic gaps, proving the upper statement.
Summing over components gives (4.3)--(4.4).  \(\square\)

The carry theorem fixes the bad-edge number (3.6), but the precise port
locations, and hence the gaps in (4.1), may depend on the Hamming
translate `k`.  Formula (4.3) is therefore the exact occurrence census;
there is no gap-independent single closed value beyond it.  The universal
bounds are nevertheless sharp enough:

\[
 B_C\le A_q(C)\le qB_C.                              \tag{4.6}
\]

Using (3.8),

\[
 \boxed{
 {1-3^{-t}\over4t}G
 \le A_q^\pm\le
 {q(1-3^{-t})\over4t}G,}                             \tag{4.7}
\]

which is (0.4).

Every exceptional window can of course be certified in some mixed frame:
its `q` moves lie in distinct eight-blocks and hence form disjoint
coordinate pairs.  But all such mixed-frame occurrences together have
mass only `A_q`.  Their distribution among the other frames cannot repair
more than `A_q` literal targets of the deficient `P_1` orbits.

## 5. The Gaussian cut

The exact fixed-frame census gives, uniformly when

\[
                         q=x\sqrt m+o(\sqrt m),       \tag{5.1}
\]

\[
 {D_{m,q}\over W}\longrightarrow
 \delta(x)=e^{-x^2}\Phi(x/2)-\Phi(-3x/2)>0.          \tag{5.2}
\]

Apply Theorem 2.1 to `P=P_1` and use (4.7).  Since `G\le W`,

\[
\begin{aligned}
 M_q^\pm
 &\ge D_{m,q}-A_q^\pm\\
 &\ge D_{m,q}
   -{q(1-3^{-t})\over4t}G.
\end{aligned}                                        \tag{5.3}
\]

Therefore

\[
 \boxed{
 \liminf_{m\to\infty}{M_q^\pm\over W}
 \ge
 \delta(x)-\limsup_{m\to\infty}{q\over4t}.}         \tag{5.4}
\]

If

\[
                         {t\over\sqrt m}\to a
                         \in(0,\infty],               \tag{5.5}
\]

then (5.4) reads

\[
 \liminf {M_q^\pm\over W}
 \ge \delta(x)-{x\over4a},                           \tag{5.6}
\]

with `1/a=0` when `a=\infty`.

In particular, the constant-one carry parameters have `a=\infty`, so
(0.12) follows.  Even at a fixed `t=a\sqrt m`, the cut is positive whenever

\[
                         a>{x\over4\delta(x)}.         \tag{5.7}
\]

Since

\[
 \delta(x)=\sqrt{2/\pi}\,x+O(x^2)
 \qquad(x\downarrow0),                               \tag{5.8}
\]

every `a>\sqrt{\pi/2}/4` is already obstructed at all sufficiently small
fixed Gaussian depths.  In particular, under the carry parameter relation
`H\le t<2H`, any regime with `t\ge\sqrt m` has a positive literal Hall
deficit somewhere in its controlled Gaussian window.

## 6. Consequences for expansion and repair

The desired carry-specific expansion theorem would have to make the
actual shadow image cover all but `o(W)` members of every literal target
layer.  The target family `\mathcal Z_{P_1,q}^\pm` from (2.7) is an
explicit counterexample: its uncovered mass is at least the right side of
(5.3), which is `Theta_x(W)` in the constant-one regime.

This also gives the exact edge-density repair threshold.  In any exact
factor let `B_P` be the number of outgoing edges which are not `P`-pair
flips.  Every such edge lies in exactly `q` forward depth-`q` windows, so

\[
                         A_{P,q}^\pm\le qB_P.          \tag{6.1}
\]

Combining this with Theorem 2.1 gives

\[
 \boxed{
 M_q^\pm\ge D_{m,q}-qB_P.}                           \tag{6.2}
\]

Hence `M_q^\pm=o(W)` at `q=x\sqrt m+o(\sqrt m)` forces

\[
 \boxed{
 B_P\ge(\delta(x)-o(1)){W\over q}.}                  \tag{6.3}
\]

The carry factor instead has, relative to its dominant frame,

\[
 B_{P_1}={1-3^{-t}\over4t}G.                         \tag{6.4}
\]

The ratio of (6.4) to the necessary scale `W/q` is at most

\[
                         {q\over4t}=o(1).              \tag{6.5}
\]

Thus no owner allocation, target-frame reassignment, internal packet
injectivity, or cross-macrocell matching can repair the present factor
without changing its physical edge set on an additional
`Omega_x(W/q)` incidences relative to `P_1`.

Passing the scalar `W_1` cut relative to `P_0` does not contradict this
obstruction.  Replacing most old rows by new rows moves type relative to
`P_0`, but it simultaneously concentrates almost all shallow windows in
the new fixed frame `P_1`.  The Gaussian deficit then reappears in the
`P_1` type coordinate.  A successful construction must be genuinely
frame-diffuse at **window scale**: for every fixed pairing `P` and every
fixed Gaussian depth, a positive density of its windows must leave `P`.

## 7. Audit ledger

1. The factor's cycles are globally mixed, but this is irrelevant.  The
   fixed-frame Hall proof uses depth-`q` windows, and (4.7) shows that
   almost all of those windows remain in `P_1`.
2. The opposite-shore edge count is not the pair-frame escape count.  Two
   of the six old rows move only on the reservoir pairs shared by `P_0`
   and `P_1`; this gives the exact factor `2/3` in (3.8).
3. The first-`t` eligible-block rule does not create owner-dependent
   coordinate matchings.  `P_1` is fixed on every global eight-block;
   eligibility only selects active blocks.
4. Omitted bad middle owners cannot weaken the lower bound.  They remove
   possible sources and hence can only create more holes.
5. The gap formula counts physical occurrence starts and is valid for
   both signed shadows.  No assumption of independence or random port
   spacing is used.
6. The obstruction is literal: (2.7) is a union of actual target masks,
   and each exceptional occurrence can repair at most one of them.
7. A final repair by `o(W)` appended target literals cannot absorb
   (0.12).  The present carry atlas therefore does not satisfy adjusted
   cap-one PCap and cannot yield coefficient one.
