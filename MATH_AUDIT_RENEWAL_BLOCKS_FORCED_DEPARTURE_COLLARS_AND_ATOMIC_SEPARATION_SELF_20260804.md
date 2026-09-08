# Self-audit: renewal blocks, forced-departure collars, and atomic separation

**Date:** 2026-08-04  
**Method:** independent symbolic replay of every implication in the theorem;
pure mathematics; no computation, search, or solver  
**Audited file:**
`MATH_THEOREM_RENEWAL_BLOCKS_FORCED_DEPARTURE_COLLARS_AND_ATOMIC_SEPARATION_20260804.md`  
**Verdict:** **SELF-GO at the stated fixed-factor and collar-only scopes.**

## 1. Renewal indexing

The theorem now states the same non-ubiquity hypothesis as the underlying
cyclic flag-serialization theorem, so every positive run has a genuine
entry and departure and `tau_i(x)` is finite.  It also states `q>=d`, the
application range in which the canonical full threshold chain starts with
the nonempty rank-`q-d+1` member.

On a run of length `ell`, an age path starts at zero and ends at `d-1`.
If `z` is its last zero, the terminal age is `ell-1-z`, so necessarily

\[
                         z=\ell-d.
\]

Consecutive zero positions have gap at most `d`; otherwise the age reaches
`d` before the next reset.  Conversely, distances from the most recent
zero give exactly the reset/increment dynamics.  The block convention
checks a reset position in the block which starts there, not in the block
which ends there, so there is no omitted endpoint constraint in
(1.4)--(1.5).

## 2. Right-aligned uniqueness

A right-aligned length-`m` flag has addresses

\[
                         d-m,d-m+1,\ldots,d-1.
\]

For fixed ages, the value at address `u` is the unique sublevel set
`{x:a(x)<=u}`.  Hence (1.7) is forced.  Strictness is exactly the condition
that the displayed sublevel sets are strict; no target relabelling remains.
Because a literal occurrence has one set value, the support formula
(1.10)--(1.11) has no hidden Hall competition.

## 3. Canonical time-to-departure ages

Let `tau` count the remaining roots of the current positive run, including
the current root.  For a survivor, `tau` decreases by one.

* `2<=tau<=d` gives an increment from `d-tau` to `d-tau+1`;
* `tau>=d+1` gives a legal zero-to-zero refresh;
* entry has `tau>=d` and hence age zero; and
* departure has `tau=1` and hence age `d-1`.

Thus (0.3) is literal.  Residence also implies that the next `j<d`
departures were already present, are distinct, and have not left earlier.
This proves the intersection identity (2.3) and the rank formula
`|I_(i,j)|=q-j`.

For threshold `t`, precisely the next `d-1-t` departures have age greater
than `t`; therefore its value is `I_(i,d-1-t)`.  The endpoint cases are
correct: `t=d-1` gives `Q_i`, while `t=0` gives the intersection of `d`
successive roots and rank `r-d`.

## 4. Forced top collar

In an arbitrary literal spelling, `alpha_(i+u)` is terminal at root
`i+u`.  Backward through fewer than `d` survivor steps, it cannot have
reset and still reach age `d-1`; hence it had age `d-1-u` at root `i`.

If the top `h+1` right-aligned flag members have consecutive ranks, then
the age classes `d-h,...,d-1` are singletons.  The future departures occupy
those classes, forcing equality, not merely containment.  Removing the top
`j` singleton classes gives exactly `I_(i,j)`.  This proves Theorem 3.2.

## 5. Nested selector scope

In a collar-saturated table, a root reaching depth `j+1` also reaches depth
`j`, so the banks `R_j` are nested.  Exact use of all rank-`q-j` targets
forces their sizes and, by Theorem 3.2, forces the intersection-colour map
to be bijective.  Conversely the canonical spelling contains all these
declared occurrences simultaneously.

The converse is intentionally only a selected-collar statement.  It does
not declare unselected canonical thresholds harmless: they can create a
large central duplicate bank.  Therefore the theorem does not infer
coefficient-one lower waste or an additive-constant word.

At `d=3`, selecting `R_2` is exactly a matching from depth-two intersection
colours to distinct depth-one colours.  Once that matching is fixed,
surjectivity of the depth-one deck fills every unused depth-one colour from
its disjoint root fibre.  This verifies both directions of Corollary 4.2;
no three-matroid claim is made.

## 6. Local separation example

For the old flag, the age classes are `{1}` and `{2,4}`.  The good new
terminal class `{1}` is contained in the old age-zero class; the bad new
terminal class `{4}` is not.  Both new bottom targets have rank two, both
contain the newborn `3`, and the old top block contains the departure `2`.
Thus changing only the rank-two target name toggles the exact survivor
equation while all recorded rank/address/endpoint data stay fixed.

This is a local separation theorem.  It is not presented as a completed
resident owner-exact global counterexample.

## 7. Exact exclusions

The audited theorem does not prove:

* existence of the nested bijective banks (4.3) on the protected factor;
* a renewal construction covering residual ranks below `r-d`;
* zero or bounded duplicate waste from unselected thresholds;
* connectedness, upper completeness, or a safe linear opening; or
* `nu(k)<=B(k)+O(1)`.

Its proof-safe gain is an exact reparameterization of the right-aligned
co-selection problem by renewal positions and root cutoffs, plus the forced
future-intersection law for the consecutive top collar.
