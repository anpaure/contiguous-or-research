# SBE endpoint cuts as forbidden subcubes, and the robust threshold

Date: 2026-07-31  
Status: exact all-parameter reduction and exact `n=3,4` obstruction census;
corrected proof-producing `n=5` robust tests are in progress.  No all-parameter
orientation theorem is claimed.

## 0. Result

Fix an **undirected** Catalan path forest `F` and one of its two strict
occurrence shores.  Let `X` be the middle layer and let
`Gamma(H)` be the simple outer occurrence neighbourhood of
`H subseteq X`.  Write the path endpoints as disjoint two-element blocks,
with singleton components treated as one-element fixed blocks.

Every SBE cut has an exact forbidden-subcube form.  For a middle set `H`,
let

* `i(H)` be the number of singleton path endpoints in `H`;
* `b_2(H)` be the number of nontrivial endpoint blocks wholly in `H`;
* `B_1(H)` be the set of nontrivial endpoint blocks having exactly one end
  in `H`.

For `j in B_1(H)`, let `X_j(H)=1` when the shore's selected terminal of
path `j` is its endpoint in `H`.  Then the exact cut is

\[
 i(H)+b_2(H)+\sum_{j\in B_1(H)}X_j(H)
 \le \left\lfloor{N|\Gamma(H)|-R|H|\over C}\right\rfloor .
 \tag{0.1}
\]

Thus, after putting

\[
 u(H)=\left\lfloor{N|\Gamma(H)|-R|H|\over C}\right\rfloor
       -i(H)-b_2(H),                                  \tag{0.2}
\]

the bad event is the binomial tail

\[
             \sum_{j\in B_1(H)}X_j(H)\ge u(H)+1.      \tag{0.3}
\]

When `0<=u(H)<|B_1(H)|`, this event is the union of the
`binom(|B_1(H)|,u(H)+1)` minimal forbidden subcubes obtained by forcing any
`u(H)+1` of its signed endpoint literals.  Its exact minimum subcube
codimension is

\[
                         c(H)=u(H)+1.                  \tag{0.4}
\]

The midpoint immediately controls this codimension.  If the half-endpoint
point is SBE and `sigma_(1/2)(H)` denotes its scaled slack, then

\[
 c(H)=\left\lfloor {|B_1(H)|\over2}
                  +{\sigma_{1/2}(H)\over C}\right\rfloor+1,
 \tag{0.5}
\]

and hence every nontrivial bad event requires a strict majority of its
split endpoint blocks.  Under independent fair orientation its exact
probability is

\[
 2^{-|B_1(H)|}\sum_{t=c(H)}^{|B_1(H)|}
                         { |B_1(H)|\choose t}.         \tag{0.6}
\]

This is the correct starting point for a lopsided-LLL or cluster-expansion
argument.  Counting raw cuts is unnecessary; only canonical closed sets and
their signed endpoint supports matter.

The orientation-free extreme is also exact.  The forest is SBE on this
shore for **every** coherent orientation if and only if

\[
 R|H|+Cq_E(H)\le N|\Gamma(H)|\qquad(H\subseteq X),    \tag{0.7}
\]

where `q_E(H)=i(H)+b_2(H)+|B_1(H)|` is the number of endpoint blocks met by
`H`.  This is substantially stronger than existence of one orientation.

At `n=3`, the authenticated recursive forest has opposite unit cut events,
so the minimum cut-event codimension is one and no orientation exists.  At
`n=4`, the simultaneous two-shore feasible relation has exactly 59 prime
forbidden subcubes.  Their codimension histogram is

\[
 2^1,\ 4^5,\ 5^{16},\ 6^{22},\ 7^9,\ 8^6.            \tag{0.8}
\]

The unique codimension-two obstruction is the assignment

\[
                         x_4=x_{13}=0,                \tag{0.9}
\]

equivalently the already known SBE clause `x_4 or x_13`.  Its underlying
upper-shore middle set is

\[
                         H=\{0x5c,0x6c,0xe8\}.        \tag{0.10}
\]

It has `|H|=3`, `|Gamma(H)|=2`, `b_1(H)=2`, and `c(H)=2`.
The maximum variable-dependency degree among the 59 prime subcubes is 58.
Even in the sharper conjunction lopsidependency graph, where opposite
literals are not joined, the maximum is 58 and the unique codimension-two
event has degree 31.  Thus the naive symmetric LLL does not explain the
small `n=4` fixture.

The stored recursive orientations exhibit increasing local clearance:

\[
\begin{array}{c|c|c|c}
n&\text{effective path bits}&\text{complete passing Hamming radius}
 &\text{consequent prime-subcube lower bound}\\ \hline
5&33&5&c_{\min}\ge6\\
6&114&2&c_{\min}\ge3\\
7&386&1&c_{\min}\ge2.
\end{array}                                             \tag{0.11}
\]

The rows test respectively `284,274`, `6,556`, and `387` distinct coherent
orientations with exact two-min-cut replay.  They are finite lower bounds,
not a proof that the relations have no more distant obstruction or that the
radius grows with `n`.

## 1. Complement-cut derivation

For a terminal bank `Z`, the closed-neighbourhood SBE form is

\[
                 N|U|\le R|N(U)|+C|Z\cap N(U)|.       \tag{1.1}
\]

The total capacity identity is

\[
                         NP=RM+CK,                    \tag{1.2}
\]

where `K` is the number of forest components and `Z` contains one terminal
from each.  Put `H=X\setminus N(U)` and let `Gamma(H)` be the outer rows
having a neighbour in `H`.  Maximal closure gives

\[
                 R|H|+C|Z\cap H|\le N|\Gamma(H)|.    \tag{1.3}
\]

Conversely every `H` gives the maximal outer family outside `Gamma(H)`, so
(1.3) for all `H` is equivalent to SBE.

For a fixed `H`, singleton components contribute `i(H)` to `|Z cap H|`, a
block wholly in `H` contributes one, a disjoint block contributes zero, and
a split block contributes its signed orientation literal.  Substitution
into (1.3), followed by integer rounding, proves (0.1)--(0.4).

Maximizing `|Z cap H|` over all coherent orientations independently chooses
the endpoint in `H` on every split block, giving exactly `q_E(H)`.  This
proves (0.7).  Notice that `q_E` counts endpoint blocks meeting `H`; an
internal path vertex whose two component endpoints lie outside `H`
contributes zero.  Confusing these two notions gives a strictly stronger
but incorrect alleged equivalence.

## 2. Midpoint slack and codimension

At the half-endpoint point,

\[
 |Z_{1/2}\cap H|=i(H)+b_2(H)+{|B_1(H)|\over2}.        \tag{2.1}
\]

Define its scaled complement slack by

\[
 \sigma_{1/2}(H)=N|\Gamma(H)|-R|H|
 -C\left(i(H)+b_2(H)+{|B_1(H)|\over2}\right).        \tag{2.2}
\]

Rearranging (0.2) gives

\[
 u(H)={|B_1(H)|\over2}+{\sigma_{1/2}(H)\over C}
       \quad\hbox{before taking the floor}.           \tag{2.3}
\]

This proves (0.5).  In particular, if the midpoint is feasible then

\[
                  c(H)\ge\lfloor |B_1(H)|/2\rfloor+1. \tag{2.4}
\]

Thus midpoint feasibility does not itself round—`n=3` is the literal
counterexample—but it turns every obstruction into a strict-majority event.
The two shores use opposite signed literals on every path, and events whose
literal supports are disjoint are independent.  Equations (0.5)--(0.6)
therefore expose exactly the two quantities an LLL proof must bound:

1. the split-block size and half slack of every canonical bad set; and
2. the number of other minimal subcubes sharing one of its path variables.

More precisely, replace every tail event (0.3) by all of its codimension-
`c(H)` minimal conjunctions.  Avoiding those conjunctions is equivalent to
satisfying every SBE cut.  Give two conjunctions a lopsided edge only when
they contain a common **same-sign** literal; a common opposite-sign literal
makes them disjoint.  The lopsided Lovasz local lemma gives the exact
conditional sufficient criterion

\[
 2^{-c(E)}\le x_E\prod_{E'\sim E}(1-x_{E'})
 \qquad(0<x_E<1).                                    \tag{2.5}
\]

In particular, if every conjunction has codimension at least `c_0` and
same-literal dependency at most `Delta`, then

\[
                         e(\Delta+1)2^{-c_0}\le1       \tag{2.6}
\]

is sufficient for an integral simultaneous orientation.  This theorem is
purely Boolean and does not require the rounded endpoint demand to be
crossing supermodular.  What remains is to prove useful all-`n` bounds on
`c_0` and `Delta` for the recursive occurrence geometry.

## 3. Canonical closure

Put

\[
 \operatorname{cl}(H)=\{x\in X:\Gamma(x)\subseteq\Gamma(H)\}. \tag{3.1}
\]

Then `H subseteq cl(H)` and
`Gamma(cl(H))=Gamma(H)`.  For every fixed orientation,

\[
 D_Z(\operatorname{cl}(H))-D_Z(H)
 =R|\operatorname{cl}(H)\setminus H|
  +C|Z\cap(\operatorname{cl}(H)\setminus H)|\ge0.    \tag{3.2}
\]

Hence every violating orientation has a Galois-closed witness.  This
canonicalization is proof-safe for cut counting.  Its endpoint support may
grow, so one must recompute `(i,b_2,B_1,u)` after closure rather than retain
the old subcube label silently.

The established leaf-peeling theorem further reduces a positive maximizer
to a closed connected outer-2-core.  That compression is useful for
enumeration, but it does not by itself bound subcube dependency.

## 4. Exact endpoint-boundary ledger

Let

\[
 \beta(H)=\sum_{x\in H}(2-d_F(x)),                   \tag{4.1}
\]

let `chi(H)=|B_1(H)|`, and let `lambda(H)` count occurrence edges from
`X\setminus H` into the active outer rows `Gamma(H)`.  Since a singleton
contributes two to `beta`,

\[
                 q_E(H)={\beta(H)+\chi(H)\over2}.     \tag{4.2}
\]

The exact edge ledger

\[
 (n+2)(|H|-|\Gamma H|)=4|H|-\beta(H)-\lambda(H)      \tag{4.3}
\]

turns robust SBE (0.7) into

\[
\boxed{
 n\lambda(H)+2|H|
 \ge (n+1)\beta(H)+(2n+1)\chi(H).}                  \tag{4.4}
\]

Since `q_E=(beta+chi)/2`, the same inequality has the transparent
**two-plus-one endpoint form**

\[
 \boxed{
 \lambda(H)+{2\over n}\bigl(|H|-q_E(H)\bigr)
 \ge 2q_E(H)+\chi(H).}                               \tag{4.5}
\]

Thus every touched endpoint block costs two units, a split block costs one
additional unit, and vertices beyond the first in each touched block supply
`2/n` units of internal reserve.  For `H=X`, one has
`|H|=(n+1)q_E`, `chi=lambda=0`, so (4.5) is equality.  The unique `n=4`
codimension-two obstruction has

\[
 (|H|,q_E,\chi,\lambda)=(3,2,2,4),
\]

and fails (4.5) by `3/2` units.

Equations (4.4)--(4.5) are the sharp all-orientation expansion target.  They separate the
ordinary endpoint mass from the extra tax for a split path.  A path with
opposite endpoint membership has at least one physical forest boundary
edge, so `chi(H)<=|delta_F(H)|`; however no general inequality presently
converts those physical boundary edges into enough occurrence `lambda`
credit.  The recursively verified facet bound `eta^pm(F)>=3` is local
candidate supply, not yet such a conversion.

### 4.1 The first exact obstruction is a two-socket bridge

Call a path endpoint `x` a **pure socket endpoint** on the named shore when
its simple occurrence neighbourhood is a singleton, say
`Gamma(x)={s_x}`.  Suppose two pure socket endpoints `a,b` lie on distinct
path blocks and an internal forest vertex `y` has

\[
                     \Gamma(y)=\{s_a,s_b\}.           \tag{4.6}
\]

If the Galois closure of the two sockets is exactly
`H={a,y,b}`, then `H` has two split endpoint blocks, no full endpoint block
or singleton component, and `|Gamma(H)|=2`.  Hence its forbidden-subcube
codimension is

\[
 c(H)=1+\left\lfloor{2N-3R\over C}\right\rfloor,
 \tag{4.7}
\]

while robust all-orientation SBE fails by

\[
                         3R+2C-2N=R.                \tag{4.8}
\]

The twice-scaled midpoint slack on the same closure is

\[
                         4C-2N.                     \tag{4.8a}
\]

Thus this motif is never robust.  When `2C>=N` it is a genuine rounded
orientation obstruction despite midpoint feasibility; once `2C<N` it
already refutes the midpoint relaxation itself.

This local motif exactly explains the unique `n=4` codimension-two row:

\[
 (a,y,b)=(0x5c,0x6c,0xe8),\qquad
 (s_a,s_b)=(0x7d,0xed).                              \tag{4.9}
\]

The two split path indices are `4,13`; (4.7) gives `c(H)=2`, and (4.8)
equals `14`.  Thus the clause `x_4 or x_13` is not an anonymous cut: it is
the orientation demand created by one internal connector between two pure
endpoint sockets.

An exact census of the authenticated recursive forests finds the following
numbers of such two-socket connector pairs on `(upper,lower)` shores:

\[
\begin{array}{c|ccccc}
n&3&4&5&6&7\\ \hline
\text{upper}&0&1&0&0&0\\
\text{lower}&0&0&0&0&0.
\end{array}                                           \tag{4.10}
\]

This is finite structural evidence, not an all-parameter exclusion theorem.
It does show that the first nontrivial prime obstruction is a literal local
socket bridge and that the stored recursion removes this motif immediately
after `n=4`.

## 5. Exact finite census

The independent audit

```text
scratch/audit_catalan_sbe_forbidden_subcubes_n3_n4_20260731.py
scratch/catalan_sbe_forbidden_subcubes_n3_n4_20260731.audit.json
```

authenticates the existing exact orientation census, enumerates all
`3^10-1` nonempty partial assignments at `n=4`, retains precisely those
with no feasible extension and minimal support, and recomputes (0.8)--(0.9).
Its current SHA-256 values are to be frozen after final review.

The recursive Hamming-ball rows (0.11) are produced by

```text
scratch/audit_catalan_recursive_sbe_oneflip_balls_n5_n7_20260731.py
scratch/catalan_recursive_sbe_hamming_ball_radius5_n5_20260731.audit.json
scratch/catalan_recursive_sbe_hamming_ball_radius2_n6_20260731.audit.json
scratch/catalan_recursive_sbe_oneflip_ball_n7_20260731.audit.json
```

The producer reconstructs both occurrence graphs from the authenticated
forest, enumerates every reversal set in the named Hamming ball, and runs an
integer max-flow on both shores.  Passing a radius-`r` ball implies that no
prime forbidden subcube has codimension at most `r`: any such subcube has a
point within distance at most `r` of the ball centre unless it contains the
centre, which is itself feasible.

The corrected endpoint-block robust query is implemented separately in

```text
scratch/search_catalan_recursive_full_orientation_robust_sbe_20260731.py
scratch/build_catalan_recursive_full_orientation_robust_sbe_cnf_20260731.py
```

The first script preserves `INFEASIBLE/UNKNOWN`; the second emits a CNF for
proof-producing SAT.  No finite `n=5` robust result is asserted here until
the endpoint-block model, solver result, and proof are independently
replayed.  In particular, a discarded stale run which charged every internal
path vertex as an endpoint resource has no mathematical status.

The pure-socket bridge census (4.10) is independently reconstructed by

```text
scratch/audit_catalan_sbe_pure_socket_bridges_n3_n7_20260731.py
scratch/catalan_sbe_pure_socket_bridges_n3_n7_20260731.audit.json
```

It authenticates the recursive witness payload, rebuilds both occurrence
shores, computes all pure endpoint sockets and all internal two-socket
connectors, closes each socket pair in the occurrence Galois connection,
and recomputes (4.7)--(4.9) from the resulting literal masks.

## 6. Remaining theorem

There are now two sharply separated positive routes.

1. **Robust threshold:** prove (4.4) for recursively supplied forests from
   some parameter onward.  Then orientation becomes a gauge variable and
   no rounding is needed.
2. **Lopsided endpoint rounding:** if robust SBE fails, prove a lower bound
   on `(c(H),|B_1(H)|)` and an upper bound on the dependency graph of the
   canonical forbidden subcubes strong enough for a lopsided LLL or cluster
   expansion.  The exact event probability is (0.6).

Generic supermodular uncrossing cannot replace either route: the ceiling
creates the authenticated `n=3` integrality gap, and endpoint pairs with no
common outer neighbour give the wrong-sign crossing term.  What remains is
Boolean-specific expansion or Boolean-specific cut counting on the actual
recursive forest class.
