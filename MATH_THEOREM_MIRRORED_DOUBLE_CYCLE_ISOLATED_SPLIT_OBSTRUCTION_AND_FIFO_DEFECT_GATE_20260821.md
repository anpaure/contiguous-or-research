# Mirrored double cycles cannot split in isolation, and their FIFO defect is exact

**Date:** 2026-08-21  
**Status:** unconditional local correction obstruction and exact conditional
fragmentation bound; no global ordinary-wreath completion is claimed

## 0. Outcome

Put `r>=2` and

\[
                  b=2r+1,\qquad J=[2r],\qquad *=2r+1.       \tag{0.1}
\]

The complement/time-reversal phase construction produces paired
length-`2r` odd-graph paths.  Under the required global distinct-union-
colour hypothesis, each pair is a simple cycle of length `2b=4r+2`.
This note proves three exact facts about the proposed correction.

1. **No isolated split.**  No such simple doubled cycle can be repartitioned,
   using its own vertices, into two ordinary length-`b` wreath cycles.  This
   remains false even if arbitrarily many induced chords are available.
2. **Cluster balance.**  A collection of `k` doubled cycles can be
   repartitioned internally into `2k` wreaths only if its coordinate swap
   counts are exactly balanced coordinate by coordinate.  Hence any repair
   must couple different root pairs; the endpoint involution cannot be fixed
   pair by pair.
3. **Near-FIFO alternative.**  If one doubled pair has hole defect `delta`,
   deleting at most `2 delta` transitions from either constituent path breaks
   it into at most `2 delta+1` genuine sliding-window arcs.  At depth `q`, the
   boundary collar is `O(q(delta+1))` per pair.  Thus a global bound
   `sum delta=O(Cat_r)` would give the sharp `O(A/r)` source-piece scale and
   `o(A)` loss at each depth `q<=H=o(r)`, but distinct colours alone do not
   imply this defect bound.

The first two facts are a theorem-grade obstruction to the concrete
double-cycle-to-two-wreath correction.  The third isolates a different,
conditional fragment route.  It does not close those fragments into a
global ordinary wreath factor.

## 1. One doubled path and its exact hole word

Let

\[
                         X_0,X_1,\ldots,X_r             \tag{1.1}
\]

be rank-`r` subsets of `J`, with consecutive sets at Johnson distance one.
Write

\[
 \begin{split}
 d_t&\in X_{t-1}-X_t,\qquad a_t\in X_t-X_{t-1},\\
 T_t&=X_{t-1}\cap X_t,\qquad
 C_t=J-(X_{t-1}\cup X_t) \qquad(1\le t\le r).
 \end{split}                                             \tag{1.2}
\]

The odd-graph lift of (1.1) is

\[
 X_0,\ \{*\}\cup C_1,\ X_1,\ldots,
 \{*\}\cup C_r,\ X_r.                                  \tag{1.3}
\]

The complement-reverse path is

\[
 J-X_r,\ \{*\}\cup T_r,\ J-X_{r-1},\ldots,
 \{*\}\cup T_1,\ J-X_0.                                \tag{1.4}
\]

Joining the two displayed paths by the complement edges at their ends gives
the doubled closed walk `D(X)`.  Its edge-hole word is exactly

\[
 (a_1,d_1,\ldots,a_r,d_r,*,
   a_r,d_r,\ldots,a_1,d_1,*).                            \tag{1.5}
\]

Indeed, the unique label outside
`X_{t-1} union ({*} union C_t)` is `a_t`, and the unique label outside
`({*} union C_t) union X_t` is `d_t`.  The same calculation on (1.4)
gives the reverse list of ordered pairs.

For `x in J`, define

\[
 s_x=|\{t:x\in\{a_t,d_t\}\}|,
 \qquad
 \delta(X)=\sum_{x\in J}(s_x-1)_+ .                     \tag{1.6}
\]

Since `sum_x s_x=2r=|J|`,

\[
 \delta(X)=|\{x:s_x=0\}|=2r-|\{x:s_x>0\}|.             \tag{1.7}
\]

### Lemma 1.1 (phase map and simplicity hypothesis)

In the mirrored Chung--Feller phase ansatz, let

\[
 G=f_{h-1}\cdots f_0:{\cal D}^0\longrightarrow {\cal D}^h,
 \qquad \sigma=G^{-1}cG,                                \tag{1.8}
\]

where `r=2h` and `c` is complementation on `J`.  The path rooted at
`P in D^0` has endpoint `c sigma(P)`, and the path rooted at `sigma(P)`
is its complement reverse.  The map `sigma` is a fixed-point-free
involution.

If, in addition, all intermediate union colours in the odd-graph lifts are
globally distinct, then the lifted paths are vertex-disjoint and their
complement closure is a factor into simple doubled cycles `D(X)`.

#### Proof

The endpoint and involution statements are the typed identity
`sigma=G^{-1}cG`.  The non-anchor vertices are already distinct because
the transition bijections give a path cover of the disjoint phase classes.
An intermediate anchor vertex is `{*} union C_t`; global distinctness of
these colours is exactly the remaining vertex-disjointness condition.
The complement closure then pairs the two paths in each orbit of `sigma`.
`square`

The distinct-colour condition is essential.  Without it, (1.3)--(1.5) are
identities for serialized paths, but there need not be a simple odd-graph
cycle or a doubled factor.

## 2. Every shortest odd cycle is a wreath

### Lemma 2.1

Every closed walk of length `b=2r+1` in `O_r=KG(2r+1,r)` has each edge-hole
label exactly once.  In particular, every simple `b`-cycle is an ordinary
wreath cycle, and each ground coordinate occurs in exactly `r` of its
vertices.

#### Proof

For an edge `V_i V_{i+1}`, let `z_i` be its unique hole, so

\[
                         V_{i+1}=[b]-(V_i\cup\{z_i\}).     \tag{2.1}
\]

If a coordinate `x` never occurred among the `z_i`, its membership bit
would toggle at all `b` steps.  Since `b` is odd, the walk could not close.
Thus every one of the `b` coordinates occurs at least once among the `b`
holes, and consequently occurs exactly once.

Starting immediately after the unique `x`-hole, the membership bit of `x`
alternates around the other `2r` edges.  It is one on exactly `r` vertices.
The hole permutation reconstructs the usual cyclic-window order, proving
the wreath assertion. `square`

## 3. The isolated-split obstruction

### Theorem 3.1 (exact point-degree identity)

Assume `D(X)` is simple.  For every `x in J`, its number of occurrences
among the `2b` vertices of `D(X)` is

\[
                              2r+1-s_x.                    \tag{3.1}
\]

The anchor `*` occurs exactly `2r` times.

#### Proof

For each `0<=t<=r`, exactly one of `X_t` and `J-X_t` contains `x`.
The `2r+2` non-anchor vertices therefore contribute `r+1` occurrences.

At transition `t`, the sets `T_t` and `C_t` are disjoint and cover
`J-{a_t,d_t}`.  They contribute one occurrence of `x` unless `x` is a
swapped coordinate, when they contribute zero.  The `2r` anchor vertices
therefore contribute `r-s_x`.  This proves (3.1).  Every one of those
anchor vertices contains `*`. `square`

### Theorem 3.2 (no doubled cycle splits in isolation)

No simple doubled cycle `D(X)` can be partitioned, on the same vertex set,
into two length-`b` cycles of the odd graph.  Equivalently, it cannot be
repaired into two ordinary wreaths by any collection of chords internal to
its own vertex set.

#### Proof

By Lemma 2.1, two length-`b` cycles would contain every coordinate exactly
`2r` times.  Comparing with (3.1) forces

\[
                              s_x=1\quad(x\in J).           \tag{3.2}
\]

Every coordinate initially in `X_0` must then be deleted at its unique
appearance, and every coordinate outside `X_0` must be added.  Hence
`X_r=J-X_0`.  But then the first and last non-anchor vertices in the two
halves of `D(X)` coincide, contrary to simplicity.

In the phase notation, `X_0=P` and `X_r=J-sigma(P)`, so the same conclusion
would say `sigma(P)=P`, contradicting the fixed-point-free involution in
Lemma 1.1. `square`

This is stronger than the elementary two-edge gate.  The odd graph has no
`C_4`: four distinct alternating vertices would give two disjoint unions of
size at least `r+1`, requiring at least `2r+2` ground coordinates.  Thus a
two-factor exchange cannot begin with two changed edges.  Theorem 3.2 says
that, for one doubled pair, no number of internal edge changes suffices.

### Corollary 3.3 (sharp local defect and endpoint distance)

Let `P=X_0` and write `X_r=J-Q`.  Then

\[
                   \delta(X)\ge d_J(P,Q).                  \tag{3.3}
\]

If `D(X)` is simple, then `d_J(P,Q)>=1`.  Consequently, a simple mirrored
factor with `m=Cat_r` phase paths and `m/2` doubled cycles has total defect
at least `m/2=A/(2b)`.

#### Proof

Membership of `x` toggles exactly `s_x` times along the Johnson path.
Therefore

\[
 P\mathbin\triangle Q
   =X_r\mathbin\triangle(J-X_0)=\{x:s_x\text{ is even}\}. \tag{3.4}
\]

There are exactly `delta` zero-multiplicity coordinates by (1.7), and at
most `delta` positive even-multiplicity coordinates, since each of the
latter contributes at least one to (1.6).  Hence
`|P triangle Q|<=2 delta`, proving the first inequality.  The second is
automatic in the phase setting from the fixed-point-free property.  More
generally, if `P=Q`, then `X_r=J-X_0`; the two halves of `D(X)` repeat their
endpoint vertices, so `D(X)` is not simple. `square`

### Proposition 3.4 (adjacent endpoints are abstractly sufficient for defect one)

Conversely, if rank-`r` sets `P,Q subset J` are adjacent in the Johnson
graph, there is a length-`r` Johnson path from `P` to `J-Q` with
`delta=1`.

#### Proof

Write

\[
                 P=S\cup\{u\},\qquad Q=S\cup\{v\},       \tag{3.5}
\]

where `|S|=r-1`, and put
`R=J-(S union {u,v})`, so `|R|=r-1`.  Choose enumerations
`S={s_1,...,s_{r-1}}` and `R={z_1,...,z_{r-1}}`.  Make the swaps

\[
 s_1\mapsto v,\qquad v\mapsto z_1,\qquad
 s_i\mapsto z_i\quad(2\le i\le r-1).                  \tag{3.6}
\]

There are exactly `r` swaps.  They finish at `R union {u}=J-Q`.
The coordinate `u` is omitted, `v` occurs twice, and every other coordinate
occurs once, so `delta=1`. `square`

Together with Corollary 3.3, this says that defect-one paths exist exactly
for adjacent endpoint pairs **when the Chung--Feller phase constraints are
ignored**.  For necessity, if `delta=1`, (1.7) gives exactly one
zero-multiplicity coordinate, while the excess-one identity gives exactly
one coordinate of multiplicity two and all others multiplicity one.
Equation (3.4) then has exactly two coordinates, so `d_J(P,Q)=1`.
Requiring the intermediate set at time `t` to lie in
`D^t`, and requiring all such paths simultaneously to partition every
phase, is an additional routing problem; Proposition 3.4 does not solve it.

## 4. Cross-pair balance is necessary

There is no root-level obstruction to pairing adjacent Dyck words when `r`
is even.  Ruskey and Proskurowski, *Generating binary trees by
transpositions*, Journal of Algorithms 11 (1990), 68--84,
doi:`10.1016/0196-6774(90)90030-I`, prove that all semilength-`r` Dyck
words admit an adjacent-transposition Gray listing exactly when `r` is even
or `r<5`.  For even `r`, the Catalan number is even; pairing consecutive
words in that listing gives a perfect matching of `D^0` by Johnson edges.
Proposition 3.4 therefore gives an abstract defect-one path for every root
pair.  It does **not** make those paths simultaneously traverse the fixed
phases or balance their union colours; those remain global constraints.

### Theorem 4.1 (cluster balance)

Let `D(X^1),...,D(X^k)` be vertex-disjoint simple doubled cycles.  If their
combined vertex set can be partitioned into `2k` ordinary wreath cycles,
then, for every `x in J`,

\[
                         \sum_{p=1}^k s^p_x=k.             \tag{4.1}
\]

#### Proof

Sum (3.1) over the `k` doubled cycles.  The left side has coordinate degree
`k(2r+1)-sum_p s^p_x`.  By Lemma 2.1, the proposed `2k` wreaths have degree
`2kr`.  Equality gives (4.1). `square`

For `k=1`, (4.1) recovers the necessary condition (3.2), whose
incompatibility with simplicity proves Theorem 3.2.  For a global exact doubled factor,
(4.1) summed over all root pairs holds automatically because the doubled
factor covers the entire middle layer.  Thus (4.1) is a **local-to-global
gate**, not a global point-margin obstruction: a possible correction must
move vertices between different root pairs or use a genuinely global
trade.  Coordinate balance is necessary, not sufficient, for such a
repartition.

## 5. Exact FIFO-defect fragmentation

The full mirrored paths are not FIFO arcs.  In fact, `delta>=1` by
Corollary 3.3.  Nevertheless their failure is measured exactly by `delta`.

### Lemma 5.1 (clean blocks are sliding-window arcs)

Take a consecutive block of transitions in (1.1).  If all labels

\[
                         a_i,d_i                              \tag{5.1}
\]

used by that block are distinct, its sets are consecutive rank-`r` windows
of a word of distinct labels.

#### Proof

At the first set of the block, every future deleted label is present.  It
cannot have been added inside the block, because that would repeat its
label.  Similarly, every future added label is absent initially and cannot
be deleted inside the block.  If the block deletes
`d_1,...,d_l` and adds `a_1,...,a_l`, let `K` be the common untouched core.
Then its successive windows are the length-`r` windows of

\[
                   d_1\cdots d_l\;K\;a_1\cdots a_l,        \tag{5.2}

with an arbitrary fixed ordering of `K`. `square`

### Theorem 5.2 (defect-to-fragments bound)

Delete every transition containing a label whose multiplicity `s_x` is at
least two.  From either constituent Johnson path of `D(X)`, this deletes at
most `2 delta(X)` transitions and leaves at most `2 delta(X)+1` maximal
sliding-window arcs.  The two paths have the same defect and together leave
at most `4 delta(X)+2` arcs.

After trimming `q` starts at every artificial arc boundary, the number of
discarded depth-`q` starts is

\[
                         O(q(\delta(X)+1)).                 \tag{5.3}

All retained same-start targets through depth `q` are genuine nested
interval targets of their physical arc.

#### Proof

If `s_x>=2`, then `s_x<=2(s_x-1)`.  Hence the total number of occurrences
of repeated labels is at most

\[
       \sum_{x:s_x\ge2}s_x
       \le2\sum_x(s_x-1)_+=2\delta(X).                    \tag{5.4}

The number of deleted transitions is no larger.  The surviving transition
blocks satisfy Lemma 5.1, and deleting `e` transitions creates at most
`e+1` blocks.  The complement-reverse path has the same multiplicities.
Finally, a depth-`q` interval can cross a new boundary only if its start is
within `q` positions of that boundary, proving (5.3). `square`

Let `Delta=sum_p delta(X^p)` over the `m/2` doubled pairs.  The theorem gives
at most

\[
                          4\Delta+m                         \tag{5.5}

physical arc pieces and fixed-depth collar loss

\[
                          O(q(\Delta+m)).                   \tag{5.6}

Thus the still-open estimate

\[
                          \Delta=O(m)                       \tag{5.7}

would be best possible up to constants and would imply:

* `O(m)=O(A/b)=O(A/r)` physical source/boundary loss;
* `O(qA/b)=o(A)` loss at every `q<=H=o(b)`; and
* aggregate collar loss `O(H^2A/b)=o(HA)` over all depths through `H`.

Neither the pointwise phase bijections nor global distinctness of the q1
union colours proves (5.7).  Equation (5.7), correlated all-depth coupon
coverage inside the retained arcs, and completion of the fragments into an
ordinary wreath factor are three separate gates.

## 6. Scope

The proved obstruction assumes the doubled cycle itself is simple; in the
phase construction that is exactly where global union-colour distinctness
is used.  Without it there is only a serialized Johnson path cover.

The theorem rules out an **independent per-pair** correction, including all
same-vertex `C_6`, `C_8`, or longer chord recuts.  It does not rule out a
trade involving several doubled cycles, an absorber using vertices from a
reserve, or a global ordinary wreath factor.  The fragmentation theorem is
a partial-arc statement and does not silently supply any of those global
objects.

## 7. Finite audit

The H100 checker

```text
scratch/audit_mirrored_double_cycle_split_and_fifo_defect_20260821.py
```

verifies (1.5), (3.1), (3.3), the adjacent-endpoint construction, and the
transition-deletion/clean-block assertions of Theorem 5.2 on exhaustive
Johnson paths for the smallest ranks and on the canonical mirrored phase
paths for `r=4,6,8`.  It also enumerates the induced odd subgraphs at those
ranks and confirms that none has a two-wreath factor.  The depth-`q` collar
bound is proved directly and is not separately enumerated.  The finite
enumeration is evidence; Theorems 3.1--5.2 are independent of it.
