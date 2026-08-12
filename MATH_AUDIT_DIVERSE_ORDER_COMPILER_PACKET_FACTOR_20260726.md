# Audit of the diverse-order compiler packet factor

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Verdict

The main packet-local theorem in
`MATH_THEOREM_DIVERSE_ORDER_COMPILER_PACKET_FACTOR_20260726.md` is
correct.  For every (H\to\infty) with (H=o(m)), the stated choice of
(R) gives

\[
                         H=o(R),\qquad R=o(m),
\]

the rank-twisted product-cell construction leaves (o(W/H)) middle
owners, and the parity-complete compiler applies literally to every
retained physical (Q_R)-fibre.  At every sign and every
(1\le q\le H), its target map is injective on the entire packet, not
merely on each compiler cycle.  There is consequently no hidden
within-cycle, cross-cycle, or cycle-closure repeat.

The exact component count and the cross-packet repeat identity are also
correct:

\[
                M={G\over2R}=o(W/H),\qquad
                M_q^\pm=N_q-G+\mathcal R_{q,\mathrm{cross}}^\pm.
\]

There are two qualifications.

1. The compiler supplies a canonical forward orientation (and,
   separately, a canonical reverse orientation) on all of its cycles.
   The cited theorem proves injectivity for either global orientation.
   It does not state cross-orientation injectivity for an arbitrary
   cycle-by-cycle mixture.  The present construction needs no such
   mixture: orient every installed compiler component canonically.
2. The estimate (M=o(W/H)) proves that an interface theorem charging
   (O(H)) per component would cost (o(W)).  It does not itself
   construct a joining or quarantine operation with that cost.  Thus
   Outcome 3 should be read conditionally, exactly as Section 4 later
   phrases it.  If it is intended as an unconditional transfer theorem,
   an external (O(H))-per-component interface lemma must be cited.

One strengthening is available for free.  Distinct parallel (Q_R)
fibres cut from the same parent product cell have disjoint literal trace
images at every protected depth.  Their different frozen spectator
orientations survive in every lower and upper target.  Hence all possible
cross-packet collisions already occur between different parent product
cells, not between sibling fibres of one cell.

Subject to the two scope qualifications above, the advertised reduction
is valid.  It removes the common-order syndrome and reduces the remaining
coefficient-one problem to the cross-parent-cell grouped
Hall/covariance estimate.

## 1. Scale audit

Let (n=4\cdot2^t) be least with (n\ge\sqrt{mH}), and put (R=2n).
Successive admissible values differ by a factor two, so

\[
              \sqrt{mH}\le n<2\sqrt{mH}.
\]

It follows that

\[
 {R\over H}\ge2\sqrt{m/H}\longrightarrow\infty,
 \qquad
 {R\over m}<4\sqrt{H/m}\longrightarrow0.
\]

Moreover

\[
 {H\over n}\le\sqrt{H/m}\longrightarrow0,
\]

so eventually (H\le n/2-1=R/4-1).  These are exactly the scale
hypotheses needed by the compiler and the owner tiling.  No stronger
restriction such as (H=o(m^{1/3})) is hidden here.

## 2. Applicability of the parity-complete compiler

The cited compiler theorem is parametrized by a coarse dimension
(n=4\cdot2^t).  Its paired-order lift factors

\[
                         Q_{2n}=Q_R
\]

into isometric (C_{4n}=C_{2R})'s.  Corollary 4.2 of
`MATH_ATTACK_S_PARITY_COMPLETE_MAPPING_TRACE_ENTROPY_CUT_20260726.md`
proves literal lower and upper trace injectivity, through physical length
(n/2-1), on the full paired-order domain.  The statement includes both
physical start phases and includes starts whose intervals cross the
closure of a compiler cycle.

Every retained rank-twisted packet is a genuine coordinate-disjoint
Johnson cube.  Its (R) axes are disjoint ground-coordinate pairs, and a
move exchanges the two endpoints of exactly one such pair.  Therefore an
arbitrary bijection between these axes and the compiler's (R) physical
directions is a literal physical cube conjugacy of the type required by
Corollary 4.2.  The fact that the axes came from different local ranks or
macroblocks is irrelevant after the product cell has been fixed.

The exterior of the (Q_R)-fibre also causes no ambiguity.  Fixed
zero-status pairs contribute no endpoints to either target, fixed
two-status pairs contribute both, and every frozen split-pair spectator
contributes its one fixed endpoint.  These are fixed literal decorations
of the compiler target, so they preserve injectivity.

Consequently, for either canonical orientation and either sign, the
packet image contains exactly

\[
                              2^R
\]

targets at every (1\le q\le H).

### Orientation scope

The source theorem proves that the forward map is injective on its full
domain and that the reverse map is injective on its full domain.  This is
enough: use the inherited forward orientation on every component, or use
the inherited reverse orientation on every component.  What is not
explicitly proved is that the union of a forward image from one cycle and
a reverse image from another cycle is injective.  Hence independent
component reversals should not be inserted without an additional
cross-orientation lemma.

## 3. Owner leave

The rank-twisted macroblock theorem applies with logarithmic block size
(d\to\infty) and (R=o(m)).  For a fixed local-rank vector, the number
of flexible split pairs has law

\[
                         S\sim\operatorname{Bin}(m+O(d),1/2)
\]

under the unconditioned subset count.  Thus

\[
                         \Pr(S<R)=2^{-m+o(m)}.
\]

There are only

\[
 (2d+1)^{m/d}=
 \exp\!\left(O\!\left({m\log d\over d}\right)\right)=2^{o(m)}
\]

rank vectors, and the residual coordinate factor is also (2^{o(m)}).
The number of rank-(m) owners in low-dimensional cells is therefore at
most

\[
                              L\le2^{m+o(m)}.
\]

Since

\[
 W=\binom{2m}{m}=2^{2m-o(m)},\qquad H\le m
\]

eventually, (L=o(W/H)).  Every retained (Q_S), (S\ge R), is
partitioned exactly into parallel (Q_R)'s.  Hence

\[
                              G=W-L=W-o(W/H)
\]

with no fractional or completion leave inside a retained cell.

## 4. Spectator-fibre separation

Fix one parent (Q_S), choose its common set (A) of (R) compiler
axes, and let (B) be the (S-R) frozen spectator axes.  A parallel
fibre is specified by one orientation (y_b\in\{0,1\}) for every
(b\in B).

For a compiler window with varied direction set (J\subseteq A), the
literal lower target contains

* neither endpoint of every axis in (J);
* exactly the current endpoint of every axis in (A\setminus J); and
* exactly the frozen endpoint (y_b) of every (b\in B).

The upper target contains both endpoints on (J), one current endpoint
on (A\setminus J), and again the one frozen endpoint on every
(b\in B).  Thus if two sibling fibres differ at a spectator (b), all
of their lower targets differ at (b), and all of their upper targets
differ at (b).  Therefore

\[
 I_{P,q}^\pm\cap I_{P',q}^\pm=\varnothing
\]

for distinct parallel fibres (P,P') of the same parent cell.

This argument uses the order of construction in the source note: choose
the (R) axes once for the parent (Q_S), then freeze every orientation
of the complement.  If one instead allowed the selected axes to depend on
the fibre, the conclusion would require a new check.

Different parent product cells can collide.  For example, a pair frozen
at zero status in one cell and used as a varied direction in another can
look identical in a lower target.  Such collisions are precisely part of
the stated cross-packet residual.

## 5. No hidden compiler repeat

There are three possible places a repeat could have been hidden.

1. **Inside one cycle.**  Corollary 4.2 is an injectivity theorem on all
   starts, so this is excluded.
2. **Between two compiler cycles in one packet.**  The corollary comes
   from the joint code on the full paired-order domain, not from separate
   per-cycle arguments.  It therefore excludes this as well.
3. **Across the cyclic closure.**  The trajectories are trajectories of
   the cyclic neighbour permutations.  Starts near the end of a written
   direction word are part of the same full domain, so closure-crossing
   windows are included.

Thus the within-packet repeat count really is zero.  No (Q_8)-style
turnaround or seam term is being silently omitted from the packet-local
trace ledger.

## 6. Support-count comparison

For a common-order factor, a fixed (q)-support leaves (R-q) split
orientations visible, so it gives at most (2^{R-q}) literal targets.
There are at most (R) cyclic (q)-supports.  Hence its image has size at
most

\[
                             R2^{R-q}.
\]

By contrast the compiler image has size (2^R).  Since one support can
still give at most (2^{R-q}) targets, the compiler necessarily uses at
least (2^q) supports.  This verifies the claimed sharp escape from the
common-order syndrome at the packet scale.

## 7. Component count and interface qualification

Every compiler component has (2R) owners.  Therefore

\[
                          M={G\over2R}.
\]

There is no divisibility gap: (R=2n=2^{t+3}), so (2R\mid2^R), and
each packet is exactly factored.  Moreover

\[
 {M\over W/H}\le {H\over2R}\longrightarrow0.
\]

This proves the component-count condition exactly.

What it implies about an eventual linear word depends on the interface
lemma used.  If a collar, bridge, or quarantine construction costs
(O(H)) entries per component across the whole protected band, then its
total cost is

\[
                              O(HM)=o(W).
\]

The packet theorem itself does not exhibit that construction.  A naive
cut that simply discards every closure-crossing window would lose
(q-1) occurrences at depth (q), or (Theta(H^2)) per component after
summing all depths.  Thus the (O(H)) interface hypothesis is substantive
and should be cited rather than inferred solely from (M=o(W/H)).

This does not affect the packet-local factor or trace theorem; it only
qualifies Outcome 3 and any later transfer to one linear array.

## 8. Exact cross-packet ledger

For fixed (q) and sign, let

\[
 a_T=\#\{P:T\in I_{P,q}^\pm\}.
\]

Packet injectivity gives

\[
 \sum_Ta_T=\sum_P|I_{P,q}^\pm|=G.
\]

If (U=\{T:a_T>0\}), then

\[
 \mathcal R_{q,\mathrm{cross}}^\pm
   =\sum_T(a_T-1)_+
   =G-|U|.
\]

The number of missing targets is (N_q-|U|), whence

\[
 \boxed{
 M_q^\pm=N_q-G+\mathcal R_{q,\mathrm{cross}}^\pm.}
\]

This identity is algebraic and does not need (G\ge N_q).  In the
present construction the exponentially small leave in fact gives
(G>N_q) for every (q\ge1) eventually, so (G-N_q) is the genuine
forced repeat quota.  Summing the boxed identity proves the equivalence
with (5.5).

By Section 4 above, the repeat count can be sharpened to pairs of packets
coming from different parent product cells.  No owner, spectator,
within-packet, cross-cycle, or closure term remains hidden in it.

## 9. Audited boundary

Proved:

* the scale (H\ll R\ll m);
* the (o(W/H)) owner leave;
* exact (Q_R\)-to-(C_{2R}) factoring in every retained fibre;
* literal two-sign injectivity through every (1\le q\le H), using a
  canonical global compiler orientation;
* zero within-packet and sibling-fibre repeats;
* (M=G/(2R)=o(W/H)); and
* the exact cross-packet missing/repeat identity.

Not proved by this theorem:

* arbitrary componentwise mixing of forward and reverse orientations;
* an (O(H))-per-component joining/quarantine interface;
* the cross-parent-cell covariance/Hall estimate; or
* coefficient one.

The first two are scope/interface qualifications.  The third is the real
remaining combinatorial gate.
