# Independent audit: monotone rotor fractional scope and integral fusion

Date: 2026-08-01  
Status: PASS after the corrections incorporated in
`MATH_THEOREM_L_MONOTONE_ROTOR_FRACTIONAL_SCOPE_AND_INTEGRAL_FUSION_GATE_20260801.md`.

## 1. Fractional theorem

The vertex decomposition, short/long/mixed rotor clocks, and labelled
biregular lift were checked independently.  The exact proof-safe range is
`r>=2`, `1<=d<=r-1`; the flow is normalized to mass one per owner; and
available suffix ranks form a set.  Long and mixed rotor edge masses are
respectively `1/binom(b,d)` and `1/binom(b-a,d-a)`.

The triangular corollary requires the canonical values of
`r,W,Lambda,d,h`, an actual left-filled Ferrers board with `sum b_s=h`, and
`b_s=0` beyond its columns.  Its target complementarity is fractional after
the symmetric average.  It is not an integral named-target cover.

## 2. Integral scope

For the complete core-free positive-composition set with uniform marginals,
summing every legal successor inequality forces zero slack termwise.  The
only successor type is cyclic block rotation.  This remains true for a
uniform legal coupling by Birkhoff decomposition and is unaffected by owner
labels.  It does not apply to positive cores, altered multisets, nonuniform
flows, or alternative supports realizing the same rank vector.

The Burnside necklace count and occurrence-edit lower bound were checked:

\[
 \kappa(B,L)={1\over L}\sum_{q\mid\gcd(B,L)}
     \varphi(q)\binom{B/q-1}{L/q-1},
 \qquad
 t\ge\left\lceil{\kappa\over2(r-d)}\right\rceil
       \quad(\kappa>1).                                       \tag{2.1}
\]

The second inequality bounds changed positive-composition occurrences.  It
bounds net named-target damage only with private anchors or an explicit
no-cancellation condition.

For permanent core `K>0`, every arc used by a full successor permutation
has exactly the split form

\[
 (a_0,\ldots,a_d)\mapsto
 (a_0+a_d-t,t,a_1,\ldots,a_{d-1}),
 \quad1\le t\le\min(a_0+a_d-1,K+a_0).                          \tag{2.2}
\]

Thus this face is an assignment-plus-subtour gate, not a proved no-go.

## 3. Protected equivalence

The occurrence-level indegree/outdegree equations plus all proper directed
cut inequalities are exactly one successor cycle.  The compact type flow
expands only with an endpoint-state-conserving literal representative
matching.  Its guarded Ore--Ryser projection is exact only in the odd
middle-level host and only when one fixed `Z` completely encodes all
completion-edge conflicts; otherwise completion variables must remain in
the joint upper/common-cap model.

Finally, a spanning tree of merge macros is sufficient only for a
serial-safe selected set: ports are distinct, each deleted baseline edge is
still live in a rooted processing order, and every switch merges rather than
splits the current components.  Under private payloads, fusing `kappa`
necklaces costs at least `kappa-1` named loads.  Zero or `O(1)` net load
disturbance therefore needs a resource-compatible payload-transparent
spanning system or explicit bounded cancellation.  Pairwise owner/`q1`
disjointness alone proves none of these connector cuts.
