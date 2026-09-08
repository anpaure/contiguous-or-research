# Independent audit of the `k=17` phase-free history master and Pascal pivot reset

**Date:** 2026-08-02  
**Status:** proof/source audit PASS for the directed positive-residence
encoding; one all-`k` quotient qualification and one recursive boundary
guard are essential.  No SAT status or word claim is made.

## 1. Audited objects

The audit covers

```text
MATH_THEOREM_K17_PHASE_FREE_DIRECTED_HISTORY_MASTER_20260802.md
scratch/build_k17_marker58_directed_history_master_20260802.cpp
MATH_THEOREM_K_DIRECTED_HISTORY_PORT_MONOID_AND_PIVOT_RESET_20260802.md
```

The C++ source compiles under `clang++ -std=c++20 -fsyntax-only`.
The audit did not run the large generated CNF or any solver.

## 2. Exact transition semantics

Normalize a selected physical transition to the canonical frame at its
tail.  Write it as

\[
 S_u\longrightarrow \rho^\delta S_v,
 \qquad S_u-\rho^\delta S_v=\{a\},
 \qquad \rho^\delta S_v-S_u=\{b\}.
\]

If `(h_1,h_2,h_3)` are the three most recent inserted coordinates in the
tail frame, the exact head-frame update is

\[
 (h_1,h_2,h_3)\longmapsto
 (b-\delta,h_1-\delta,h_2-\delta),
 \tag{2.1}
\]

and it is legal exactly when

\[
                         a\notin\{h_1,h_2,h_3\}.
\tag{2.2}
\]

Equation (2.2) excludes precisely insertion-to-next-deletion distances
one, two, and three.  Hence it is equivalent to every bounded cyclic
positive run having length at least four.  It does not impose the dual
condition on zero runs.

The sign in (2.1) is correct.  The source normalization is
`physical_source = rot(S_u,g)` and the head normalization is
`physical_target = rot(S_v,g+delta)`.  A fixed absolute coordinate
therefore loses `delta` when re-expressed in the head frame.

As an independent off-by-one check, all rooted directed simple cycles of
lengths three through eight in `J(5,2)` were enumerated.  There were
`108900` cycles.  For each `d=1,2,3`, direct cyclic positive-run lengths
agreed with the last-`d` insertion test on every cycle; there were zero
discrepancies.  This is a semantic calibration, not an audit of the frozen
`k=17` catalogue.

## 3. CNF/source audit

For every nonloop residual option the builder creates two orientation
variables and enforces their sum to the primary.  For every protected edge
it selects exactly one of the two directions.  It kills the eight quotient
self-loop options.  Conditional on the independently audited base
degree-two rows, one nonempty incoming clause and one nonempty outgoing
clause at each owner imply directed indegree and outdegree exactly one.

The source counts recompute as follows.

```text
nonloop edge orbits                     35937
directed arc variables              2*35937 = 71874
history variables                 1430*3*17 = 72930

orientation and loop clauses                         143292
incoming/outgoing clauses                              2860
history exactly-one clauses              1430*3*(1+C(17,2)) = 587730
arc/history clauses                          71874*(1+3+2*17) = 2731212
                                                     --------
added clauses                                         3465094
```

Thus `204167+71874+72930=348971` variables and
`439463+3465094=3904557` clauses are correct.  The transport implications
are one-way clauses syntactically, but exact-one history at the tail and
head turns them into equality on every selected arc.

The builder checks the supplied map rows against their physical endpoint,
facet, owner, cap, and voltage records.  It does not regenerate the base
catalogue or prove the base degree/resource semantics; those remain an
external authenticated premise.  Its loop deletion is lossless for the
eventual connected quotient target, not for an unconstrained catalogue of
all disconnected cycle covers.

## 4. Why the selected transition carries phase at `k=17`

The undirected primary does not by itself choose a direction.  Once one of
its two directed variables is selected, its physical endpoint record fixes
the relative phase `delta`; no absolute phase variable is needed.

This is exact here because every rank-nine `Z_17` owner orbit is free.  A
nonidentity rotation of a prime cycle is transitive on the seventeen
coordinates, so its only invariant subsets are the empty and full sets.
A rank-nine owner therefore has trivial stabilizer.

This qualification is load-bearing in an all-`k` statement.  For a
periodic owner orbit a quotient edge generally fixes only a stabilizer
double coset.  One must either

1. refine the owner state by its coset in `Gamma/Gamma_u`, or
2. prove that the chosen dart and history are invariant under every
   stabilizer ambiguity.

Without one of these additions, one unrefined history tuple per owner orbit
is not an exact phase-free encoding.  The general port-monoid theorem was
corrected to state the free-orbit hypothesis and this coset repair.

## 5. Exact recursive composition and the pivot reset

For depth `d`, a directed transition `(a,b)` acts on a history tuple by the
partial map

\[
 \tau_{a,b}(h_1,\ldots,h_d)
   =(b,h_1,\ldots,h_{d-1}),
 \qquad a\notin\{h_1,\ldots,h_d\}.
\tag{5.1}
\]

Path concatenation is composition of these partial maps.  A cyclic splice
is positive-resident exactly when the composed map has a consistent fixed
point.  Thus residence is a genuine compositional port relation, separate
from the Boolean rail/cap relation.

The asymmetric one-cell pivot has `d` owner transitions with deletion and
insertion banks

\[
 (\ell,\lambda_{d-1},\ldots,\lambda_1),
 \qquad
 (\rho_1,\ldots,\rho_{d-1},\mu),
\tag{5.2}
\]

which are disjoint.  Its partial map is defined exactly when

\[
 a_t\notin\{h_1,\ldots,h_{d-t+1}\}
                     \quad(1\le t\le d),
\tag{5.3}
\]

and then has constant output

\[
                  (\mu,\rho_{d-1},\ldots,\rho_1).
\tag{5.4}
\]

Hence the pivot is a literal `d`-transition reset: the incoming history is
forgotten.  Its persistent ordered `(d-1)`-rail supplies all but the first
entry of (5.4); one terminal insertion label supplies the remaining entry.
This is the precise way in which the aperture/pivot module can transport a
finite residence state without accumulating one raw run blocker per
generation.

## 6. Sharp boundary obstruction and weakest extra hypothesis

The same ordered rail and mutual Boolean-cap containment do not imply
history compatibility.  After the pivot, append the legal Johnson edge
which deletes `mu`.  The coordinate `mu` was inserted on the immediately
preceding pivot edge, so it has a positive run of length one.  This
extension can leave the rail and cap containments unchanged.  Likewise a
later boundary edge can delete one of the `rho_j` before it ages past `d`.

Therefore a protected Pascal port must additionally export either

\[
                  \mathcal R_d(P)
       =\{(H,H'): \Phi_P(H)=H'\},
\tag{6.1}
\]

or, on the pivot-reset face, the constant tuple (5.4) together with the
triangular input domain (5.3).  Two ports splice residence-safely exactly
when the composed child, seam, and correction relations have a fixed point
(or the corresponding open-path relation is nonempty).  This is the
weakest exact extra compatibility row; cap containment alone cannot replace
it.

For a bounded packet with at least `d` transitions, the output depends only
on its last `d` insertions, so a reset bank is regenerative.  This is a
finite-state theorem, not an existence theorem for compatible Pascal child
menus.

## 7. Exact scope

For the frozen `k=17` base, the eager master retains the externally audited
rank-nine owner degree, exact rank-eight lower-q1 ownership, protected edge
bank, and rank-ten coverage, and adds exact positive depth-three residence
on its directed quotient cycle cover.

It does **not** close:

* quotient connectivity or nonzero component voltage;
* literal physical decode/replay and a linear opening;
* negative-run residence, unless the dual automaton is also imposed;
* upper ranks eleven through seventeen;
* source-letter factorization or nonempty envelopes; or
* the lower common-cap/compiler matching and exhaustive word verification.

For the all-`k` Pascal bridge, the pivot reset closes only the compositional
positive-residence interface.  Existence of rail/cap-compatible closing
ports, one-copy owner/target payload, upper completeness, the ambient
residence collars, and terminal common-cap feasibility remain logically
separate.
