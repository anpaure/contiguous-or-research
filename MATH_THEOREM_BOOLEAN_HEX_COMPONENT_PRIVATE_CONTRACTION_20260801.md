# Component-private ternary hexes give an exact cycle contraction

Date: 2026-08-01  
Status: exact deterministic contraction theorem.  It isolates the precise
list-versus-component-load inequality which would reduce `c` physical cycles
to `o(c)`.  The companion hex-free theorem proves that this inequality is
not a consequence of the Delcourt--Postle hypotheses alone.

## 1. Applicable packet lists

Let `M` be a four-resource matching.  Its directed physical graph has
indegree and outdegree at most one, so every component is a directed path or
a directed cycle.

For each cycle component `C`, let `A_C` be a collection of ternary-hex old
phases

\[
 O(P)=\{A B,C'D,E F\}\subseteq M                         \tag{1.1}
\]

such that

* `EF` lies on `C`;
* `AB` and `C'D` lie on two distinct path components; and
* those three components are pairwise distinct.

Thus every `P in A_C` is individually applicable by the exact cycle-mode
theorem.  Its **component footprint** `kappa(P)` is that triple of physical
components.

Put

\[
 L=\min_C |A_C|,
 \qquad
 \rho=\max_Q |\{P:Q\in\kappa(P)\}|,                   \tag{1.2}
\]

where `Q` ranges over all physical components and the packet count is over
the union of all lists.

## 2. Contraction theorem

### Theorem 2.1 (component-private contraction)

If `M` has `c` physical cycles, there is a set `I` of pairwise
component-disjoint applicable packets, using at most one packet from every
cycle list, of size

\[
 |I|\ge {cL\over L+3(\rho-1)}.                         \tag{2.1}
\]

Toggling all packets in `I` simultaneously preserves every lower, upper,
tail and head resource and leaves at most

\[
 c'\le {3(\rho-1)\over L+3(\rho-1)},c               \tag{2.2}
\]

physical cycles.

In particular, the quantitative supply estimate

\[
                              L\ge m^\epsilon\rho       \tag{2.3}
\]

implies

\[
                              c'\le3m^{-\epsilon}c.      \tag{2.4}
\]

#### Proof

Form the conflict graph on all listed packets: two packets conflict if they
belong to the same cycle list or if their component footprints meet.  Take
a maximal independent set `I`, and write `s=|I|`.

Consider a cycle whose list contributes no member of `I`.  By maximality,
every one of its at least `L` packets meets the component footprint of a
selected packet.  A selected footprint has three components, and each
component belongs to at most `rho` listed packets including the selected
one.  It therefore conflicts, outside its own cycle list, with at most
`3(rho-1)` packets.  Double counting conflicts between selected packets and
the lists of unselected cycles gives

\[
                         L(c-s)\le3(\rho-1)s.            \tag{2.5}
\]

Solving for `s` proves (2.1).

Distinct selected packets occupy disjoint old physical components.  Their
old atoms are therefore distinct; because `M` is a four-resource matching,
their complete typed supports are disjoint.  Every new phase uses exactly
the typed support of its old phase.  Hence all toggles are resource
compatible.

On each footprint, the cycle-mode theorem replaces one cycle and two paths
by two paths.  Disjoint footprints make these changes commute.  Exactly
`s` cycles disappear and none is created, proving (2.2).  Equation (2.4)
is immediate.  `square`

### Corollary 2.2 (all cycles at once)

If every list has size at least `L>6(rho-1)`, delete the irrelevant edges
inside each list and regard the lists as the vertex parts.  The resulting
cross-conflict graph has maximum degree at most `3(rho-1)`, so the standard
independent-transversal bound `part size > 2 Delta` gives one packet from
every cycle list.  All cycles may then be eliminated simultaneously.

For the contraction application, Theorem 2.1 is preferable: it needs only a
growing ratio `L/rho`, not a full transversal.

## 3. Dynamic versus frozen applicability

The component-private hypothesis is deliberately stronger than necessary.
A balanced ternary-hex switch consumes no permanent graphic rank or fresh
sink: its two path components are returned as two paths.  Thus a small path
bank may in principle be reused serially.

The exact dynamic object is the state digraph whose vertices are
four-resource factors and whose arcs are legal ternary-hex toggles.  A
factor with `c` cycles contracts precisely when it reaches a state with
fewer than `c` cycles.  Static individual applicability is insufficient:
two packets may share a path component, and the first toggle can invalidate
the second.  Component-disjointness avoids this issue and is why Theorem
2.1 is unconditional.

The corresponding weaker future target is a **returned-catalyst theorem**:
from every nonterminal state, one of a bounded set of path-bank states has
an applicable cycle packet and the resulting path-bank state remains in the
same bounded set.  Such a theorem would permit serial contraction without
the list/load ratio (2.3).

## 4. Exact remaining supply statement

For one matching component `Q` with `q` atoms, the crude catalogue bound is

\[
 |\{P:Q\in\kappa(P)\}|\le q(m-1)^2,                  \tag{4.1}
\]

because an atom belongs to exactly `(m-1)^2` displayed packet lines.  There
is no positive universal lower bound on `L`: the companion theorem
`MATH_THEOREM_BOOLEAN_HEX_DP_HEX_FREE_CYCLE_OBSTRUCTION_20260801.md`
constructs a valid `N-o(N)` Delcourt--Postle body with one cycle and `L=0`.

Therefore (2.3) must be enforced while the body is chosen.  It cannot be
deduced afterward from near-perfectness, high physical girth, or the full
conflict-free colouring alone.
