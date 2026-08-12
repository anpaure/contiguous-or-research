# Goddyn--Gvozdjak long runs do not survive literal middle-level restriction

Date: 2026-08-02  
Status: unconditional obstruction to the direct restriction/compression
route, plus an exact statement of the missing nonlocal bridge.  This does not
rule out adapting the Goddyn--Gvozdjak stream construction itself.

## 0. Context

Goddyn and Gvozdjak prove that the `n`-cube has a cyclic Gray code with
minimum bit-run length

\[
                    R\ge n-3\log_2 n
\]

(and a slightly sharper constant in their paper).  Numerically this is far
larger than the middle-level requirement relevant here:

\[
  2d(n)+1=\sqrt{\pi n/2}+O(1).
\]

The numerical reserve is real.  What is missing is not run length but a
rank-compatible compression.

## 1. Extreme-excursion obstruction

Put `n=2m+1`, and let

\[
 C=(v_0,v_1,\ldots,v_{2^n-1})
\]

be a cyclic Hamilton cycle of the cube.  Say that its transition separation
is at least `R` if two flips of the same coordinate are at cyclic transition
distance at least `R`.

### Theorem 1

If `R>=m`, then listing the vertices of weights `m` and `m+1` in their cyclic
order along `C` is not a walk in the middle-level graph.

More precisely, the two middle vertices nearest the all-zero vertex on its
two sides are distinct rank-`m` vertices, consecutive in the restricted
cyclic order, and the arc of `C` between them through zero has length `2m`.
The analogous arc through the all-one vertex has two rank-`m+1` endpoints.

#### Proof

Start at the all-zero vertex and follow `C` in one direction.  During the
first `m` transitions no coordinate repeats.  Every flipped coordinate was
therefore still zero, so the weights are exactly

\[
                         0,1,2,\ldots,m.
\]

The first encountered middle vertex has rank `m` and lies at distance `m`.
The same argument in the opposite direction gives a second rank-`m` vertex
at distance `m`.  They are distinct because `C` is Hamiltonian.  Every
internal vertex on the arc through zero has rank below `m`, so the two
endpoints are consecutive after middle-level restriction.

Every edge of the middle-level graph joins different ranks, so two rank-`m`
vertices cannot be adjacent.  Complementing the argument gives the
rank-`m+1` obstruction through the all-one vertex.  QED.

### Corollary 2

For all sufficiently large odd `n`, every Goddyn--Gvozdjak long-run cycle has
the obstruction in Theorem 1.

In particular, neither of the following operations produces a middle-level
Hamilton cycle:

1. delete every vertex outside the two middle levels and retain the induced
   cyclic order;
2. contract each maximal outside excursion to an edge with the same retained
   endpoints.

The second operation fails because every lower excursion has two rank-`m`
endpoints and every upper excursion has two rank-`m+1` endpoints.

## 2. The quantitative compression gap

Suppose one nevertheless tries to obtain a middle transition word by an
order-preserving block compression of the full Gray cycle.  To inherit a run
floor `L` from transition separation `R`, the usual sufficient density row is

\[
       \text{maximum source-block length }g\le R/L.       \tag{2.1}
\]

For `L=2d(n)+1` and the Goddyn--Gvozdjak value of `R`, the right side is

\[
 \frac{R}{2d(n)+1}
      =\sqrt{\frac{2n}{\pi}}+O(\log n/\sqrt n)
      =\left(\frac4\pi+o(1)\right)d(n).                  \tag{2.2}
\]

This is a plausible scale on average: the ratio between all cube vertices
and all middle-level vertices is

\[
 \frac{2^n}{2\binom n m}
      =\sqrt{\frac{\pi n}{8}}+O(n^{-1/2})
      =d(n)+O(1).
\]

But Theorem 1 forces a literal source block of length `2m=n-1` through zero
if a whole outside excursion is represented by one middle edge.  Therefore
literal excursion contraction has `g=Theta(n)`, and (2.1) transfers only a
constant run floor, not `Theta(sqrt n)`.

The obstruction is thus much stronger than a small boundary loss.  A useful
compression would have to split and globally interleave the extreme
excursions; it cannot preserve the original cyclic order component by
component.

## 3. Why the product-stream proof is not rank-stationary

The Goddyn--Gvozdjak recurrence constructs a Hamilton cycle of
`Q_a x Q_b` by merging

* a stream in `Q_a` whose step-permutation has one bipartition shore as an
  orbit; and
* a Hamilton cycle in `Q_b`.

The invariant is parity.  At a fixed stream time the `Q_a` states range over
the entire even or odd shore.  The middle-level condition in the product is

\[
                 |x|+|y|\in\{m,m+1\},                    \tag{3.1}
\]

which is not determined by the two parities.  Restricting the merged walk to
(3.1) therefore destroys the orbit identity used to prove Hamiltonicity.
The long-run recurrence supplies no rank-refined replacement for that
identity.

Equally importantly, a long transition run is a statement about *which
coordinate* flips; it puts no restriction on the signs of successive weight
changes.  A block of distinct coordinate flips may alternate additions and
deletions at every step.  Hence it need not contain a useful monotone chain
segment.

## 4. The exact bridge that would make the theorem useful

Delete from `C` all vertices outside the middle two levels.  The retained
edges form a path forest `P` on all middle vertices.  Each component endpoint
is a port at which `C` entered a lower or upper excursion.

The required new statement is the following.

### Run-preserving excursion-braid lemma

There is a set `F` of middle-level containment edges such that

1. `P union F` is one Hamilton cycle on all middle vertices;
2. lower-excursion ports and upper-excursion ports are paired globally, not
   by contracting each excursion to its own endpoints;
3. the edges of `F` and the retained edges admit a cyclic coordinate
   labelling with minimum transition run at least `2d(n)+1`;
4. the braid carries an order/density certificate that transfers the
   Goddyn--Gvozdjak separation, or proves the same separation afresh after
   the component permutation.

Conditions 1--2 are an uncoloured endpoint-factor/Hamilton-joining problem.
Conditions 3--4 are a coloured scheduling problem: a new edge `L subset U`
has colour `U\L`, and the old Gray-code theorem does not constrain two new
chords of the same colour.

Theorem 1 proves that condition 2 is indispensable.  Section 2 proves that a
one-edge-per-excursion order-preserving contraction cannot satisfy condition
4.  Thus a valid bridge must be a genuinely nonlocal coloured braid.

## 5. Relation to symmetric-chain constructions

The central-levels constructions of Gregor--Micka--Mutze give both

* Hamilton cycles in every central band; and
* a full-cube Hamilton cycle containing the Greene--Kleitman symmetric-chain
  decomposition.

This solves the uncoloured adjacency/topology problem in a different host,
but it does not give the Goddyn--Gvozdjak run floor.  Conversely, the
Goddyn--Gvozdjak host gives the run floor but not the rank-compatible braid.

A possible synthesis would require an almost equitable monotone-segment
decomposition with maximum half-segment length at most

\[
                     (4/\pi+o(1))d(n),                   \tag{5.1}
\]

plus run-transparent joins.  Ordinary Greene--Kleitman chains have extreme
half-length `Theta(n)`, so they do not satisfy (5.1).  Obtaining (5.1) is
closely aligned with the equitable-chain obstruction already visible in the
OR-word lower bound.

## 6. Verdict

The Goddyn--Gvozdjak theorem is encouraging numerically but does not presently
shorten the proof.  Its direct middle-level restriction is impossible, and
its literal excursion compression loses the run scale by a factor
`Theta(sqrt n)`.

The exact reusable target is not another full-cube long-run code.  It is the
run-preserving excursion-braid lemma (or an equivalent equitable monotone-
segment compression).  Proving that lemma would turn the full-cube theorem
into a middle-level residence theorem; without it, the two results control
orthogonal resources.

Primary references:

* L. Goddyn and P. Gvozdjak, *Binary Gray Codes with Long Bit Runs*,
  Electronic Journal of Combinatorics 10 (2003), R27,
  DOI `10.37236/1720`.
* P. Gregor, O. Micka and T. Mutze, *On the Central Levels Problem*,
  arXiv `1912.01566`.
