# Independent audit: one-singleton positive-resident clock and weighted support

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_ONE_SINGLETON_EXCEPTION_POSITIVE_RESIDENT_CLOCK_AND_WEIGHTED_SUPPORT_20260813.md`  
**Audited source SHA-256:**
`7b48524834c213d4228f6c7ea2dfeef4211788385da32a435b1e7d60550eea5f`  
**Verdict:** **PASS after adding the disjoint-ground/common-rank hypothesis
in (1.0).**

## 1. Graph and positive residence

The added decomposition `X dotcup Y dotcup C` is load-bearing: it ensures
that a common endpoint payload cannot mask the coordinate removed or added
by a base Johnson edge.  With it, (1.4) makes every old and new block join
exactly the corresponding base exchange and keeps every displayed owner at
one rank.

A base-coordinate run avoiding the singleton contains a whole normal
block.  If it contains the singleton, (2.2) extends it into at least one
adjacent normal block, so its length is at least `L+1`.  For an auxiliary
coordinate, an internal run is covered by condition 3.  A run through an
ordinary join only concatenates endpoint runs.  A run through the
singleton lies in `S`; (1.4) gives a terminal `h`-run, the singleton, and
an initial `h`-run, for length at least `2h+1`.  The positive-residence
proof is therefore exact.  No zero-gap conclusion is implicit.

## 2. Weighted support

The full ordered type word records whether the unique singleton is absent,
initial, terminal, or internal, as well as every normal input/output tag
type.  Thus equal type words have equal block-length words.  Equal
numerical offsets are legal in the corresponding endpoint block types,
including offset zero when an endpoint is the singleton.  Internal normal
blocks contribute the same multiples of `L=2h+2`, and the singleton
contribution agrees.  Template equality gives the same literal auxiliary
union.  Theorem 3.1 is consequently sufficient for every `h`.

The standard cyclic-arc definition is fail-closed for a repeated start
block.  A singleton cannot occur as two nonempty clipped endpoint pieces;
only arcs that actually project from lifted intervals are admitted to
`Omega`, so no spurious singleton endpoint case is introduced.

## 3. Literal `T_2` check

For

\[
 a=\{0,2,4,5,8,9,11\},
\]

the old neighbours delete `4` and `5`, while the new neighbours delete
`8` and `2`.  Hence every coordinate of `a` survives in at least one
adjacent normal block in each state, exactly as (2.2) requires.  The four
inserted coordinates `6,3,3,6` and all displayed words replay correctly.

Palette simplicity is deliberately a hypothesis (or replaceable by an
exact ledger), not an inferred property of the singleton construction.
The source also correctly leaves the finite weighted support inclusion and
global host/tensor completion open.
