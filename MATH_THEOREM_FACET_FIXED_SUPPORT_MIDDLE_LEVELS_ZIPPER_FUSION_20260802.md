# Fixed-support Middle-Levels zipper fusion for even dimension

Date: 2026-08-02  
Status: unconditional fusion of every module in one fixed-support
unbuffered reservoir into a single owner/q1-simple resident source cycle,
for even ambient dimension.  This is a partial-reservoir theorem, not a
complete carrier theorem.  It does not join different tag supports or
prove deeper upper/compiler gates.

## 0. Outcome

Let the ambient dimension `k=2r` be even and put

\[
 h=d+1\ge2,qquad s=r-h-1.                               \tag{0.1}
\]

Choose a refreshed point `beta` and a private tag pool

\[
 V=\mathbb Z_{2h},\qquad |V|=2h,                         \tag{0.2}
\]

disjoint from `beta`.  Put

\[
 G=[k]-(V\cup\{\beta\}).                                \tag{0.3}
\]

Then

\[
 |G|=k-2h-1=2(r-h-1)+1=2s+1.                            \tag{0.4}
\]

For every `s`-set `X subset G`, construct a length-`2h` alternating
unbuffered source cycle with core `X`, refreshed point `beta`, and tag pool
`V`.  There is a simultaneous choice of tag orders and `P/H` phases such
that all

\[
                         M=\binom{2s+1}{s}                \tag{0.5}
\]

cycles can be fused sequentially into one source cycle of length `2hM`.
Its length-`h` owner row is a simple Johnson cycle of rank `r`; its
immediate lower and upper palettes are simple of ranks `r-1,r+1`; and its
coordinate residence floor is at least `h`.

The proof combines the core-change zipper with a Middle Levels Hamilton
cycle on the outside cores.

## 1. A rainbow ordering of all outside cores

The bipartite Middle Levels graph on `G` has shores

\[
 \binom Gs\quad\text{and}\quad\binom G{s+1},             \tag{1.1}
\]

of equal size `M`.  By the Middle Levels Theorem it has a Hamilton cycle.
Write its alternating vertices as

\[
 X_0,R_0,X_1,R_1,\ldots,X_{M-1},R_{M-1},X_0.            \tag{1.2}
\]

Every `X_i` is an `s`-set, every `R_i` an `(s+1)`-set, and incidence in
(1.2) gives

\[
                         R_i=X_i\cup X_{i+1}.             \tag{1.3}
\]

Thus the cores `X_i,X_{i+1}` are adjacent, and the edge-union colours
`R_i` are all distinct.  Delete the last link and retain the path

\[
 X_0,X_1,\ldots,X_{M-1}                                 \tag{1.4}
\]

with distinct union colours `R_0,...,R_(M-2)`.

## 2. Explicit regenerating tag sockets

All tag arithmetic in this section is modulo `2h`.  Put

\[
                         u_i=i(h-1).                      \tag{2.1}
\]

Split the common tag pool into two halves

\[
\begin{aligned}
 A_i&=\{u_i,u_i+1,\ldots,u_i+h-1\},\\
 B_i&=V-A_i.
                                                               \tag{2.2}
\end{aligned}
\]

Consecutive halves have the exact intersections

\[
 A_i\cap A_{i+1}=\{u_i+h-1\},
 \qquad
 B_i\cap B_{i+1}=\{u_i-1\}.                              \tag{2.3}
\]

For an internal index, the preceding and following singleton intersections
inside `A_i` are `u_i` and `u_i+h-1`, which are different; inside `B_i`
they are `u_i+h` and `u_i-1`, also different.

Give the core-`X_i` source cycle the cyclic tag order

\[
 \mathcal V_i=
 (u_i,u_i+1,\ldots,u_i+h-1,
  u_i-1,u_i-2,\ldots,u_i+h).                             \tag{2.4}
\]

The first half is `A_i` and the second half is `B_i`.  There are two
distinguished cut edges:

* the incoming wrap socket

\[
              u_i+h\longrightarrow u_i;                 \tag{2.5}
\]

* the outgoing midpoint socket

\[
              u_i+h-1\longrightarrow u_i-1.              \tag{2.6}
\]

Equations (2.3) say exactly that the outgoing socket of cycle `i` and the
incoming socket of cycle `i+1` are cross-positioned reverse sockets:

\[
\begin{aligned}
 \operatorname{tail}(i,\mathrm{out})
   &=u_i+h-1=u_{i+1}
     =\operatorname{head}(i+1,\mathrm{in}),\\
 \operatorname{head}(i,\mathrm{out})
   &=u_i-1=u_{i+1}+h
     =\operatorname{tail}(i+1,\mathrm{in}).              \tag{2.7}
\end{aligned}
\]

Moreover, the preceding `h`-tag halo is `A_i`, the following halo is
`B_i`, and

\[
 |A_i\cap A_{i+1}|=|B_i\cap B_{i+1}|=1.                 \tag{2.8}
\]

Thus each new seam has exactly one repeated boundary tag and no second
active collision.

## 3. Exact `P/H` phase recursion

Let `epsilon_i` be the `P/H` type at position zero of cycle `i`, encoded in
`Z_2`.  Sources alternate around the even cycle.  The incoming wrap edge
has phase

\[
                         (1-\epsilon_i)\to\epsilon_i,     \tag{3.1}
\]

while the outgoing midpoint has phase

\[
 (\epsilon_i+h-1)\to(\epsilon_i+h)\pmod2.               \tag{3.2}
\]

Choose

\[
                         \epsilon_{i+1}=\epsilon_i+h
                         \pmod2.                          \tag{3.3}
\]

Then (3.1) for cycle `i+1` is exactly (3.2) for cycle `i`.
Consequently both cross seams remain alternating.  In words, retain the
phase when `h` is even and flip it when `h` is odd.

## 4. Sequential physical fusion

Start with the cycle for `X_0`.  Inductively suppose cycles
`0,...,i` have been fused and the `X_i` block is still contiguous with its
midpoint edge (2.6) intact.  Cut that midpoint edge and the incoming wrap
edge (2.5) of the standalone `X_(i+1)` cycle, and reconnect them crosswise.

The local cores are

\[
 X_i=C_i\cup\{a_i\},\qquad
 X_{i+1}=C_i\cup\{b_i\},                                \tag{4.1}
\]

by (1.3).  Equations (2.7)--(2.8) give the two tag zippers, and (3.3) gives
the parity compatibility.  The core-change zipper theorem therefore
applies.

At the source-word level the replacement has the schematic form

\[
 \cdots A_i\,B_i\cdots
 \quad\longmapsto\quad
 \cdots A_i\,A_{i+1}\,B_{i+1}\,B_i\cdots.               \tag{4.2}
\]

In particular the entire new block `A_(i+1) B_(i+1)` remains contiguous,
and its outgoing midpoint edge remains intact.  This proves the induction
and fuses all `M` source cycles into one.

## 5. Global named-deck simplicity

Let

\[
                         D=V\cup\{\beta\}.               \tag{5.1}
\]

Intersection with `G=[k]-D` is a complete collision invariant.

Every retained pure owner or q1 colour from cycle `i` has outside trace
exactly `X_i`.  Since the `X_i` are distinct, all pure decks from different
blocks are disjoint.  Pure decks of different ranks are separated by rank,
and each individual alternating cycle has simple owner/lower/upper q1
palettes because `2h>h+1`.

At zipper `i`, every mixed owner, every interior lower q1 colour, and every
new upper q1 colour has outside trace

\[
                         X_i\cup X_{i+1}=R_i.             \tag{5.2}
\]

These traces have size `s+1`, so they cannot equal a pure trace `X_j` of
size `s`.  The `R_i` are pairwise distinct by (1.2), so different zippers
cannot collide.  Within one zipper, the two seam tags and the Johnson
geodesic formulas give simplicity.

The endpoint lower q1 colours have traces `X_i` or `X_(i+1)`.  As proved in
the core-change zipper theorem, they are exactly the unique proper
`(h-1)`-interval colours exposed at the deleted socket.  Their original
occurrences are removed by the rethread, and the two sockets of one block
are distinct.  Therefore they do not duplicate a retained pure colour or
one another.

It follows that the final source cycle has exactly `2hM` distinct owners
and `2hM` distinct colours on each immediate shore.

## 6. Residence

Every final owner is the union of `h` consecutive sources.  Each source
occurrence of a coordinate creates an interval of `h` consecutive owner
occurrences, and unions of such intervals have no positive component
shorter than `h`.  Hence the final cyclic owner chronology has residence
floor at least `h`.

This argument is independent of how many sequential zippers were used; it
is exactly why the length-`2h` socket construction regenerates without
accumulating a residence sidecar.

## 7. Scale and relation to clustered pruning

One fixed support contains

\[
 M=\binom{k-2h-1}{r-h-1}                                 \tag{7.1}
\]

modules.  Since `h=Theta(sqrt(k))`,

\[
                         M=\Theta(W/2^{2h}).              \tag{7.2}
\]

Each **unfused module** still has only `O(h^2)=O(q^2)` named occurrence
cylinders.  At the scalar candidate-count level, sampling the reciprocal
number of supports has the prospective product

\[
 \Theta(2^{2h}/q^2)\text{ supports}
 \times\Theta(W/2^{2h})\text{ modules per support}
 =\Theta(W/q^2).                                         \tag{7.3}
\]

Equation (7.3) records only compatibility of candidate scales; it is not a
new cross-support packing theorem.  The existing clustered-pruning proof
deletes individual colliding modules.  Such deletions fragment the
Middle-Levels core path, so the fixed-support one-component conclusion does
not survive verbatim.  Conversely, treating the whole fused reservoir as
one atom multiplies its footprint by `M` and has no proved support-level
conflict bound.  A valid cross-support theorem must either prune in long
contiguous core paths, absorb the deleted cores, or prove a new whole-path
collision estimate.

## 8. Strict scope and remaining gates

This theorem closes a specific regeneration gap: for even `k`, every
module in one fixed-support reservoir can be fused into one component using
literal regenerated sockets, while keeping owner/q1 simplicity and
residence.

It does not prove:

* a corresponding all-core fusion for odd `k` (`G` then has size `2s`, so
  there are fewer `(s+1)` union colours than `s`-cores);
* pairwise disjointness or fusion between different tag supports;
* preservation of the original named owner palette--the zipper halos are
  rethreaded;
* coverage of upper ranks `r+2,...,k`;
* the complete lower marked deck, occurrence positions, or compiler/common
  cap;
* a universal word, `B(k)+O(1)`, or `nu(k)=B(k)`.

The next connector problem is smaller but still correlated: sparsify these
length-`2h` reservoirs while retaining long core paths (or absorbing path
breaks), then connect the surviving support-components without losing the
outside-trace separation or the deep guards.
