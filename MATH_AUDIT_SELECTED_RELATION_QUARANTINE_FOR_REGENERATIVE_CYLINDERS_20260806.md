# Audit of selected-relation quarantine for regenerative cylinders

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_SELECTED_RELATION_QUARANTINE_FOR_REGENERATIVE_CYLINDERS_20260806.md`  
**Method:** stopped-event induction, future-quarantine measurability, and
cleanup accounting; no computation or search  
**Verdict:** **PASS WITH TWO EXPLICIT QUALIFICATIONS.**  The raw-to-cleaned
cylinder is valid if every marked block type later queried is included in
the tests, and the probability proof is read as a killed-event induction,
not as conditioning the next clock on future survival.  The expected
cleanup scale is correct.  A constant unconditional probability of small
cleanup does not by itself give a fully hereditary cylinder after arbitrary
stopped prefixes.

## 1. Future-dependent quarantine does not bias the raw clock

Fix prescribed blocks `A_1,...,A_q`.  At a raw pre-hit history `H`, let
`F(H)` be the conditional probability that all prescribed blocks are later
selected and survive quarantine.

If a required pair or cluster row has failed anywhere in `H`, then

\[
                         F(H)=0.
 \tag{1.1}
\]

Indeed, if the relevant blocks are later selected, the definition of the
bad graph marks a relation or a vertex and quarantine deletes at least one
of them.  If no required row has failed, the next raw exponential clock has
its original cause distribution.  Bonferroni and the cluster row bound that
raw cause exactly as in the regenerative first-hit theorem.  Induction on
the number of remaining blocks then gives the displayed cylinder.

This is a killed-event argument on the raw filtration.  One must not first
condition the clock law on the future event that all blocks survive
quarantine; that conditioning could bias the cause distribution.  The
source conclusion is valid, but this is the proof-safe interpretation of
its conditioning sentence.

Raw selected edges which are later deleted cause no problem.  Before a
requested first hit they are ordinary intervening raw transitions; if they
consume a requested carrier, the requested event becomes impossible.
After a requested service, later deletion only destroys the event.

## 2. Exhaustive tested-block scope

The bad graph protects only the occurrences and clusters which its tests
include.  Therefore Theorem 2.1 applies to every cylinder queried later
provided the post-run construction tests:

* every marked occurrence in a selected edge;
* every compatible same-edge marked block of the sizes used by the
  cluster row, here at most three; and
* every pair of selected carrier blocks needed by the cross-edge row.

For a balanced doublet this is only a bounded list per selected edge,
because it carries at most six marked owner occurrences.  If some queried
block is omitted from the tests, equations (2.1)--(2.2) of the source need
not hold for it.

## 3. Cleanup scale

Deleting all individually bad selected edges and both endpoints of every
bad relation removes at most

\[
                         B_0+2B_1
 \tag{3.1}
\]

doublets.  Each balanced doublet contains exactly `2d` lower resources.
Thus

\[
 \mathbb E(B_0+B_1)=O(M/d^2)
 \tag{3.2}
\]

implies expected additional lower leave `O(M/d)`.  Thus the little-oh scale
in the source is stronger than necessary for the stated big-oh leave.  A
smaller vertex cover may improve constants but is not needed.

If the raw process reaches separator density with probability at least
`c_0>0`, Markov's threshold may be chosen so that cleanup failure has
probability below `c_0/2`; the intersection then has positive probability
and still costs `O(M/d)`.

## 4. Conditioning and hereditary scope

Conditioning the final cleaned law on an event `G` with
`Pr(G)>=c_0>0` multiplies every **unconditional** cylinder probability by
at most `1/c_0`, which is an allowed fixed root factor.

For a stopped prefix `H`, however,

\[
 \Pr(\mathcal C\mid H,G)
 ={\Pr(\mathcal C\cap G\mid H)\over\Pr(G\mid H)}.
 \tag{4.1}
\]

An unconditional lower bound on `Pr(G)` gives no lower bound on
`Pr(G|H)`.  Therefore global success conditioning does not automatically
preserve the same fixed factor after every doublet-closed separator
exposure.

The raw post-quarantine law does retain the stopped killed-event cylinder:
repeat Section 1 after any fixed raw prefix.  To combine that heredity with
a deterministic `O(M/d)` cleanup bound, an application needs one of:

1. a uniformly positive conditional probability of small cleanup after
   every allowed prefix;
2. an almost-sure cleanup cap; or
3. a downstream theorem which only needs expected cleanup and the
   unconditioned cylinder.

This is a scope qualification, not a failure of the selected-relation
cylinder itself.

## 5. Final verdict

Selected-relation quarantine validly replaces a maximum pair test against
all potential carriers by an average over pairs actually selected.  This
is exactly the quantifier matched by the rooted squared-codegree energy of
the rank-compensated doublet clock.  Its remaining application inputs are
the averaged estimate (3.2), positive continuation to separator density,
and the hereditary cleanup qualification in Section 4.
