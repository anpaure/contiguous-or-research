# Diagonal typed-token matching and the single-role terminal-socket cut

**Date:** 2026-08-03  
**Status:** exact occurrence theorem and exact capacity obstruction on the
single-role face.  No finite search is used.  The result does not forbid a
complete dual-role ticket which lets one physical occurrence serve both its
upper-witness and terminal-socket semantics, and it does not forbid a new
remote bank of typed sinks.

## 0. Result

Put, throughout, `m>=3` (equivalently `k>=5`),

\[
 k=2m-1,\qquad r=m,\qquad
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname {Cat}_m={2W\over m+1}.              \tag{0.1}
\]

Let a cyclic q1-exact literal diagonal row have owner occurrences

\[
 T_i=\bigcup_{h=i}^{i+d}A_h,
 \qquad
 P_i=\bigcup_{h=i+1}^{i+d}A_h=T_i\cap T_{i+1},
 \qquad i\in\mathbb Z_W.                                \tag{0.2}
\]

Its upper-turn occurrence at the cut `i|i+1` is

\[
 Q_i=[i,i+d+1],\qquad
 R_i=\operatorname {OR}(Q_i)=T_i\cup T_{i+1}.             \tag{0.3}
\]

There are two sharply different conclusions.

1. **Typed occurrence matching is automatic on the cyclic carrier.**  The
   occurrence graph between the `W` owner occurrences and the `W` cyclic
   upper-turn occurrences, with `Q_i` adjacent to `T_i,T_(i+1)`, is a single
   even cycle.  Hence it has two perfect matchings; explicitly,
   `T_i -> Q_i` is one.  Thus no additional Hall or common-basis theorem is
   needed to assign each owner a containing upper occurrence on that cyclic
   row.  A literal linear opening has only `W-1` internal q1 seams unless the
   wrap occurrence is exported separately; the capacity obstruction below
   remains valid because it deliberately grants all `W` cyclic candidates.

2. **Unused terminal capacity is not automatic.**  Suppose every physical
   occurrence has one unit of capacity, a cell used as a lower, owner, or
   required upper witness cannot simultaneously be called an *unused*
   terminal socket, and owner capacities are reserved.  At exact length
   `B(k)=W+d`, let

   \[
    \Lambda=\sum_{s=1}^{m-1}{k\choose s},\qquad
    \tau_d={d(d+1)\over2},\qquad
    \sigma=dW+\tau_d-\Lambda.                            \tag{0.4}
   \]

   Then all surplus q1 occurrences together with all unused short/common-cap
   cells supply at most

   \[
                         C+\sigma                              \tag{0.5}
   \]

   pairwise distinct sockets.  Consequently every terminal linkage of all
   `W` routed owner types from only those resources has deficiency at least

   \[
                  \boxed{(W-C-\sigma)_+}.                       \tag{0.6}
   \]

   The Ferrers boundary is already contained in the short-cell ledger in
   (0.4).  A boundary cell used for a lower target is not an additional
   unused socket.

At length `B(k)+1`, the raw short-interval count increases by `W+d+1`.
On the same width-`d+1` diagonal-owner face, exactly `W` units in that
enlarged pool are reserved for the central owner row.  On this no-alias
reserved-owner face, the corresponding bound is therefore

\[
             \#\{\text{available single-role sockets}\}
             \le C+\sigma+d+1,                              \tag{0.7}
\]

and terminal deficiency is at least

\[
                  \boxed{(W-C-\sigma-d-1)_+}.                 \tag{0.8}
\]

Thus the familiar `+W` scalar increase at `B+1` is not by itself a fresh
socket bank.  It consists of the newly admitted width-`d+1` band, whose
`W` selected units are precisely the reserved central owners, plus only
`d+1` residual triangular/boundary units.

More generally, assume the stronger **graded-upper-exact diagonal-band**
hypothesis: for every admitted band `1<=j<c`, that band witnesses every
rank-`m+j` target.  At fixed additive charge `c>=1`, after reserving all
strict lower targets, `W` central owners, and one witness for every such
upper target, the maximum single-role free capacity is

\[
 F_c\le
 \sigma+(\tau_{d+c}-\tau_d)
 +\sum_{j=1}^{c-1}\left(W-{2m-1\choose m+j}\right)
 +\mathbf 1_{c=1}C.                                        \tag{0.9}
\]

For every fixed `c`, apart from the uncontrolled scalar `sigma`, the right
side contributes only `o(W)`:

\[
 \tau_{d+c}-\tau_d=O_c(d),\qquad
 \sum_{j=1}^{c-1}\left(W-{2m-1\choose m+j}\right)
 =O_c(W/m)=o(W).                                           \tag{0.10}
\]

Equations (0.5)--(0.10) are terminal-cut obstructions, not impossibility
theorems for `nu(k)<=B(k)+O(1)`.  The exact escape is one of:

* a proved complete dual-role bundle using load-bearing occurrences as
  terminal resources without splitting one physical capacity;
* a new capacity-faithful `W-O(1)` typed sink bank; or
* a different common-cap linkage whose literal capacity ledger proves the
  same rank directly.

The raw short-cell slack at charge `c` is

\[
 \sigma_c=\sigma+cW+cd+{c(c+1)\over2}.                       \tag{0.11}
\]

Thus at `c=1` raw scalar cardinality alone no longer obstructs `W` sinks.
The no-alias cut (0.8) survives only because its `W` central-owner units are
reserved; it is a role/type statement, not a scalar one.

## 1. The automatic typed occurrence matching

Give `Q_i` its literal occurrence address, not merely its upper value
`R_i`.  Form the bipartite occurrence graph

\[
 {\cal H}=\bigl(\{T_i:i\in\mathbb Z_W\},
                 \{Q_i:i\in\mathbb Z_W\};E\bigr),             \tag{1.1}
\]

where

\[
                  N_{\cal H}(Q_i)=\{T_i,T_{i+1}\}.             \tag{1.2}
\]

Every `Q_i` has degree two.  Every `T_i` is incident with `Q_(i-1)` and
`Q_i`, so it also has degree two.  The chronological addresses make

\[
 T_0,Q_0,T_1,Q_1,\ldots,T_{W-1},Q_{W-1},T_0             \tag{1.3}
\]

one alternating cycle.  Therefore

\[
 \theta^-(T_i)=Q_i,
 \qquad
 \theta^+(T_i)=Q_{i-1}                                   \tag{1.4}
\]

are its two perfect matchings.  Both are correctly typed by containment:

\[
 T_i\subseteq R_i,
 \qquad
 T_i\subseteq R_{i-1}.                                   \tag{1.5}
\]

This proof retains occurrence addresses.  If the q1 palette is the simple
cap-two target `1+1_D`, then the token multiset has one token for every
upper colour and one extra token for every `R in D`, but (1.4) is stronger
than a value-level capacitated Hall theorem: it matches the actual turn
tokens already present in the row.

This is a theorem about the cyclic carrier occurrence graph.  Opening the
carrier into a literal linear word removes the wrap turn unless a separately
priced boundary occurrence realizes it.  Therefore (1.4) alone is not a
`W`-token literal matching theorem for an unaugmented linear opening.

The conclusion also stops before capacity reservation.  If an occurrence in
(1.4) has already been consumed by another single-role ticket, writing down
the same address a second time does not create a second physical socket.

For comparison, if only the abstract cap-two value multiset `1+1_D` is
given, make two formal copies of every upper colour and let the resulting
tokens be adjacent to the middle owners they contain.  The base-copy tokens
are independent in this transversal matroid, and contraction by them gives
a rank-`C` matroid on the duplicate copies.  A `C`-set `D` is a basis of
that contraction exactly when

\[
 |N(X)|+|D\cap N(X)|\ge |X|
 \qquad\text{for every family }X\subseteq { [2m-1]\choose m}. \tag{1.6}
\]

The realized diagonal row certifies this basis condition through (1.4).
Coordinate-regularity and cap-two multiplicities alone do not constitute
that occurrence certificate.

For completeness, the matroid ranks follow from elementary incidence
counting.  The rank-`(m+1)`/rank-`m` inclusion graph has degrees `m+1` and
`m-1`.  Hence every upper family `Y` has

\[
 |N(Y)|\ge {m+1\over m-1}|Y|\ge |Y|,                  \tag{1.7}
\]

so the base copies match injectively to owners.  Conversely every owner
family `X` has

\[
 2|N(X)|\ge {2(m-1)\over m+1}|X|\ge |X|               \tag{1.8}
\]

for `m>=3`; the two-copy token graph therefore saturates all `W` owners.
Its transversal rank is `W`, and contraction by the `U` independent base
copies has rank `W-U=C`.  Hall on the owner shore after retaining only the
duplicate copies indexed by `D` is exactly (1.6).

## 2. Exact capacity at `B(k)`

For a word of length `W+d`, the number of linear interval cells of lengths
at most `d` is

\[
 \sum_{\ell=1}^d(W+d-\ell+1)
 =dW+\tau_d.                                             \tag{2.1}
\]

An exact lower compiler uses `Lambda` distinct such cells.  Hence at most

\[
                        \sigma=dW+\tau_d-\Lambda             \tag{2.2}
\]

of them are unused.  This count already includes every triangular/Ferrers
boundary address: the boundary is a particular part of (2.1), not another
physical bank.  In particular, if

\[
 h=(\Lambda-dW)_+\le\tau_d                              \tag{2.3}
\]

boundary cells are installed and assigned to lower targets, those `h`
cells belong to the `Lambda` consumed units in (2.2).

The cyclic q1 upper row contains `W` occurrence tokens.  In a literal
linear opening there are only `W-1` internal width-`d+2` intervals unless
the wrap turn is exported by a separately priced boundary occurrence.
For the obstruction we grant all `W` cyclic candidates; this can only
increase the alleged socket supply.  In the simple cap-two
target there are `U` distinct upper colours and exactly `C=W-U` surplus
occurrences.  Reserving at least one occurrence for every required upper
colour leaves at most `C` unused q1 addresses.  The q1 cells have width
`d+2`, so they are disjoint as interval addresses from the short-cell pool
in (2.1).

Thus the union of the two proposed single-role banks has capacity at most
`sigma+C`.  A linkage of `W` unit ports to distinct terminal units needs
at least `W` units across the terminal cut.  This proves (0.5)--(0.6).
Typed restrictions, phase restrictions, or common-cap product closure can
only reduce the rank further.

There is an exact Rado/gammoid restatement.  In either occurrence coordinate
of the terminal common-cap theorem, let `I` be the `W` owner tickets and let
`S` be the admitted free terminal bank.  For the full ticket set,

\[
 r_N(A(I))\le |S|\le C+\sigma.                         \tag{2.4}
\]

Taking `J_0=I,J_1=emptyset` (or the other coordinate) in the exact common
deficiency formula gives

\[
 \delta\ge |I|-r_N(A(I))
 \ge (W-C-\sigma)_+.                                  \tag{2.5}
\]

Hence the cut is already present in the exact occurrence-labelled Rado
theorem; it is not an artefact of forgetting types.

## 3. Why `B+1` does not export `W` fresh no-alias sockets

At length `W+d+1`, the number of interval cells of lengths at most `d+1`
is

\[
 (d+1)W+\tau_{d+1}.                                    \tag{3.1}
\]

Subtracting (2.1) gives

\[
 \bigl((d+1)W+\tau_{d+1}\bigr)
 -(dW+\tau_d)=W+d+1.                                   \tag{3.2}
\]

On the width-`d+1` diagonal-owner face, there are two equivalent ways to see
the two terms.

* The newly admitted width-`d+1` band contains the central owner row, of
  which `W` distinct occurrences are reserved.
* The remaining `d+1` is the triangular endpoint/insertion correction.

After retaining the exact lower compiler and reserving the owner row, at
most

\[
 (d+1)W+\tau_{d+1}-\Lambda-W=\sigma+d+1               \tag{3.3}
\]

short-or-new units remain.  Adjoining the `C` surplus q1 tokens proves
(0.7)--(0.8).  Counting all `W+d+1` units in (3.2) as free sockets would
split the already reserved central owner capacities.

## 4. Fixed additive charge

Let `c>=1` and `e=d+c`.  Continue to assume the same width-`d+1` diagonal
owner band.  The interval pool through width `e` has size

\[
                         eW+\tau_e.                         \tag{4.1}
\]

Under the graded-upper-exact diagonal-band hypothesis, reserve:

* `Lambda` cells for strict-lower targets;
* `W` cells for the central owner row; and
* for every `1<=j<=c-1`, at least
  \({2m-1\choose m+j}\) cells witnessing all rank-`m+j` targets in the
  corresponding admitted upper band.

The remaining capacity is at most

\[
 \begin{aligned}
 &(d+c)W+\tau_{d+c}-\Lambda-W
 -\sum_{j=1}^{c-1}{2m-1\choose m+j}\\
 &\qquad=
 \sigma+(\tau_{d+c}-\tau_d)
 +\sum_{j=1}^{c-1}\left(W-{2m-1\choose m+j}\right).
                                                               \tag{4.2}
 \end{aligned}
\]

Without that graded-upper-exact hypothesis, (4.2) is not asserted: q1
exactness alone says nothing about ranks `m+j` for `j>=2`.

For `c=1`, the q1 band is outside this admitted short pool; allowing its
surplus occurrences as extra sockets adds the final term in (0.9).  For
`c>=2`, the q1 surplus is already the `j=1` term of (4.2), so adding `C`
again would double count the same occurrence addresses.  The exact-length
case `c=0` is Section 2, not (4.2).

Finally,

\[
 { {2m-1\choose m+j}\over W}
 =\prod_{\ell=1}^j{m-\ell\over m+\ell}.                  \tag{4.3}
\]

For fixed `j`, the elementary product bound gives

\[
 0\le 1-\prod_{\ell=1}^j{m-\ell\over m+\ell}
 \le\sum_{\ell=1}^j{2\ell\over m+\ell}
 =O(j^2/m).                                             \tag{4.4}
\]

Also `d=Theta(sqrt(m))`, so

\[
 \tau_{d+c}-\tau_d=cd+{c(c+1)\over2}=O_c(\sqrt m).      \tag{4.5}
\]

Equations (4.2)--(4.5) prove (0.9)--(0.10).

## 5. Calibrations

### `k=9`

Here

\[
 m=5,\quad W=126,\quad C=42,\quad d=2,\quad
 \Lambda=255,\quad \sigma=2(126)+3-255=0.             \tag{5.1}
\]

Therefore the exact-length single-role bank has at most `42` sockets and
deficiency at least

\[
                         126-42=84.                         \tag{5.2}
\]

At `B+1` it has at most `45` sockets and deficiency at least `81` after
the central owner row is reserved.

### `k=17`

Here

\[
 m=9,\quad W=24310,\quad C=4862,\quad d=3,\quad
 \Lambda=65535,\quad \sigma=3(24310)+6-65535=7401.     \tag{5.3}
\]

Thus the exact-length bank has capacity at most

\[
                         4862+7401=12263                 \tag{5.4}
\]

and deficiency at least

\[
                         24310-12263=12047.              \tag{5.5}
\]

At `B+1`, the no-alias capacity is at most `12267` and the corresponding
deficiency is at least `12043`.

These are scoped terminal-cut numbers.  They neither contradict the known
optimal `k=9` and `k=15` words nor prove a lower bound beyond `B(17)`:
their certificates necessarily bundle roles or use a sink bank outside
this restricted single-role inventory.

## 6. Exact frontier

The q1-exact diagonal theorem and the cap-two target theorem therefore fit
together as follows:

\[
 \boxed{
 \begin{array}{c}
 \text{typed owner-to-upper-occurrence matching: automatic},\\
 \text{unused capacity-faithful socket export: not automatic}.
 \end{array}}
                                                               \tag{6.1}
\]

The exact positive target is no longer an abstract containment matching.
It is a **role-coinstantiation theorem**: prove that the complete upper
witness ticket and the terminal suffix ticket coexist on the matched
occurrence without duplicating its unit capacity, or construct a separate
`W-O(1)` addressed typed sink bank.  The exact terminal common-cap/Rado
theorem then checks the two occurrence coordinates and product closure.
