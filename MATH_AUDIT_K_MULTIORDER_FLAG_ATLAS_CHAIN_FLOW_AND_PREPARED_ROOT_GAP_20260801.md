# Multi-order flag atlases: exact suffix marginals, chain-flow rounding, and the prepared-root gap

**Date:** 2026-08-01  
**Lane:** K, protected multi-order flags / balanced-turn interface  
**Status:** unconditional support and rounding theorems, plus two exact scope
corrections.  The suffix-only full-order model rounds integrally.  A sampled
order cover need not inherit that rounding, and fixing only the prepared tail
roots does not preserve the ordered-shift portal lists.  Nothing here proves
an owner/turn matching or an additive-constant word bound.

## 0. Audit verdict

Put

\[
                    n=2m+1,
\qquad W={n\choose m},
\qquad 0\le a\le d-1 .                              \tag{0.1}
\]

For an order `pi` and an `m`-set `q`, let `S_a^pi(q)` be `q` after deleting
its first `a` elements in the restriction of `pi` to `q`.  Thus
`S_(d-1)^pi(q)=C_0^q`, and the `S_a` are all the high suffix ranks of the
all-high flag.

The independently checked conclusions are as follows.

1. A random family of

   \[
   O\!\left(
     {\binom{2m+1}{d-1}\over\binom{m+d}{d-1}}
     \log(dW)
   \right)                                           \tag{0.2}
   \]

   global orders supports every target at every rank `m-a`, `0<=a<d`.
   This is within a logarithmic factor of the exact bottom-rank covering
   lower bound.

2. Uniformly averaging all orders at every root gives every rank-`m-a`
   target the exact common marginal

   \[
       \rho_a={W\over\binom{n}{m-a}}
              ={\binom{m+a+1}{a}\over\binom ma}.     \tag{0.3}
   \]

   This is an exact fractional statement, not a one-copy selector.

3. If every local order is available, the suffix-only one-copy problem is
   a layered Boolean network flow.  Consequently there is an integral
   selector for which every rank-`m-a` target has load either
   `floor(rho_a)` or `ceil(rho_a)`, simultaneously at every depth.  No SCD
   or absorption theorem is needed for this unpinned suffix-only statement.

4. After entire prepared chains are fixed, exact completion has an ordinary
   weighted-Hall criterion on each adjacent pair of Boolean levels.  It is
   not automatic.  Three prepared roots can use one order satisfying the
   robust-order hypothesis and collide on the same suffix at every positive
   depth.  At every depth with `rho_a<2` this exceeds the balanced upper
   quota two.  For `d=Theta(sqrt(m))` this gives `Theta(sqrt(m))` violated
   rank rows.  Thus arbitrary `O(1)` prepared roots do not preserve the
   balanced face and do not imply `O(1)` defect.

5. There is a separate, earlier turn-interface gap.  The ordered-shift atom
   from the robust-order theorem uses the chosen order at **both** its tail
   and its head.  Fixing only `O(1)` tail roots to the prepared order inside
   a mixed one-order-per-root selector does not preserve a linear portal
   list.  One must prove a cross-order head-robustness statement or constrain
   linearly many candidate heads.  Therefore the local list estimate cannot
   yet be inserted unconditionally into the balanced-turn portal theorem.

## 1. Every high suffix rank under one order

Write the elements of `q` in increasing `pi`-order as

\[
                         z_1<_{\pi}\cdots<_{\pi}z_m . \tag{1.1}
\]

Then

\[
 S_a^\pi(q)=q-\{z_1,\ldots,z_a\}
 =C_0^q\cup\cdots\cup C_{d-a-1}^q                 \tag{1.2}
\]

for `0<=a<=d-1`, with the evident interpretation at `a=0`.

### Theorem 1.1 (all-rank occurrence formula)

Fix an `(m-a)`-set `T`, and let `j_pi(T)` be the position of its first
element in the global order.  The number of roots `q` satisfying
`S_a^pi(q)=T` is

\[
                         {j_\pi(T)-1\choose a}.       \tag{1.3}
\]

In particular, `T` is supported by `pi` if and only if the first `a`
global coordinates of `pi` avoid `T`.

#### Proof

Such a root is uniquely `q=T dotcup H`, where `|H|=a` and every member of
`H` precedes every member of `T`.  Thus `H` is any `a`-subset of the
`j_pi(T)-1` coordinates preceding `min_pi T`.  Conversely each such `H`
gives the required suffix.  The positivity statement follows immediately.
`square`

This extends the bottom-suffix formula in
`MATH_THEOREM_ROBUST_ORDER_FLAGS_AND_BOTTOM_SUFFIX_COVER_OBSTRUCTION_20260801.md`
without changing its proof.

## 2. A simultaneous random-atlas upper bound

For fixed `a,T`, a uniformly random order supports `T` with probability

\[
 p_a={\binom{n-|T|}{a}\over\binom na}
     ={\binom{m+a+1}{a}\over\binom{2m+1}{a}}.        \tag{2.1}
\]

For `2d-3<=m`, these probabilities decrease with `a`, because

\[
                    {p_{a+1}\over p_a}
       ={m+a+2\over 2m+1-a}\le1                    \tag{2.2}
\]

for `0<=a<=d-2`.  Hence

\[
 p_*:=\min_{0\le a<d}p_a=p_{d-1},\qquad
 {1\over p_*}
 ={\binom{2m+1}{d-1}\over\binom{m+d}{d-1}}.        \tag{2.3}
\]

### Theorem 2.1 (random all-high-rank atlas)

Assume `2d-3<=m`.  For every `c>0`, there is a family of at most

\[
 L=\left\lceil {\log(dW)+c\over p_*}\right\rceil    \tag{2.4}
\]

orders supporting every target `T` at every rank `m-a`, `0<=a<d`.
Independent random orders have this property with probability at least
`1-e^{-c}`.

#### Proof

For one target the failure probability after `L` independent orders is
at most `exp(-Lp_a)<=exp(-Lp_*)`.  Every involved level has at most `W`
sets, so there are at most `dW` target rows.  The union bound gives failure
probability at most

\[
                       dW e^{-Lp_*}\le e^{-c}.       \tag{2.5}
\]

Positive success probability proves existence.  `square`

At `d=Theta(sqrt(m))`, (2.4) is the bottom-rank covering lower bound times
`O(m)`.  This theorem is support-only.  Uniform weights on the sampled
orders need not have exact target marginals, and support at each rank does
not by itself select correlated chains.

## 3. Exact uniform fractional suffix marginals

### Theorem 3.1 (uniform order marginal)

Give every root `q` unit mass spread uniformly over all total orders.  At
depth `a`, every rank-`m-a` target `T` receives exactly the load `rho_a` in
(0.3).

#### Proof

There are `binom(m+a+1,a)` roots containing `T`.  For any such root
`q=T dotcup H`, the set `H` is the first `a` elements of `q` with
probability `1/binom(m,a)`.  Therefore the target load is

\[
 {\binom{m+a+1}{a}\over\binom ma}.
\]

The factorial identity with `W/binom(n,m-a)` proves (0.3).  `square`

The same marginal is obtained by taking the uniform convex combination of
the **whole** single-order tables `F^pi`, with one common `pi` at all roots.
These two fractional couplings have identical suffix marginals but very
different turn correlations.  In particular, conditioning protected roots
to one specified common order in the latter coupling conditions the entire
table to that order; it does not leave a symmetric residual mixture.

Equivalently, the uniform process deletes one uniformly chosen coordinate
at every step.  If a level-`t+1` set carries load `rho_(m-t-1)` and sends it
equally to its `t+1` children, each level-`t` set receives

\[
 (n-t){\rho_{m-t-1}\over t+1}
 ={W\over\binom nt}=\rho_{m-t}.                     \tag{3.1}
\]

Thus the entire fractional flag is one coherent layered flow, not
merely a collection of equal single-rank marginals.

## 4. The full-order suffix selector is integral

Let `L_a=binom([n],m-a)`.  Direct an edge `A->B` from `L_(a-1)` to `L_a`
when `B subset A` and `|A-B|=1`.

### Theorem 4.1 (balanced one-copy chain rounding)

When every local order is available, there is one suffix chain from every
root such that, simultaneously for all `a,T`,

\[
 \lfloor\rho_a\rfloor
 \le \#\{q:S_a(q)=T\}
 \le \lceil\rho_a\rceil .                          \tag{4.1}
\]

#### Proof

Split every node `T in L_a` into an in-node and an out-node.  Give its
internal arc lower capacity `floor(rho_a)` and upper capacity
`ceil(rho_a)`; at `a=0` both capacities are one.  Put unbounded arcs along
the displayed Boolean containments, a source before `L_0`, and a sink after
`L_(d-1)`.

The uniform deletion flow of Section 3 is a fractional flow of value `W`
respecting every interval capacity.  All bounds are integral, so network
flow integrality supplies an integral flow of value `W`.  Decompose it into
unit source--sink paths.  The top capacities give exactly one path from
each root, and the internal-node flow is exactly the target load in (4.1).

Finally, every downward path from a root is induced by a total order: put
the successively deleted coordinates first, in deletion order, and extend
arbitrarily to the remaining coordinates.  `square`

This is the strongest legitimate consequence of normalized matching in the
unprotected full-order suffix model.  It says nothing about owner
attachments, legal turns, upper shadows, residence, or a finite sampled
atlas.

The last restriction is substantial.  At one fixed root, an order induces
one ordered `(d-1)`-tuple of deleted coordinates, whereas there are

\[
                         (m)_{d-1}=m(m-1)\cdots(m-d+2)           \tag{4.2}
\]

possible rooted suffix chains.  An atlas which is path-complete at even one
root therefore has at least `(m)_(d-1)` orders.  The support atlas of
Theorem 2.1 is not asserted to be path-complete and is vastly smaller in
the problem range.  Its one-copy selector is a configuration-hypergraph
problem: choosing one sampled chain per root couples all depth rows in one
column.  The layered-flow proof may splice a prefix and suffix belonging to
different sampled orders, so it cannot be applied without an additional
chain-splice closure theorem.

## 5. Exact prepared-chain completion criterion

Suppose distinct prepared roots have fixed full downward paths.  Let
`f_a(T)` be the number of fixed paths through `T`.  First fix desired
integer target loads `b_a(T)` satisfying

\[
 b_0(q)=1,\quad b_a(T)\ge f_a(T),\quad
 \sum_{T\in L_a}b_a(T)=W.                          \tag{5.1}
\]

Put `b'_a=b_a-f_a`.

### Theorem 5.1 (weighted-Hall criterion)

The fixed paths extend to one path from every unprepared root with exact
loads `b_a` if and only if, for every `1<=a<d` and every
`X subseteq L_(a-1)`,

\[
 \sum_{A\in X} b'_{a-1}(A)
 \le
 \sum_{B\in N_a(X)} b'_a(B),                       \tag{5.2}
\]

where `N_a(X)` is the family of level-`a` subsets contained in a member of
`X`.

#### Proof

For each adjacent pair of levels, the required edge multiplicities form a
bipartite `b`-matching with left degrees `b'_(a-1)` and right degrees
`b'_a`.  Equal total degree and the capacitated Hall theorem make (5.2)
necessary and sufficient.  Choose such an integral `b`-matching at every
adjacent layer.  At each intermediate node, arbitrarily pair its incoming
and outgoing units.  The resulting units concatenate into the required
rooted paths.  Necessity follows by restricting any path family to one
layer.  `square`

For balanced rather than preassigned loads, one may quantify over
`b_a(T) in {floor(rho_a),ceil(rho_a)}` in Theorem 5.1.  Equivalently, use
the node-split lower/upper-capacity network from Theorem 4.1 after subtracting
the fixed paths; Hoffman's circulation cuts are an exact finite criterion.
There is no unconditional pin-extension theorem.

## 6. Three robust prepared roots force growing balanced defect

The missing pin hypothesis is not cosmetic.

Choose an `(m-1)`-set

\[
                     S=\{s_1,\ldots,s_{m-1}\}
\]

and three distinct coordinates `a_1,a_2,a_3` outside it.  Put

\[
                         p_i=S+\{a_i\},\quad i=1,2,3. \tag{6.1}
\]

Use the common order

\[
 a_1<a_2<a_3<s_1<s_2<\cdots<s_{m-1}<\text{all remaining coordinates}.
                                                               \tag{6.2}
\]

Restricted to `p_i`, it deletes `a_i,s_1,s_2,...`.  Hence all three fixed
chains pass through the same target

\[
                 T_a=S-\{s_1,\ldots,s_{a-1}\}       \tag{6.3}
\]

at every depth `1<=a<d`.

This is genuinely a prepared robust order in the sense of the robust-order
theorem: take

\[
 Q_i=\{a_i,s_1,\ldots,s_{d-1}\}.                   \tag{6.4}
\]

Their union precedes every coordinate outside it, so the same linear local
turn-list estimate applies.

On the other hand,

\[
 \rho_a
 =\prod_{i=0}^{a-1}\left(1+{a+1\over m-i}\right)
 \le \exp\!\left({a(a+1)\over m-a+1}\right).       \tag{6.5}
\]

Thus `rho_a<2` whenever

\[
                  a(a+1)< (m-a+1)\log2 .            \tag{6.6}
\]

At each such depth the balanced upper quota is two, while the prepared
paths already give `T_a` load three.  Consequently:

### Corollary 6.1 (prepared-pin obstruction)

The three prepared paths (6.1)--(6.4) have no completion satisfying the
balanced target bounds (4.1).  Moreover the number of independently
violated rank rows is at least

\[
 \min\!\left\{d-1,
   \max\{a:a(a+1)<(m-a+1)\log2\}\right\}.           \tag{6.7}
\]

For `d=Theta(sqrt(m))` this is `Theta(sqrt(m))`.

This refutes an automatic balanced-extension or `O(1)`-imbalance claim for
arbitrary `O(1)` prepared roots.  It does **not** refute a cover-only
selector with unrestricted excess multiplicity, nor a specially chosen
pin family satisfying the cuts of Theorem 5.1.

## 7. The order-mixing quantifier gap in the portal interface

The ordered-shift theorem starts with one global order `pi`, gives the
`pi`-flag to every root, and for

\[
 q_\beta=p-\{z_1\}+\{\beta\}                       \tag{7.1}
\]

uses the facts that the first `d-1` elements of `q_beta` in **the same
order** are `z_2,...,z_d`.  Therefore each certified turn uses

\[
                    F^\pi(p)\quad\hbox{and}\quad F^\pi(q_\beta). \tag{7.2}
\]

Now let a multi-order selector choose `sigma(q)` independently at each root.
The constraint `sigma(p)=pi` alone does not retain (7.1).  For example, at
`d=2`, choose `sigma(q_beta)` with `beta` first in `q_beta`.  Then the oldest
head singleton is `{beta}`, which is not contained in the source bottom
class `p-{z_1}`; the survivor containment fails.  The same counterexample
works at every `d>=2` by putting `beta` in the first head singleton.

In fact the compatible head cylinder can be described exactly.  Write the
first `d-1` elements of `q_beta` in its selected head order as
`w_1,...,w_(d-1)`.  The survivor containments are equivalent to

\[
 w_1=z_2,\quad w_2=z_3,\quad\ldots,\quad
 w_{d-2}=z_{d-1},\qquad
 w_{d-1}\in\{z_d,\ldots,z_m\}.                     \tag{7.3}
\]

There are therefore only `m-d+1` compatible ordered deletion prefixes out
of the `(m)_(d-1)` possible prefixes at that head.  Under an independently
uniform head order, one candidate survives with probability

\[
                    {m-d+1\over(m)_{d-1}}.          \tag{7.4}
\]

Even before collisions between candidates, the expected retained list at
one prepared tail is at most

\[
                  (m+1){m-d+1\over(m)_{d-1}},       \tag{7.5}
\]

which is `O(1)` at `d=3` and tends to zero for every fixed `d>=4` (and much
faster in the problem range).  Thus independent random per-root orders do
not merely fail to prove robust degree; they destroy it on average.

Hence the robust-order theorem proves

\[
 \deg_{H(F^\pi)}(p)=\Omega(m),                       \tag{7.6}
\]

but not

\[
 \deg_{H(F^\sigma)}(p)=\Omega(m)
 \quad\hbox{from only }\sigma(p)=\pi.               \tag{7.7}
\]

To preserve the literal certified list, one must either

1. force the relevant flags at `Omega(m)` candidate heads to be compatible
   with `pi`; or
2. prove a new cross-order head-robustness theorem guaranteeing linearly
   many survivor containments after the mixed selector is chosen.

Accordingly, the statement that the balanced-turn LLL is “automatic for
these prepared ordered flags” is valid inside the complete single-order
table `F^pi`, and for tail-anchored portal tasks whose fixed alternating
paths have already been made resource-disjoint.  It is not yet valid after
the proposed one-order-per-root lower-exact selection.

There is a second shore restriction: the displayed ordered-shift list is
anchored at a tail root.  An odd-cycle absorber whose only usable portal row
lies on the head or owner shore needs a separate conjugate list theorem.

## 8. Exact interface with balanced-turn rounding

The strongest valid implication is conditional.

Assume a one-copy mixed-order selector has already produced a fixed rooted
flag table `F` such that:

1. its named suffix multiplicities have the required integer values;
2. its protected portal rows have robust lists measured in the **final
   mixed table**, i.e. a bound on `delta_F(b_h)`, not merely (7.3);
3. the bounded portal packets are conflict-free; and
4. after their resources are removed, the residual turn hypergraph is
   balanced and has fractional deficiency at most `C`.

Then the prepared-portal theorem and balanced-matrix integrality give turn
deficiency at most `C`.  If the separate upper/residence/physical compiler
hypotheses hold, the cited terminal conversion gives `B(k)+C` plus any
declared physical charge.

Neither Theorem 2.1 nor Theorem 3.1 supplies hypotheses 1--4.  In
particular:

* random atlas coverage is only support;
* the exact fractional suffix marginals do not give one-copy flags;
* Theorem 4.1 gives one-copy suffix balance only for the full local-order
  universe and does not create owner attachments or legal turns;
* balanced-turn rounding needs a fractional matching in the **turn
  hypergraph**, not merely a fractional suffix flow; and
* arbitrary prepared pins can already violate the balanced suffix face by
  Corollary 6.1.

Thus no exact or `O(1)` terminal conclusion currently follows.  The clean
remaining alternatives are:

\[
\boxed{\text{pin-admissible chain flow + mixed-order robust turn Hall}}
\]

or a direct absorber which simultaneously changes the prepared suffix
chains and the owner/turn matching.  Fractional feasibility alone cannot
replace either statement.
