# Small next search after the prescribed `ML_11` extension

## 1. State and exact objective

Represent a middle-level Hamilton cycle as the union of two disjoint perfect
matchings `M_0,M_1` between the 462 rank-five and 462 rank-six masks.  Colour
the 36 edges of the prescribed path alternately and freeze them in the
corresponding matching.  Every state considered below therefore retains the
entire prescribed path and every middle-layer vertex.

Orient the single cycle so that the nineteen prescribed rank-six masks occur
first in their certified order.  Write the resulting rank-six row as

\[
                    C_1,C_2,\ldots,C_{462}.
\]

For the `q=19` mixed schedule, an internal coordinate one-run beginning in
row position at most 20 must have length at least three; a later internal run
must have length at least four.  Define the exact run deficit

\[
 \Delta(C)=\sum_R\max\{0,m(R)-|R|\},
\]

where `m(R)` is the applicable minimum.  Mixed-delay factorability is exactly
`Delta(C)=0`.  The secondary score is the number of deficient runs.

This objective is exact, although the search described below is heuristic.

## 2. Bounded perfect-matching sampler

`ml11_prescribed_matching_search.cpp` now accepts an optional fourth numeric
argument `SHORT_COUNT`.  In that mode it repeatedly:

1. completes each frozen path-edge colour to a perfect matching;
2. forbids the first matching's edges while completing the second;
3. rejects a union having more than one cycle; and
4. scores the oriented Hamilton cycle by the exact mixed-run criterion.

It emits the best connected certificate found.  A bounded local run

```bash
./ml11_match k11_ml_prescribed_path_q19.txt 5000 77125 19 \
  > k11_ml_prescribed_cycle_q19_runbest210.txt
```

took about 0.42 seconds in the recorded environment and improved the `q=19`
score from

\[
             (\Delta,\#\text{bad runs})=(239,154)
\]

to

\[
                         (210,136).
\]

The resulting 924-vertex output independently passes the complete Hamilton
cycle and prescribed-path verifier.  This is a search checkpoint, not an
optimality or impossibility certificate.

Its SHA-256 is

```text
e42c4fa8f2a658a9d0c74e34a47d83e1218bea643ead242f6ca4beff07ac0020  k11_ml_prescribed_cycle_q19_runbest210.txt
```

For comparison, exhaustive 369/93 cutting of this newer cycle gives:

```text
valid_q_arcs=702 factorable=0
best deficit=91 violations=82 start_mask=1338 direction=1
prefix_at_P_start direction=-1 reversed=0 deficit=109 violations=93
prefix_at_P_start direction=1  reversed=1 deficit=95  violations=84
```

Thus sampling different completions matters materially; the original
cycle's best 369/93 deficit was 111.

## 3. Prefix-preserving local matching exchange

Randomly rebuilding both matchings discards useful structure.  The smallest
local move is an exchange in one matching.  If that matching contains

\[
                   l_1u_1,\qquad l_2u_2,
\]

and the cross-incidences `l_1u_2,l_2u_1` exist, replace the first pair by the
second.  The move is legal when neither removed edge is frozen and neither
new edge belongs to the other matching.  It preserves perfection,
disjointness, all vertices, and the complete prescribed path.

There is an exact component rule:

- if the two removed edges lie in different alternating cycles, the exchange
  merges those cycles;
- if they lie in one alternating cycle, the exchange splits it into two.

Therefore no nontrivial single exchange preserves a Hamilton cycle.  The
minimal Hamilton-preserving neighborhood uses **two** exchanges:

1. switch two unfrozen `M_0` edges of the Hamilton cycle, producing two
   alternating cycles;
2. switch one unfrozen `M_1` edge from each of those components, choosing
   valid cross-incidences; this merges them back into one cycle.

The same operation with the colours reversed is also allowed.  Exactly four
old and four new incidence edges are involved.  Every accepted state remains
a full middle-level Hamilton cycle containing the prescribed path, so no
subtour repair or post hoc certificate reconstruction is needed.

## 4. Proposed bounded optimizer

Maintain the two matching arrays, their inverse arrays, and frozen-edge bits.
For each iteration:

1. sample two removable same-colour edges and test the two cross incidences;
2. temporarily apply the splitting exchange and label its two components;
3. sample or enumerate pairs of opposite-colour removable edges lying in
   different components;
4. accept a valid merging exchange when the lexicographic score
   `(run deficit, bad runs)` improves, with occasional annealed neutral moves;
5. periodically verify from scratch that both matchings are perfect and
   disjoint, their union is one cycle, and the prescribed path is intact.

Recomputing the complete run score costs only `O(11*462)` per candidate, so
incremental run bookkeeping is unnecessary initially.  Once deficit becomes
small, extend the lexicographic score by the fixed-boundary failures from
Theorem 5.1, then by missing longer upper OR shadows.

This is substantially smaller than raw array SAT: all 924 middle vertices,
the rank-five ledger, and the nineteen-mask portal path remain correct in
every search state.  The remaining central target is precisely

\[
             \Delta(C)=0
\]

together with the three fixed-boundary containment conditions.  Even success
there would still leave lower pinning and complete upper-shadow coverage to
certify.
