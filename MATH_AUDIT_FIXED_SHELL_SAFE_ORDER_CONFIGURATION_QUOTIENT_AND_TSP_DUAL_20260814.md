# Audit: fixed-shell safe orders, configuration quotient, and the TSP dual

**Date:** 2026-08-14  
**Verdict:** **PASS.**  The exact fixed-shell and complete-orbit degree
formulas, protected-safe order bound, rank-one point-role counterexample,
configuration-quotient codegree calculation, and `q=2` TSP-hardness all
check.  The result is an exact fractional/method theorem, not an integral
ordering theorem.

**Frozen theorem:**
`MATH_THEOREM_FIXED_SHELL_SAFE_ORDER_DEGREES_COMPLETE_ORBIT_FRACTIONAL_FACTOR_AND_RANKONE_NOGO_20260814.md`  
**Theorem SHA-256 (H100):**
`774175a4e68354aa51da5453a676f81851f6486a391f09798223f03051cbbeda`

**Verifier:** `verify_fixed_shell_safe_order_degrees_and_complete_orbit.py`  
**Verifier SHA-256 (H100):**
`551eb73efa806da41a30269ebbb6830e1a747f54ee02e58501eb0c3a06c3cfa9`

**Frozen H100 output SHA-256:**
`ee59f04af45b648fb262eadfd641a9e2c9def2a838eb48a038dd155709469f92`

## 1. Fixed-shell enumeration

There are `(N-1)!` oriented cyclic orders modulo rotation.  A prescribed
`q`-petal is a cyclic window in `q!(N-q)!` orders, while a prescribed
`(q-1)`-petal occurs in `(q-1)!(N-q+1)!` orders.  Positioning two cyclic
arcs and assigning labels to overlap, differences, and exterior gives the
three displayed codegree families.

For an incident owner/facet petal pair, the lower arc is obtained by
deleting either endpoint of the owner arc.  Hence the mixed codegree is
`2(q-1)!(N-q)!`, a `2/q` fraction of the owner degree.  This large
correlation is exact, not an artefact of a loose estimate.

## 2. Protected safety

A fixed core lies below at most `2^(q-1)` transversal lower sets.  It lies
below at most `(2c+q-1)2^(q-2)` lifted owners: split according to whether
the core already contains the lifted owner's double pair.  Multiplying by
the uniform window probabilities and union-bounding gives the stated unsafe
fraction.  At `N=2q+O(1)`, `p=Theta(q^2)`, it is exponentially small in
`q`.  Thus every shell retains safe cyclic orders eventually.

This does not imply that every residual named vertex is eligible in some
shell.

## 3. Complete-orbit fractional factor

Choosing the core inside a fixed owner or lower set, choosing the remaining
support outside it, and multiplying by the fixed-shell degree gives the
same common degree on both equal shores:

\[
                         D_N={R!(R-1)!\over c!(R-1-N+q)!}.
\]

Uniform reciprocal weights therefore form an exact fractional perfect
matching.  The same core/support count combined with the local arc formulas
gives every same-shore and mixed codegree in the theorem.

## 4. Configuration quotient

Contracting the two incident facet occurrences into each owner occurrence
removes the normalized `2/R` mixed codegree from the external collision
ledger.  Same-shore distance-one pairs then have normalized codegree

\[
                         2/(R(R-1)).
\]

For a nonincident mixed pair put `j=q-s`, `s>=2`.  Direct simplification
gives

\[
 {\deg(A,L)\over D_N}
 ={2s!(s-1)!(R-s)!^2\over R!(R-1)!}.
\]

The ratio of successive terms is `s(s+1)/(R-s)^2<1`; the maximum at `s=2`
is `4/(R(R-1)^2)`.  Hence every external normalized pair codegree is
`O(k^(-2))`, and a configuration of rank `Theta(q)` has squared-rank
collision `O(q^2/k^2)=O(k^(-1))` centrally.

This restores favorable diagonal geometry but does not invoke a theorem:
the quoted Delcourt--Postle `A`-perfect results fix the rank before the
degree limit, whereas this configuration rank grows as `Theta(sqrt k)`.
A uniform growing-rank extension and the relevant partite degree hypotheses
remain unproved.

## 5. Point-role and Birkhoff no-gos

Repeating only one cyclic orbit block per period gives exact point roles,
but the union of eligible named owners and lower sets has size only
`k exp(O(q))=o(W)`.  A named vertex outside that union separates the
fractional order polytope, while every point-additive dual weight passes.
Therefore rank-one point weights are not a complete dual family.

At `q=2`, owner petals are edges of a Hamilton cycle and lower petals are
singletons independent of order.  Arbitrary owner weights turn the token
max-order problem into maximum-weight Hamilton cycle.  Its `0/1` threshold
version contains Hamilton-cycle decision, so it is NP-hard.  The order
polytope is the symmetric TSP polytope and cannot be replaced by Birkhoff
assignment constraints without subtour rows, unless `P=NP`.

## 6. H100 replay

All finite enumeration, compilation, and hashing were performed through
`ssh h100`.  The verifier exhaustively checked fixed shells `(N,q)=(6,2)`
and `(7,3)`.  It also materialized the complete parameterized orbit at
`(p,q,N)=(5,2,6)`:

* `277200` parameterized rails;
* common owner/lower degree `3600`; and
* incident owner--lower codegree `1200=2D/R`.

The replay is not a protected fixed-bank fractional solver.

## 7. Scope

The theorem proves a complete unrestricted fractional factor and identifies
the correct incidence-aware quotient scale.  It also proves that point-role
balance and naive Birkhoff rounding are insufficient.  Safe fractional
feasibility for the explicit nonuniform protected bank, growing-rank
configuration matching, integral ordering, upper support, and chronology
remain open.
