# The side-pairing metric obstruction and the corrected topology gate

Date: 2026-07-31  
Status: exact all-`n` necessary inequality; explicit obstruction family for
every `n>=3`; corrected existential two-shore gate.  This refutes only the
universal prescribed-pair sufficient theorem, not the two-coordinate
recursion itself.

## 0. Verdict

The abstract topology-decoupling theorem is valid, but its proposed
shore-local strengthening

```text
realize every requested Cat_n-matching of seam anchors
```

is false.  A physical side component joining two anchors is a Johnson path,
so the sum of the Johnson distances of all requested double-anchor pairs
cannot exceed the complete side-edge budget.

Put

\[
 K=\operatorname{Cat}_n,\qquad
 P={2n\choose n-2}.
\]

The average available budget per double-anchor pair is

\[
                         {P\over K}={n(n-1)\over n+2}<n-1.       \tag{0.1}
\]

Consequently a requested matching of `K` maximum-distance pairs is
impossible.  Such anchor sets and pairings exist in every dimension
`n>=3`.  Already at `n=3`, five requested distance-two pairs require ten
edges while the entire side has only six.

The recursion therefore needs **joint selection of physically realizable
pairings on the two shores**.  The correct remaining topology row is not
universality of either shore's pairing map; it is that the two realizable
pairing families contain one pair whose union with the central partial
matching is acyclic.

## 1. Metric budget

Use the notation of the two-coordinate collar.  One diagonal side forest
has

\[
 N={2n\choose n-1}\quad\hbox{rank-}(n+1)\hbox{ owners},
 \qquad P={2n\choose n-2}\quad\hbox{edges}.            \tag{1.1}
\]

Its seam-anchor set has order

\[
 C={2n\choose n}-{2n\choose n-2},                    \tag{1.2}
\]

and the signed component charge forces `K=Cat_n` double-anchor components
when there is no anchor-free component.

For rank-`(n+1)` owners `A,B`, write

\[
                  d_J(A,B)={|A\mathbin\triangle B|\over2}.     \tag{1.3}
\]

### Theorem 1.1 (side-pairing distance inequality)

Let `G` be a punctured saturating side forest with seam-anchor degree at
most one and no anchor-free component.  Let `Pi(G)` be its matching of the
`K` pairs of anchors lying in the double-anchor components.  Then

\[
                  \boxed{\sum_{\{A,B\}\in\Pi(G)}d_J(A,B)\le P.} \tag{1.4}
\]

More sharply, the left side is at most the number of edges lying in the
double-anchor components.

#### Proof

Each double-anchor component is a path in `J(2n,n+1)` from its two anchors
`A,B`.  Its length is at least `d_J(A,B)`, because every Johnson edge
changes one element.  The double-anchor components are edge-disjoint, and
all their edges are among the `P` side edges.  Summing their path lengths
proves (1.4). \(\square\)

This condition is independent of lower/upper palette Hall, the common
basis and the contracted two-shore topology.  It is a prior physical
obstruction.

## 2. Universal prescribed pairing is impossible

The exact identities are

\[
 N=nK,\qquad
 {P\over K}={n(n-1)\over n+2},\qquad
 {C\over K}=4-{6\over n+2}.                           \tag{2.1}
\]

Thus `C>2K`, so an anchor set has room for the endpoints of `K` disjoint
pairs.  The Johnson diameter on rank `n+1` of a `2n`-set is `n-1`.

### Theorem 2.1 (bad requested pairings in every dimension)

For every `n>=3`, there is a `C`-element anchor set
`B subset binom([2n],n+1)` and a matching `Pi` of order `K` on `B` such
that every pair of `Pi` has Johnson distance `n-1`.  No punctured side
forest can realize `Pi` with no anchor-free component.

#### Proof

For the obstruction, once the matching exists,

\[
 \sum_{AB\in\Pi}d_J(A,B)=K(n-1)>P                 \tag{2.2}
\]

by (2.1), contradicting Theorem 1.1.  Add arbitrary unused owners to the
`2K` endpoints to obtain an anchor set of order `C`.

It remains to supply the matching.  For `n>=7`, fix a two-set
`S subset [2n]` and consider

\[
              {\cal F}_S=\{A\in{[2n]\choose n+1}:S\subset A\}.
\]

The map

\[
                         \phi(A)=S\cup([2n]\setminus A)        \tag{2.3}
\]

is a fixed-point-free involution of `cal F_S`, and
`A intersect phi(A)=S`.  Hence its orbits are maximum-distance pairs.  The
number of pairs is

\[
 {1\over2}{2n-2\choose n-1}\ge K,                 \tag{2.4}
\]

where (2.4) is equivalent to

\[
                  n(n+1)\ge4(2n-1),
\]

and holds for every integer `n>=7`.

For `n=3,4,5,6`, explicit maximum-distance matchings of order `K` are
retained in the finite audit.  This finite base plus (2.3) proves the claim
for every `n>=3`. \(\square\)

The small cases need no black-box search theorem: the audit greedily scans
the complete distance-`(n-1)` generalized Johnson graph and writes the
literal pairs.

### Example 2.2 (the transparent `n=3` obstruction)

Use decimal bitmasks on six coordinates.  Take every rank-four owner except
`15` as an anchor, and request

```text
(23,43), (27,39), (29,46), (30,45), (51,60).
```

Every pair has Johnson distance two.  Their required total path length is
ten, whereas

\[
                         P={6\choose1}=6.             \tag{2.5}
\]

Thus this requested pairing is impossible even though the scalar component
and anchor counts are correct.

This example does not assert that the displayed anchor bank is the image of
a common basis in the retained `n=3` recursion.  Its role is to disprove a
universal realization theorem over arbitrary prescribed pairings.

## 3. The corrected exact gate

Fix a child Catalan forest and a synchronized common basis `Q`.  Let
`B^-` and `B^+` be its two inherited seam-anchor banks.  Define

\[
 {\mathfrak P}^-_Q, {\mathfrak P}^+_Q                 \tag{3.1}
\]

to be the families of `K`-matchings on `B^-` and `B^+`, respectively,
which are induced by punctured saturating side forests satisfying

1. the required diagonal palette matching;
2. side maximum degree at most two;
3. seam-anchor degree at most one; and
4. no anchor-free component.

Let `P_0(Q)` be the partial left-right matching obtained by contracting the
retained child segments.

### Theorem 3.1 (exact no-empty topology gate)

Subject to the no-anchor-free sufficient normal form, the two-coordinate
physical support exists if and only if there are

\[
       \Pi^-\in{\mathfrak P}^-_Q,qquad
       \Pi^+\in{\mathfrak P}^+_Q                         \tag{3.2}
\]

such that

\[
                         P_0(Q)\cup\Pi^-\cup\Pi^+
                         \quad\hbox{is a forest}.       \tag{3.3}
\]

#### Proof

Every side component has one or two anchors, with exactly `K`
double-anchor components, so contraction gives precisely the matchings in
(3.2), plus leaves at singleton anchors.  The central components contract
to `P_0(Q)`.  The full seam-component incidence graph is a barycentric
subdivision of (3.3) with leaves adjoined.  It is acyclic exactly when
(3.3) is.  Expanding the contracted side and central forests preserves
cycle rank, and all degree caps are already included in the definitions of
the two families. \(\square\)

The abstract topology theorem says that for every matching `Pi^-` there is
*some abstract* matching `Pi^+` making (3.3) a forest.  Theorem 2.1 shows
why this does not finish the recursion: that abstract `Pi^+` may lie outside
the physically realizable family `mathfrak P^+_Q`.

Accordingly, the shortest honest replacement for universal prescribed-pair
realization is one of the following weaker statements.

* **Joint realizable-pair theorem:** choose `Q` and both side forests at
  once so (3.3) holds.
* **Graphic-richness theorem:** for one shore, its realizable pairing family
  meets every acyclic-completion class generated by `P_0` and the other
  shore.
* **Metric-feasible greedy theorem:** run the abstract greedy completion
  while restricting every selected pair to the realizable pairing family
  and maintaining (1.4).

No one of these statements is proved here.  They are strictly weaker—and
correctly scoped—than realizing every requested matching.

## 4. Reproducible audit

The standard-library audit

```text
scratch/audit_catalan_side_pairing_metric_obstruction_20260731.py
```

checks all binomial identities and strict metric inequalities for
`n=3,...,100`; records the involution capacity from `n=7` onward; constructs
literal distance-`(n-1)` matchings of order `K` for `n=3,4,5,6`; and checks
the transparent five-pair `n=3` witness.  It writes

```text
scratch/catalan_side_pairing_metric_obstruction_20260731.audit.json.
```

The finite matching witnesses establish only the stated universal-pairing
counterexamples.  They do not enumerate recursively obtainable common bases
or either realizable pairing family in (3.1).
