# Constant-weight packet hypergraphs: exact incidence, the genuine atlas escape, and the colored matching gate

Date: 2026-07-26

## 0. Outcome

Let

\[
 V_m=\binom{[2m]}m,
 \qquad W=W_m=|V_m|=\binom{2m}m.
\]

For `1 <= r <= m`, define the packet hypergraph `H_(m,r)` as follows.  An
edge is specified by

* a core `F` of size `m-r`;
* `r` pairwise disjoint unordered pairs
  `M={e_1,...,e_r}` in `[2m]\F`.

Its owner set is

\[
 P(F,M)=\left\{F\cup\{x_1,\ldots,x_r\}:x_i\in e_i\right\}.
 \tag{0.1}
\]

Thus every edge is a physical isometric `Q_r` in the middle layer and has
size `k=2^r`.

The audit has four conclusions.

1. `H_(m,r)` is exactly regular.  Its degree, number of edges, and
   Johnson-distance codegrees are

   \[
   D_{m,r}=\binom mr^2r!,
   \qquad
   |E(H_{m,r})|={ (2m)!\over 2^r r!(m-r)!^2},
   \tag{0.2}
   \]

   \[
   \lambda_a=
   \begin{cases}
   \displaystyle
   \binom{m-a}{r-a}^2(r-a)!a!,&0\le a\le r,\\[2mm]
   0,&a>r,
   \end{cases}
   \tag{0.3}
   \]

   for two owners at Johnson distance `a`.  Equivalently,

   \[
   {\lambda_a\over D_{m,r}}
   ={\binom ra\over\binom ma^2}.
   \tag{0.4}
   \]

   If `r=o(m)`, then the maximum nontrivial codegree is

   \[
   \Delta_2=\lambda_1={r\over m^2}D_{m,r}.
   \tag{0.5}
   \]

2. Near-perfect **owner** packing needs no nibble.  In one fixed perfect
   matching frame, status cells with at least `r` split pairs can be
   partitioned into `Q_r` packets.  For `r=o(m)` this covers

   \[
   (1-e^{-\Omega(m)})\binom{2m}m
   \tag{0.6}
   \]

   owners.

3. Choosing owner-disjoint packets from incompatible frames is genuinely
   outside the `U_kappa` whole-component model.  That model changes a
   frame only on a complete common-support component.  A packet matching
   may instead take one cell from one frame, a disjoint cell from a second
   frame, and quarantine the leave.  When the two completed frames have
   connected union, such a mixed partial selection is forbidden by the
   `U_kappa` theorem but is legal in `H_(m,r)`.  The escape is therefore
   real, although it depends essentially on allowing a near-factor and an
   `o(W)` completion.

4. The exact positive successor is a **colored packet matching** theorem.
   For a power-of-two `r`, the verified nonlinear cube compiler gives in
   every packet `2^r` distinct literal lower targets and `2^r` distinct
   literal upper targets, simultaneously for every `q<=r/2`.  The full
   coordinate orbit has an exact fractional matching saturating owners
   and, after certification thinning by `N_q/W`, every target part.  The
   open step is to find one integral owner-disjoint packet family that
   nearly saturates all those target parts simultaneously.

The usual fixed-uniformity nibble cannot be cited for this step.  Here the
owner-edge size is `2^r`, and for `log m << r=o(m)` a Bernoulli residual of
any fixed density contains no packet with high probability:

\[
 |E(H_{m,r})|z^{2^r}=o(1)\qquad(0<z<1\text{ fixed}).
 \tag{0.7}
\]

This does not disprove a structured packet matching--(0.6) is the direct
counterexample--but it shows that a random-like residual nibble stalls
after deleting only an `o(1)` fraction of the owners.  No elementary
growing-uniformity estimate checked here proves the colored theorem.

## 1. Exact degree and edge count

Fix an owner `S in V_m`.  To choose a packet containing `S`, first choose

\[
                         F\subseteq S,
             \qquad |F|=m-r.                            \tag{1.1}
\]

The `r` elements of `S\F` are the endpoints selected by `S`.  Choose `r`
distinct partners from `S^c` and biject them to `S\F`.  Therefore

\[
 \deg(S)=\binom mr\binom mr r!=\binom mr^2r!=D_{m,r}.  \tag{1.2}
\]

The packet parametrization is faithful: the intersection of all packet
owners is `F`, and the `r` cube directions recover the pairs in `M`.
Hence one may also count edges directly:

\[
\begin{aligned}
 |E(H_{m,r})|
 &=\binom{2m}{m-r}\binom{m+r}{2r}{(2r)!\over2^rr!}\\
 &={ (2m)!\over2^rr!(m-r)!^2}.
\end{aligned}                                             \tag{1.3}
\]

Double counting owner-edge incidences gives the consistency identity

\[
 |E(H_{m,r})|2^r=\binom{2m}mD_{m,r}.                   \tag{1.4}
\]

In particular the uniform weight `1/D_(m,r)` on every packet is an exact
fractional perfect matching of the owner hypergraph, of total weight

\[
                         {1\over2^r}\binom{2m}m.        \tag{1.5}
\]

## 2. Exact pair-codegrees

Let `S,T in V_m`, and put

\[
 a=|S\setminus T|=|T\setminus S|=m-|S\cap T|.          \tag{2.1}
\]

If both owners belong to one packet, they disagree on exactly `a` active
pairs, so necessarily `a<=r`.

Assume `a<=r`.  The core must be an `(m-r)`-subset of `S cap T`; there are

\[
              \binom{m-a}{m-r}=\binom{m-a}{r-a}        \tag{2.2}
\]

choices.  The `a` elements of `S\T` must be paired bijectively with the
`a` elements of `T\S`, contributing `a!`.  The remaining `r-a` common
selected elements are `(S cap T)\F`.  Each must be paired with a distinct
element outside `S union T`, a set of size `m-a`; this contributes

\[
                         (m-a)_{r-a}.                   \tag{2.3}
\]

Thus

\[
 \lambda_a
 =\binom{m-a}{r-a}(m-a)_{r-a}a!
 =\binom{m-a}{r-a}^2(r-a)!a!,                          \tag{2.4}
\]

which proves (0.3).  Dividing by (1.2) gives

\[
 {\lambda_a\over D_{m,r}}
 =\left({(r)_a\over(m)_a}\right)^2{1\over\binom ra}
 ={\binom ra\over\binom ma^2}.                        \tag{2.5}
\]

Write `R_a=lambda_a/D_(m,r)`.  Then

\[
 {R_{a+1}\over R_a}
 ={(r-a)(a+1)\over(m-a)^2}.                            \tag{2.6}
\]

If `r=o(m)`, the right side is at most

\[
                         {r^2\over(m-r)^2}=o(1)         \tag{2.7}
\]

uniformly for `a<r`.  Hence the nontrivial codegrees decrease with
Johnson distance and

\[
 \Delta_2=\lambda_1
 =\binom{m-1}{r-1}^2(r-1)!
 ={r\over m^2}D_{m,r}.                                 \tag{2.8}
\]

The restriction `r=o(m)` matters.  At `r=m`, complementary owners have
codegree equal to the full degree, as (2.5) correctly records.

## 3. A deterministic near-perfect owner packing

Fix one perfect matching

\[
                    \widehat M=\{e_1,\ldots,e_m\}      \tag{3.1}
\]

of `[2m]`.  Its status cells partition `V_m`.  A cell with `s` split
pairs is a physical `Q_s`.  If `s>=r`, choose deterministically `r` of
its split axes and fix the orientations of the other `s-r` axes.  This
partitions the cell into physical `Q_r` packets belonging to `H_(m,r)`.

The only uncovered owners lie in cells with fewer than `r` split pairs.
The exact number of middle owners with `s` split pairs is

\[
 A_s=
 \begin{cases}
 \displaystyle
 \binom ms2^s\binom{m-s}{(m-s)/2},&s\equiv m\pmod2,\\[2mm]
 0,&s\not\equiv m\pmod2.
 \end{cases}                                           \tag{3.2}
\]

Indeed, after choosing and orienting the split pairs, exactly half of the
remaining pairs must be full and half empty.

For `r=o(m)`, use

\[
 \binom{m-s}{(m-s)/2}\le2^{m-s}                       \tag{3.3}
\]

to obtain

\[
 \sum_{s<r}A_s
 \le2^m\sum_{s<r}\binom ms
 =2^{m+o(m)}.                                          \tag{3.4}
\]

Since

\[
 \binom{2m}m=2^{2m-o(m)},                              \tag{3.5}
\]

the uncovered proportion is `2^{-m+o(m)}`.  This proves (0.6).

This construction is useful diagnostically.  It proves that large packet
rank is not by itself an owner-packing obstruction.  It is useless for
the target problem because all packets inherit one fixed global frame,
and therefore retain the fixed-frame Gaussian cut.

## 4. Why packetwise frame mixing is outside the `U_kappa` model

Suppose `m-r` is even.  Then every packet `P(F,M)` is one status cell of
some completed perfect matching: pair the elements of `F` internally,
pair the unused set

\[
 B=[2m]\setminus\left(F\cup\bigcup M\right)            \tag{4.1}
\]

internally, declare the `F`-pairs full, the `B`-pairs empty, and the
`M`-pairs split.  Thus the distinction is not at the level of one packet.
It is at the level of what may be selected simultaneously.

The `U_kappa` recoupling theorem starts with complete status-cell
partitions.  If an atlas of completed frames has connected coordinate
union, its owner-overlap graph has one component, so an integral atlas
option chooses one global frame on the entire middle layer.

The packet hypergraph imposes only

\[
                         P_i\cap P_j=\varnothing.       \tag{4.2}
\]

It does not require the unused cells of either frame to be selected.  To
see the strict difference explicitly, cyclically label the coordinates
`x_0,...,x_(2m-1)` and take

\[
 \widehat M_0=\{x_{2i}x_{2i+1}:0\le i<m\},
 \qquad
 \widehat M_1=\{x_{2i+1}x_{2i+2}:0\le i<m\},           \tag{4.3}
\]

with indices modulo `2m`.  Their union is one alternating `2m`-cycle.
Make `x_0x_1` full in an `M_0`-cell.  Make the two `M_1`-edges incident
with `x_0,x_1` empty in an `M_1`-cell.  Choose, among the remaining
edges, `r` split edges in each cell, including one `M_0`-edge and one
`M_1`-edge sharing a coordinate.  Complete the remaining statuses with
`(m-r)/2` full and `(m-r)/2` empty edges in each frame.  This is possible
for `m-r>=4` (and, harmlessly, after increasing `m` if one prescribed
active edge meets a prescribed status edge).

The resulting two status cells have the following properties:

* they are disjoint, because every owner of the first contains both
  `x_0,x_1`, whereas every owner of the second avoids both; and
* their active pair sets contain incompatible pairs, so no single perfect
  matching contains both local frames.

The two cells are legal disjoint edges of `H_(m,r)`.  They cannot arise
from a `U_kappa` selector: the atlas union is connected and therefore has
only one `U_kappa`, while the two selected cells use different frames.

This does **not** contradict the exact component theorem.  The unused
owners have not yet been repartitioned.  The escape is the permission to
build a near-factor from isolated cells and quarantine an `o(W)` leave.
If one insists on an exact completion using only the two original full
cell partitions, the whole-component obstruction returns.

Thus an owner-disjoint packet theorem is a genuine successor architecture,
not a rounding theorem inside the false status-cell column model.

## 5. Local trace colors

Assume now that `r` is a power of two.  The recursive nonlinear factor of
`MATH_THEOREM_TENSOR_PACKET_CONSECUTIVE_WINDOW_DESIGN_20260726.md`
decomposes every physical `Q_r` packet into isometric `C_(2r)` cycles.
One common factor has injective forward and backward literal traces for
every

\[
                         1\le q\le r/2.                \tag{5.1}
\]

Consequently every compiler-labelled packet option `e` has literal target
sets

\[
 \mathcal T_{e,q}^-\subseteq\binom{[2m]}{m-q},
 \qquad
 \mathcal T_{e,q}^+\subseteq\binom{[2m]}{m+q},          \tag{5.2}
\]

with

\[
                 |\mathcal T_{e,q}^-|
                 =|\mathcal T_{e,q}^+|=2^r.            \tag{5.3}
\]

The same packet factor defines all the sets in (5.2); there is no
independent choice by depth.  Distinctness is only internal to one packet.
Two packets may produce the same labelled target, and controlling those
cross-packet collisions is the remaining problem.

This naturally makes `H_(m,r)` a set-colored hypergraph:

* the hard vertices are middle owners;
* the colors in part `(q,+/-)` are the actual rank-`m+/-q` targets;
* an option edge has owner support `P_e` and color set
  `T_(e,q)^(+/-)`.

## 6. The colored packet-matching theorem

The following is the exact positive successor.  It is an open existence
statement, not a consequence of the degree calculation.

### `CPM` -- simultaneous colored packet matching (open)

There exist powers of two `r_m`, heights `H_m`, and compiler-labelled
packet options `e` in `H_(m,r_m)` such that

\[
 {H_m\over\sqrt m}\longrightarrow\infty,
 \qquad {H_m\over r_m}\longrightarrow0,
 \qquad r_m=o(m),                                      \tag{6.1}
\]

and there is a family `M_m` of options satisfying

1. the owner supports `P_e`, `e in M_m`, are pairwise disjoint;
2. the owner leave is small:
   \[
   \binom{2m}m-\left|\bigcup_{e\in M_m}P_e\right|=o(W);
   \tag{6.2}
   \]
3. the same selected options cover almost every target simultaneously:
   \[
   \sum_{q=1}^{H_m}\sum_{\epsilon\in\{-,+\}}
   \left[
    \binom{2m}{m+\epsilon q}
    -\left|\bigcup_{e\in M_m}\mathcal T_{e,q}^{\epsilon}\right|
   \right]
   =o(W).                                               \tag{6.3}
   \]

Here `m+(-)q` means `m-q`.  The packet compiler and its cycle factor are
part of an option, so one cannot change them independently in (6.3).

### Theorem 6.1 (`CPM` implies coefficient one)

Assume `CPM`.  Then the constant-one upper bound holds.

#### Proof

The compiler partitions every selected packet into isometric `C_(2r_m)`
middle cycles.  Such a cycle is a cyclic `r_m`-strip: its direction word
is a permutation of the `r_m` active coordinate pairs repeated twice, so
its owners have the form

\[
                         K\cup I_z(t,r_m).              \tag{6.4}
\]

The selected packets are owner-disjoint, hence all these strips are
owner-disjoint.  Put every uncovered middle owner into the singleton
remainder.  By (6.2) its size is `o(W)`.

Every target certified in (5.2) is a literal consecutive-window target
of one selected strip.  Therefore (6.3) is exactly the aggregate central
hole bound required by `EMSF`.  Conditions (6.1) give

\[
 H_m/\sqrt m\to\infty,
 \qquad H_m/r_m\to0,                                   \tag{6.5}
\]

and every main strip has half-length `r_m`.  Thus all hypotheses of
`EMSF` hold.  The exact successor reduction in
`MATH_SYNTHESIS_OUTER_INTEGRAL_GAP_AND_EXTERIOR_MOVING_SUCCESSOR_20260726.md`
gives

\[
                         \nu(2m)=(1+o(1))W.             \tag{6.6}
\]

The standard odd lift and Sperner lower bound finish coefficient one.
\(\square\)

## 7. Ordinary augmented-hypergraph form and its exact fractional point

There is a stronger ordinary matching formulation of `CPM`.  For each
option `e` and every `q,epsilon`, choose a certified subset

\[
                 \Gamma_{e,q}^{\epsilon}
                 \subseteq\mathcal T_{e,q}^{\epsilon}. \tag{7.1}
\]

Make one augmented hyperedge

\[
 \widehat e=P_e\ \dot\cup\!
 \bigdotcup_{q\le H,\epsilon}
 \Gamma_{e,q}^{\epsilon}                               \tag{7.2}
\]

on the disjoint union of the owner part and all signed target parts.
An ordinary matching of augmented edges is owner-disjoint and never
certifies one target twice.  If it leaves `o(W)` vertices in aggregate
over all these parts, then the underlying options satisfy `CPM`.

The augmented catalogue has an exact simultaneous fractional perfect
matching.  Indeed, include the full coordinate orbit of every packet
compiler.  Give raw options total weight `1/D_(m,r)` per underlying packet
(divided equally among compiler labels, if several are retained).  This
saturates every owner by (1.2).

More explicitly, if the invariant catalogue has `L` compiler labels per
raw packet, its owner degree is

\[
                         D^*=LD_{m,r}.                  \tag{7.3}
\]

Coordinate transitivity and (5.3) give the exact unthinned target degree

\[
                         D_{q,\mathrm{tr}}^*
                         ={W\over N_q}D^*              \tag{7.4}
\]

in each signed target part.  Thus the degree imbalance is precisely the
forced average multiplicity `lambda_q`, not an uncontrolled error.

At signed depth `q`, the total raw trace load of a target is uniform by
coordinate transitivity.  The total trace occurrence mass under the
fractional owner cover is `W`, whereas the target part has size

\[
                         N_q=\binom{2m}{m-q}
                             =\binom{2m}{m+q}.          \tag{7.5}
\]

Hence every target has raw fractional trace load

\[
                         \lambda_q={W\over N_q}.        \tag{7.6}
\]

For each trace occurrence, certify it with marginal probability

\[
                         p_q={N_q\over W}=\lambda_q^{-1}.\tag{7.7}
\]

This is represented exactly as a fractional mixture over the subset
states (7.1), independently across signed depths.  Owner marginals remain
one, while every target marginal becomes `p_q lambda_q=1`.

Thus the remaining assertion can be stated sharply:

> round this explicit symmetric fractional perfect matching in the
> packet-option augmented hypergraph to an integral matching with total
> owner-plus-target leave `o(W)`.

Unlike the false status-cell rounding theorem, the columns here are
individual owner packets from mutually incompatible frames, and an
`o(W)` owner leave is allowed.  No theorem in the current record refutes
this packet rounding assertion.

The exact raw owner codegrees (2.4) do not prove it.  Mixed
owner-target and target-target codegrees depend on the compiler-labelled
trace geometry and remain unbounded by the present calculation.

## 8. Growing-uniformity nibble audit

At first sight (2.8) looks ideal:

\[
                         {\Delta_2\over D}={r\over m^2}=o(1).
                                                               \tag{8.1}
\]

This is the hypothesis used by fixed-rank near-perfect matching theorems
when the edge size is fixed.  Here the edge size is

\[
                         k=2^r,                                \tag{8.2}
\]

and the dependence on `k` cannot be suppressed.  Already

\[
                         k{\Delta_2\over D}
                         ={2^rr\over m^2}\to\infty             \tag{8.3}
\]

when `log m << r`.  Thus the elementary union bound over the vertices of
one selected edge gives no useful error.

There is a stronger first-moment diagnosis.  Let `R_z` be a Bernoulli
`z`-subset of the owner set.  A fixed packet survives inside `R_z` with
probability `z^(2^r)`, so

\[
 \mathbb E\,e(H_{m,r}[R_z])=|E(H_{m,r})|z^{2^r}.       \tag{8.4}
\]

Using

\[
 D_{m,r}=\binom mr^2r!
 \le\left({e^2m^2\over r}\right)^r                  \tag{8.5}
\]

and (1.4),

\[
                         \log|E(H_{m,r})|
                         =O(m+r\log m).                \tag{8.6}
\]

If `r/log m -> infinity`, then

\[
                         2^r\gg m+r\log m.             \tag{8.7}
\]

For every fixed `z<1`, equations (8.4)--(8.7) give

\[
 \mathbb E\,e(H_{m,r}[R_z])
 \le\exp\{O(m+r\log m)-|\log z|2^r\}=o(1).            \tag{8.8}
\]

By Markov's inequality, a random residual of density `z` contains no
packet with high probability.  More quantitatively, a random-like process
stalls after deleting a fraction on the order of

\[
                         {\log|E(H_{m,r})|\over2^r}=o(1)\tag{8.9}
\]

of the owners.

This is not an impossibility theorem for packet matchings.  Section 3
constructs an exponentially good near-perfect owner matching whose
residual is highly structured.  It is instead an exact warning about
method: a standard nibble whose differential-equation trajectory treats
the residual owner set as quasirandom cannot reach any fixed positive
coverage, let alone a near-factor.

The augmented edge rank is larger still--typically of order

\[
                         (1+2H)2^r,                    \tag{8.10}
\]

before certification thinning.  Moreover its mixed codegrees are not
controlled by (8.1).  Therefore no fixed-uniformity Pippenger--Spencer or
Rödl-nibble statement may be inserted as a black box in the regime
`log m << r=o(m)`.  A valid proof must exploit a structured owner tiling,
an algebraic packet decomposition, or a new growing-rank theorem with
explicit dependence strong enough to survive (8.7).

## 9. Exact frontier

The following points are proved.

1. The raw packet hypergraph has the exact incidence parameters
   (0.2)--(0.5).
2. It has an explicit owner near-factor for every `r=o(m)`.
3. Packetwise mixing of incompatible frames is strictly outside the
   connected `U_kappa` whole-component model.
4. The verified nonlinear local compiler converts a colored packet
   matching into literal simultaneous central target coverage.
5. `CPM` implies `EMSF`, hence coefficient one.
6. The full symmetric augmented catalogue has an exact simultaneous
   fractional perfect matching.
7. A random-like nibble is quantitatively incompatible with
   `log m << r`.

What is not proved is `CPM`, or equivalently the near-perfect integral
matching statement for the augmented packet catalogue.  The next useful
mathematical question is not another owner-degree computation.  It is an
outer construction that keeps the deterministic near-tiling geometry of
Section 3 while changing frames often enough that the local injective
trace sets have only `o(W)` aggregate cross-packet collisions.
