# Audit of the one-token Hall relay and cross-depth compactness theorem

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_ROOT_ONE_TOKEN_HALL_RELAY_AND_CROSS_DEPTH_COMPACTNESS_20260802.md`  
**Theorem SHA-256:**
`a84ec0d89dc42ed07e9a1edc29d0ddbd36613235455da58ce917c7eb94319cf3`

## 0. Verdict

PASS at the frozen accepted-predecessor layer.

The theorem gives a genuine exact nonaccumulation mechanism: one added Hall
capacity unit repairs a deficit-one slice, a full integral matching leaves
one capacity unit unused, and that unused unit is the outgoing token.  The
input/output relation is characterized by Hall cuts, and finite-horizon
compatibility is equivalent to an infinite relay by finite branching.

The scope boundary is stated correctly.  The result does not prove that an
abstract capacity copy is a literal physical port, that the selected packet
bank is connected, or that an output token suspends into the next depth.
Those data live in `Sigma_m` and the protected skeleton, not in the Hall
calculus.

## 1. Repair-aperture min--max

For baseline capacities `b`, adding one copy at `x` changes the capacity of
the neighborhood `N(J)` by exactly `1_(x in N(J))`.  Hall is therefore

\[
                 |J|\le b(N(J))+{\bf1}_{x\in N(J)}.    \tag{1.1}
\]

One copy cannot repair a cut of deficit at least two.  If every deficit is
at most one, the only new conditions are that `x` belong to every
deficit-one neighborhood.  Their intersection is exactly `C_b`.  This
proves Theorem 2.1 independently of any fractional or polymatroid argument.

The theorem correctly introduces the actual repair set `R_b` after the
deficit dichotomy.  This avoids a subtle false statement: when a deficit-two
cut exists, the formal intersection of deficit-one neighborhoods can be
nonempty even though no one-token repair exists.

## 2. Output aperture

After adding the input copy, total capacity is `|I|+1`.  Deleting a proposed
output copy at `y` lowers precisely those Hall neighborhoods containing
`y`.  It is legal exactly when each such cut had augmented slack at least
one.  Equivalently, `y` belongs to no augmented-tight neighborhood.  This is
formula (3.5).

Nonemptiness is constructive: any matching of all roles into the augmented
copies leaves one copy unused, and deleting that copy preserves the same
matching.  When the baseline deficiency is one, the unused copy cannot be
the copy just added, because deleting it would return to the infeasible
baseline.  Thus forced token motion is exact, not a heuristic interpretation
of the Pascal aperture.

The two-role example is minimal.  With both menus equal to `{a}` and
capacities `b(a)=b(c)=1`, the only relay is

\[
                              a\Rightarrow c.
\]

An identity suspension fails; a physical suspension `c_m -> a_(m+1)` gives
an infinite one-token chain.  Disjoint copies have additive deficiency and
require one simultaneous input token per copy.

## 3. Boundary sign

Let `m` be the fixed-head count and `eta` the protected-bank boundary, with
`b=m+eta`.  A relay matching uses tail count

\[
                         p=b+{\bf1}_x-{\bf1}_y.
\]

The free boundary is `m-p`; after adding `eta` it is

\[
                         {\bf1}_y-{\bf1}_x.
\]

Thus the sign in (4.1) is correct: the selected bank has the boundary of an
arc from input `x` to output `y`.  Boundary equality alone does not imply
one connected trail; balanced extra components remain possible and are
correctly left to the skeleton theorem.

## 4. Cross-depth quantifiers

The layered edge `x ->_m x'` contains three existential choices on the same
frozen slice:

1. an integral relay matching `x => y`;
2. an unused physical output state `y`; and
3. one literal suspension `(y,x') in Sigma_m` into the next repair set.

The token is declared Markov-complete: every field read by the next slice is
part of its state.  Under that convention, edges compose.  Without it,
pairwise slice witnesses can choose incompatible hidden histories or
addresses, and the path proof would reverse quantifiers.

For a fixed initial token, all finite compatible paths form a prefix-closed
tree.  Each node has finite degree because both adjacent state banks are
finite.  Nonempty levels of every depth therefore give an infinite branch
by Koenig's lemma.  This justifies the exact weakening from left-totality to
arbitrarily long compatible finite horizons.

Separate existence of one slice at every depth is weaker: it need not make
any level of this rooted path tree nonempty.  Similarly, a full-q1 K17
certificate and a residence-improved K17 certificate cannot be combined by
taking their best scalar coordinates unless they are one vertex/edge of the
same complete-state relay graph.

## 5. Relation to the newest inputs

The corrected pull clock closes fractional stationary membership, but has
no integral occurrence-labelled capacity copy and does not determine
`R_b` or `O_b(x)`.

The screened-collar theorem makes local residence and owner-derived upper
signatures menu-invariant, yet its predecessor deficit-one obstruction can
be replicated.  The audit confirms that this is a simultaneous within-slice
obstruction, not a temporal accumulation issue.

The K17 full immediate-upper circulation and the residence/deep-upper
descents demonstrate that the principal rows are nonempty and mobile in
scoped frozen models.  They do not yet expose an unused complete-state
capacity token or its cross-depth suspension.  The theorem's rebase keeps
that evidence in its valid scope.

## 6. Finite replay

The independent verifier

`scratch/audit_root_one_token_hall_relay_20260802.py`

has SHA-256

`17b629435a3368a980ca62a45cca1515ef6131139e0d7afa47c424fd6625edca`

and returns

```text
PASS
exhaustive_systems=40310 repairable_inputs=64416 relay_pairs=111050
sampled_four_state=5000 repairable_inputs=11104 relay_pairs=19629
replicated_deficit_copies=1..6
```

For every exhaustive system it compares:

* augmented matching existence with every cut in (2.3);
* the repair-core formula when the baseline deficiency is at most one;
* the output relation with both residual-capacity matching and (3.3);
* the tight-neighborhood output formula (3.5);
* nonemptiness of every repairable output aperture; and
* forced motion when the baseline deficiency is one.

It also checks 5,000 deterministic four-state samples and disjoint
replication through six copies.  This replay audits the finite matching
identities; the cross-depth compactness assertion is proved by the tree
argument, not by finite extrapolation.

## 7. Scope ledger

**Proved:** the exact input repair set, output aperture, one-in/one-out
boundary conservation, replicated-deficit obstruction, layered relay
criterion, and finite-horizon compactness equivalence.

**Unproved:** existence of an all-dimensional frozen slice with global
deficiency at most one; physical input/output port binding; a protected
connected skeleton; full source/address/history and compiler closure; a
literal suspension edge into every required next depth; bounded terminal
repair on the same host; and any new upper bound for `nu(k)`.

