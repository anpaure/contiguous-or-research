# Typed suffix candidate lists: Haxell/LLL private-router specialization

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sufficient theorem.  The
independent-transversal selector is standard and was already recorded for
whole buffered packets: Haxell gives the sharper primary sufficient constant
`L>=2 Delta`, while a self-contained symmetric-LLL proof gives the weaker
`L>=2e Delta`.  The content specialized here is the translation from a
literal conflict-free transversal to full typed suffix rank and its exact
composition with the regular incidence factor.  This file does **not**
assert that the current parent construction supplies the required literal
typed candidate lists.

Fix one materialized cap, guard, phase, and occurrence state.  Delete the
physical capacities used by one fixed compensation linkage and every
interior vertex of the selected claim-to-port prefixes, including every
claim start; retain only their terminal ports.  Let

\[
                         P=\{p_1,\ldots,p_M\},\qquad M\ge1,
\]

be the active physical occurrence-labelled ports in the resulting
node-split unit-capacity directed network.

The typed-rank notation below presupposes that terminal legality has been
materialized in one fixed typed suffix network: either the ports lie in
type-homogeneous blocks, or a separately proved type/identity gadget routes
every physical port copy through its common capacity-one gate.  If legality
is retained only as an external incidence predicate, the theorem still
produces the displayed explicit legal linkage, but it should not be
rephrased as independence in an ordinary untyped strict gammoid.

For each port `p_i`, let `C_i` be a finite nonempty family of literal
directed paths

\[
                         R:p_i\leadsto t(R)
\]

to unused sinks.  Every terminal type in `C_i` is required to be legal for
every gain incident with `p_i`.  Two candidates conflict if they share any
residual physical unit-capacity resource (represented, after node splitting,
by a capacity vertex) or have the same sink occurrence.  Thus every physical
suffix--suffix obstruction, not merely equality of their Boolean values, is
an edge of the conflict graph.  Candidates from the same list need not be
compared, because exactly one candidate is to be chosen from each list.

Let `H` be the multipartite conflict graph on the disjoint union of the
candidate lists: its parts are the `C_i`, and its edges are precisely the
cross-list conflicts.  Put

\[
 L=\min_i |C_i|,
 \qquad
 \Delta=\max_{R\in V(H)} d_H(R).
\tag{0.1}
\]

The graph model is exact only for a fixed literal path atlas.  Any global
acceptance condition not represented by the residual network capacities,
typed/identity gadget, or the pairwise sink-occurrence constraint must be
materialized before `H` is formed; a genuinely higher-order obstruction is
not certified by pairwise nonconflict.

## Theorem 1 (Haxell suffix transversal; primary)

If `Delta=0`, a conflict-free transversal exists trivially.  If

\[
                         \boxed{L\ge 2\Delta,}
\tag{1.1-H}
\]

then there are candidates

\[
                         R_i\in C_i\qquad(1\le i\le M)
\]

which are pairwise vertex-disjoint and end at distinct typed sink
occurrences.  Consequently the complete active port set has full typed
suffix rank,

\[
                         r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|.
\tag{1.2}
\]

### Proof

The multipartite conflict graph `H` has maximum degree `Delta`, and every
part has size at least `2 Delta`.  Haxell's independent-transversal theorem
therefore supplies one vertex from every part with no conflict edge.  By the
literal definition of `H`, the selected paths share no residual physical
capacity and have distinct sink occurrences.  They are a simultaneous typed
linkage of the full port set, which is exactly (1.2).  \(\square\)

## Theorem 1' (self-contained local-lemma fallback)

If `Delta=0`, a conflict-free transversal exists trivially.  If

\[
                         \boxed{L\ge 2e\Delta,}
\tag{1.1-L}
\]

then there are candidates

\[
                         R_i\in C_i\qquad(1\le i\le M)
\]

which are pairwise vertex-disjoint and end at distinct typed sinks.
Consequently the complete active port set has full typed suffix rank,

\[
                         r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|.
\]

### Proof

If a list has more than `L` members, discard arbitrary surplus candidates.
This cannot create a conflict, so it is enough to treat the case

\[
                         |C_i|=L\quad\hbox{for every }i.
\]

Choose one member of every `C_i` independently and uniformly.  For every
edge `xy` of `H`, with `x` and `y` in distinct lists, let `A_xy` be the bad
event that both endpoints are selected.  Then

\[
                         \Pr(A_{xy})={1\over L^2}.
\tag{1.3}
\]

The event `A_xy` depends only on the two list variables containing `x` and
`y`.  It is therefore independent of every bad event whose endpoints lie
in two other lists.  A fixed list contains `L` candidates, each incident
with at most `Delta` conflict edges.  Hence at most `L Delta` bad events use
that list.  It follows that each `A_xy` is dependent on at most

\[
                         D\le 2L\Delta-2
\tag{1.4}
\]

other bad events.  By (1.1-L),

\[
 e\Pr(A_{xy})(D+1)
 \le {e\over L^2}(2L\Delta-1)
 < {2e\Delta\over L}
 \le1.
\tag{1.5}
\]

The symmetric Lovasz local lemma therefore gives a choice for which no
bad event occurs.  This is one candidate from every list with no shared
physical capacity and no repeated sink occurrence.  The candidates form a
simultaneous typed linkage of all active ports, proving (1.2).  \(\square\)

## 2. Composition with the regular incidence factor

Let `B=(G,P;E)` be a left-`h`-regular/right-at-most-`h` literal incidence
factor in the same materialized state, with `P=N_B(G)`.  Assume every
incidence `gp` has a literal directed claim-to-port prefix in the network
remaining after deletion of the fixed compensation linkage.  Require the
full privacy hypotheses of the regular-factor theorem: distinct prefixes
share no physical capacity except that the `h` prefixes of one gain may
share that gain's claim start and the prefixes ending at one port may share
that common terminal port; a prefix meets no selected suffix except at its
own terminal port.  Assume the lists above were formed only after deleting
the fixed compensation linkage and every prefix vertex other than its
terminal port.  In particular, the prefixes themselves, every candidate
suffix, and the fixed linkage are mutually compatible in one fixed physical
state, subject only to those explicitly priced claim-start and port
capacities.

### Theorem 2 (independent-transversal factor-router composition)

Under the primary Haxell condition (1.1-H), or under the fallback LLL
condition (1.1-L), every gain in `G` has a path to a distinct legal sink,
and all these gain paths coexist with the fixed compensation linkage.

### Proof

Theorem 1, or Theorem 1' under its fallback hypothesis, gives one
simultaneous private suffix from every active port.
Work in the subnetwork consisting of the displayed prefixes and these
selected suffixes, with unit arcs from a super-source to the distinct claim
starts and unit arcs from the distinct selected sinks to a super-sink.  Send
`1/h` units along every displayed incidence prefix followed by its port
suffix.  Each gain emits one unit, because its factor degree is `h`.
Every port and suffix carries at most

\[
                         {\deg_B(p)\over h}\le1,
\]

and prefix privacy accounts for every other capacity: a claim start has
load one and a private prefix interior has load `1/h`.  This is a feasible
value-`|G|` fractional flow in an integral node-split network disjoint from
the fixed compensation linkage.  Integral max flow supplies one disjoint
path from every gain to a distinct sink.  It is legal despite the
single-commodity rounding because every selected suffix at `p` has a type
accepted by every gain incident with `p`.  \(\square\)

## 3. Quantitative consequence for buffered packet catalogues

Let `n` denote the central-layer scale parameter, distinct from the number
`M=|P|` of active ports, and let `d=d(n)` be the residence/deadline scale.
Suppose a family of fully typed literal suffix catalogues has

\[
                         |C_i|\ge \alpha n^2
\tag{3.1}
\]

at every active port, while every particular candidate conflicts, across
all other lists combined, with at most

\[
                         \beta n d(n)
\tag{3.2}
\]

candidates.  Then the primary Haxell theorem applies whenever

\[
                         {n\over d(n)}\ge {2\beta\over\alpha}.
\tag{3.3-H}
\]

The self-contained LLL fallback applies under the slightly stronger row

\[
                         {n\over d(n)}\ge {2e\beta\over\alpha}.
\tag{3.3-L}
\]

In the intended central-layer regime `d(n)=Theta(sqrt(n))`, the left side of
(3.3-H) and (3.3-L) tends to infinity.  Thus the list-versus-conflict
estimates

\[
                         L=\Omega(n^2),
 \qquad                  \Delta=O(n d(n))
\tag{3.4}
\]

are asymptotically sufficient for the **simultaneous suffix-router row**;
there is no additional factor proportional to the number `M` of ports.

This conclusion is deliberately scoped.  The candidates in (3.1) must
already be whole literal paths in one fixed materialized state, with
typed sinks and every physical conflict included in `H`.  Raw Boolean
hexagons, abstract factor incidences, marginal port menus, or paths which
exist only after candidate-dependent rematerialization do not satisfy the
hypotheses.

## 4. Relation to the ordered greedy theorem

The ordered greedy criterion

\[
 |C_i|>\sum_{j<i}\Delta_{ji}
\]

remains useful for strongly triangular conflict matrices and gives an
explicit deterministic selection.  Its uniform corollary can cost a
factor `M-1`.  Haxell's theorem, and more weakly the displayed LLL proof,
instead use the total per-candidate conflict degree and remove that global
factor.  None of these sufficient conditions is necessary; the exact
boundary remains full typed suffix rank, equivalently the all-cut Menger
inequalities in the residual occurrence network.

## 5. Scope and dependencies

This theorem proves a private typed suffix router **from** a literal
candidate atlas satisfying (1.1-H), or the weaker fallback hypothesis
(1.1-L).  It does not construct that atlas from
the current parent/reference matching, authenticate transported phase one,
plant the claim-to-port prefixes, or prove an all-dimensional carrier.
Accordingly it does not prove `nu(k)<=B(k)+O(1)` by itself.

| role | file |
|---|---|
| fixed-state regular-factor/private-router composition | `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md` |
| exact two-cross-ray common-cap boundary | `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md` |
| ordered greedy candidate-list certificate | `MATH_THEOREM_TYPED_SUFFIX_CANDIDATE_LIST_GREEDY_PRIVATE_ROUTER_20260804.md` |
| prior Haxell/LLL whole-packet selector and global-load warning | `MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md` |
